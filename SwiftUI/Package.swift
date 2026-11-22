// swift-tools-version: 5.9
import PackageDescription

let package = Package(
    name: "OCLPR",
    platforms: [.macOS(.v14)],
    targets: [
        .executableTarget(
            name: "OCLPR",
            path: "Sources/OCLPR"
        )
    ]
)
