# OCLP-R SwiftUI Front-end

Native macOS SwiftUI shell that drives the existing Python patcher
(`oclp_r`) as a subprocess. The Python backend and all patcher logic are
unchanged — this is a UI-only migration.

## Architecture

- **Thin shell + subprocess.** Each screen launches the Python patcher
  (`OCLP-R-GUI.command`) with existing CLI flags and streams its log output
  into a live console.
- **JSON bridge** for read-only queries and disk/install operations. Four
  additive CLI commands were added to the backend (nothing removed):

  | Command | Purpose |
  | --- | --- |
  | `--print_info` | Host model, OS version, build capability, supported models, effective settings |
  | `--print_patches` | Detected root patches + `can_patch` / `can_unpatch` |
  | `--set_settings <json>` | Persist `{"gui": {...}, "global": {...}}` settings (same store as wx) |
  | `--list_disks` | Installable disks (FAT32/EFI) |
  | `--list_partitions <disk>` | FAT32/EFI partitions on a disk |
  | `--install_oc <partition>` | Install a built OpenCore config to a partition |
  | `--list_installers` | macOS InstallAssistant catalog (Apple sucatalog) |
  | `--list_kdk` / `--list_metallib` | KDK / Metallib catalogs (dortania manifests) |
  | `--list_ipsw` | IPSW catalog (ipsw.me, Apple fallback) |
  | `--list_local_installers` | Installed `Install macOS*.app` in /Applications |
  | `--download <json>` | Download a file (url/path/size), streams `@@P@@` progress |
  | `--extract_installer <pkg>` | Install InstallAssistant.pkg to /Applications |
  | `--flash_installer <json>` | Flash installer to disk (installer_path/disk) |

  They emit a sentinel-delimited JSON envelope on stdout:
  ```
  @@OCLPR_RESULT_BEGIN@@
  { ... }
  @@OCLPR_RESULT_END@@
  ```
  Implemented in `oclp_r/support/swift_bridge.py`.

- **Settings** are read through the bridge (effective values after defaults)
  and written to the shared `/Users/Shared/.com.hackdoc.oclp-r.plist` using the
  same `GUI:<constants attribute>` keys as the wx GUI, so both front-ends share
  one settings store. Only keys the user actually changes are written.

- **Build / root patch / settings** reuse the existing CLI flags directly
  (`--build`, `--verbose`, `--disable_sip`, `--patch_sys_vol`, etc.).
  Settings are held in-app and passed as flags; the target model becomes
  `--model <model>`.

## Layout

```
SwiftUI/
  Package.swift                  Swift Package (executable target "OCLPR")
  Sources/OCLPR/
    OCLPRApp.swift               @main + navigation routes
    AppConfig.swift              repo-root / launcher resolution
    Models/
      PythonBridge.swift         subprocess runner + JSON envelope parsing
      AppState.swift             settings + host info (ObservableObject)
      Models.swift               Codable payloads (HostInfo, Disk, …)
    Views/
      MainMenuView.swift
      SettingsView.swift
      BuildView.swift
      InstallView.swift
      RootPatchView.swift
      HelpView.swift
      LogConsoleView.swift
  scripts/make-app.sh            build + assemble .app bundle
```

## Build & run

```bash
cd SwiftUI
swift build

# Run from the repo root so the Python package is importable:
cd ..
OCLPR_REPO="$PWD" swift run --package-path SwiftUI OCLPR
```

Or assemble an `.app` bundle:

```bash
cd SwiftUI && ./scripts/make-app.sh
```

The Python interpreter is auto-detected (`python3.14` preferred), matching the
dev machine. Set `OCLPR_REPO` to the checkout root when the current directory
is not the repo root.
