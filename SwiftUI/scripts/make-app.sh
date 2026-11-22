#!/bin/bash
# Build the native SwiftUI front-end and assemble a runnable .app bundle.
# Usage: ./scripts/make-app.sh
set -euo pipefail

cd "$(dirname "$0")/.."

APP_NAME="OCLP-R-Swift"
BUNDLE="${APP_NAME}.app"
EXECUTABLE="OCLPR"
REPO_ROOT="$(cd .. && pwd)"

swift build -c release

rm -rf "${BUNDLE}"
mkdir -p "${BUNDLE}/Contents/MacOS" "${BUNDLE}/Contents/Resources"

cp ".build/release/${EXECUTABLE}" "${BUNDLE}/Contents/MacOS/${EXECUTABLE}"

cat > "${BUNDLE}/Contents/Info.plist" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleName</key>
    <string>OCLP-R-Swift</string>
    <key>CFBundleDisplayName</key>
    <string>OCLP-R</string>
    <key>CFBundleIdentifier</key>
    <string>com.hackdoc.oclp-r-swift</string>
    <key>CFBundleExecutable</key>
    <string>OCLPR</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleShortVersionString</key>
    <string>0.1.0</string>
    <key>CFBundleVersion</key>
    <string>1</string>
    <key>LSMinimumSystemVersion</key>
    <string>14.0</string>
    <key>NSHighResolutionCapable</key>
    <true/>
    <key>NSPrincipalClass</key>
    <string>NSApplication</string>
    <key>OCLPRRepoRoot</key>
    <string>${REPO_ROOT}</string>
</dict>
</plist>
PLIST

echo "Built ${BUNDLE} (repo root: ${REPO_ROOT})"
