# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Kotlinter Gradle plugin (`org.jmailen.kotlinter` 5.4.2) wired into the build for Kotlin lint and formatting.
- Detekt Gradle plugin (`dev.detekt` 2.0.0-alpha.3) with a `detekt { ... }` configuration block.
- `.editorconfig` pinning charset, end-of-line, indent style, and ktlint rule overrides so kotlinter aligns with the project's existing Kotlin style.
- Makefile targets: `help` (self-documenting target list), `lint`, `format`, `detekt`, `detekt-baseline`.
- Makefile guard `_require-gradle-version` that fails fast if the Gradle version cannot be read from `gradle/libs.versions.toml`.

### Changed
- Bumped `readingbat-core` to 3.1.8.
- `Content.kt` now imports `ReturnType` directly instead of `ReturnType.*`; all challenge registrations qualify return types (e.g., `ReturnType.IntType`).
- Makefile `build` and `cc` targets use the canonical `-x test` flag instead of `-xtest`.
- Reordered `.PHONY` to match the in-file target definition order.

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
