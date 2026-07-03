# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Kotlinter Gradle plugin (`org.jmailen.kotlinter` 5.5.0) wired into the build for Kotlin lint and formatting.
- Detekt Gradle plugin (`dev.detekt` 2.0.0-alpha.5) with a `detekt { ... }` configuration block.
- `.editorconfig` pinning charset, end-of-line, indent style, and ktlint rule overrides so kotlinter aligns with the project's existing Kotlin style.
- GitHub Actions CI (`.github/workflows/ci.yml`) running `make lint` and `make tests` as parallel jobs on every push and pull request to `master`, with Gradle caching, concurrency cancellation, and uploaded lint/test reports.
- Makefile targets: `help` (self-documenting target list), `lint`, `format`, `detekt`, `detekt-baseline`, `versions`, `upgrade-wrapper`.
- Makefile guard `_require-gradle-version` that fails fast if the Gradle version cannot be read from `gradle/libs.versions.toml`.

### Changed
- Raised the JVM toolchain from Java 17 to Java 25 (`jvm` in `gradle/libs.versions.toml`).
- Upgraded the Gradle wrapper from 9.5.0 to 9.6.1.
- Bumped dependencies: Kotlin → 2.4.0, Ktor → 3.5.1, Kotest → 6.2.1, `readingbat-core` → 3.2.1, `common-utils` → 2.9.3, `kotlin-logging` → 8.0.4, kotlinter → 5.5.0, detekt → 2.0.0-alpha.5.
- Refactored `build.gradle.kts` into per-concern helper functions (`configureKotlin`, `configureDetekt`, `configureKotlinter`, `configureKtor`, `configureShadowJar`, `configureTest`, `configureVersions`).
- Enabled the Kotlin unused-return-value checker (`-Xreturn-value-checker=check`) on production code only (the test source set is excluded to avoid false positives from Kotest's fluent assertions).
- Build the fat jar via Ktor's `fatJar` task; the `dependencyUpdates` check now rejects pre-release candidates for dependencies currently on a stable version.
- Renamed the `gradle` version key to `gradle-wrapper` in `gradle/libs.versions.toml`.
- Renamed the Makefile `versioncheck` target to `versions`, made `help` the default target, and added `--no-configuration-cache --no-parallel` to the dependency-update check.
- `Content.kt` now imports `ReturnType` directly instead of `ReturnType.*`; all challenge registrations qualify return types (e.g., `ReturnType.IntType`).
- Makefile `build` and `cc` targets use the canonical `-x test` flag instead of `-xtest`.
- Reordered `.PHONY` to match the in-file target definition order.

### Removed
- Makefile `heroku` and `logs` targets.

### Fixed
- `ContentTests` now calls `correctAnswers()` as a function, matching the upgraded `readingbat-kotest` API (previously a property).

## [Pre-Unreleased history]

Prior changes were tracked only via Git history; see `git log` for details.
Notable recent work includes:

- Consolidated string literals and centralized versions (#12).
- Fixed the Gradle 9.5 build, refreshed dependencies, and aligned make targets (#11).
- Bumped the Gradle wrapper to 9.5.0.
- Bumped Kotlin to 2.3.21, Ktor to 3.4.3, ReadingBat to 3.1.4, Utils to 2.8.1; added `readingbat-kotest` test dependency.
- Added 80 new challenges across 8 new topic groups.
- Improved student hints across all Python challenge files.

[Unreleased]: https://github.com/readingbat/readingbat-python-content/commits/master
