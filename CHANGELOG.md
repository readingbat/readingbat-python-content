# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

Nothing yet.

## [1.1.0] - 2026-09-21

Dependency and toolchain refresh, plus line-ending normalization. No runtime
behavior, challenge content, or public DSL has changed.

### Added
- `.gitattributes` normalizing line endings on commit: `text=auto` by default, LF enforced for `gradlew`, `*.sh`, and `*.py`, CRLF for `*.bat`, and `*.jar` marked binary.

### Changed
- Upgraded the Gradle wrapper from 9.6.1 to 9.7.1.
- Bumped dependencies: Ktor → 3.6.0, Kotest → 6.2.5, `readingbat-core` → 3.4.0.
- Bumped build plugins: kotlinter → 5.7.0, detekt → 2.0.0-alpha.6, versions plugin → 0.64.0.
- `gradlew.bat` was renormalized to CRLF and the Gradle wrapper jar refreshed as part of the wrapper upgrade.

### Documentation
- Reconstructed a `[1.0.0]` section in this changelog from Git history, replacing the former catch-all "Pre-1.0.1 history" heading, and added Keep a Changelog compare links for every release.
- Documented the `.gitattributes` line-ending policy in `README.md`, `CLAUDE.md`, and `llms.txt`.
- Added the CI workflow to the `llms.txt` development section.

## [1.0.1] - 2026-08-01

Tooling, CI, and toolchain upgrades. No runtime behavior, challenge content,
or public DSL has changed.

### Added
- Kotlinter Gradle plugin (`org.jmailen.kotlinter`) wired into the build for Kotlin lint and formatting.
- Detekt Gradle plugin (`dev.detekt` 2.0.0-alpha.5) with a `detekt { ... }` configuration block.
- `.editorconfig` pinning charset, end-of-line, indent style, and ktlint rule overrides so kotlinter aligns with the project's existing Kotlin style.
- GitHub Actions CI (`.github/workflows/ci.yml`) running `make lint` and `make tests` as parallel jobs on every push and pull request to `master`, with Gradle caching, concurrency cancellation, and uploaded lint/test reports.
- Makefile targets: `help` (self-documenting target list), `lint`, `format`, `detekt`, `detekt-baseline`, `versions`, `upgrade-wrapper`.
- Makefile guard `_require-gradle-version` that fails fast if the Gradle version cannot be read from `gradle/libs.versions.toml`.

### Changed
- Raised the JVM toolchain from Java 17 to Java 25 (`jvm` in `gradle/libs.versions.toml`).
- Upgraded the Gradle wrapper from 9.5.0 to 9.6.1.
- Bumped dependencies to their current versions: Kotlin → 2.4.10, Ktor → 3.5.1, Kotest → 6.2.3, `readingbat-core` → 3.3.1, `common-utils` → 3.2.2, `kotlin-logging` → 8.0.4, kotlinter → 5.6.0, detekt → 2.0.0-alpha.5, versions plugin → 0.57.0.
- Moved the dependency-updates plugin from the retired `com.github.ben-manes.versions` id to `io.github.ben-manes.versions`.
- Refactored `build.gradle.kts` into per-concern helper functions (`configureKotlin`, `configureDetekt`, `configureKotlinter`, `configureKtor`, `configureShadowJar`, `configureTest`, `configureVersions`).
- Enabled the Kotlin unused-return-value checker (`-Xreturn-value-checker=check`) on production code only (the test source set is excluded to avoid false positives from Kotest's fluent assertions).
- Build the fat jar via Ktor's `fatJar` task; the `dependencyUpdates` check now rejects pre-release candidates for dependencies currently on a stable version.
- Renamed the `gradle` version key to `gradle-wrapper` in `gradle/libs.versions.toml`.
- Renamed the Makefile `versioncheck` target to `versions`, made `help` the default target, and added `--no-configuration-cache --no-parallel` to the dependency-update check.
- `Content.kt` now imports `ReturnType` directly instead of `ReturnType.*`; all challenge registrations qualify return types (e.g., `ReturnType.IntType`).
- Makefile `build` and `cc` targets use the canonical `-x test` flag instead of `-xtest`.
- Reordered `.PHONY` to match the in-file target definition order.
- Trimmed `CLAUDE.md` to the guidance the codebase cannot teach on its own, removing the source-file layout, the Python file-pattern code block, the Test Structure paragraph, the `make` target table, the toolchain/lint stack line, and the CI section — all of which are derivable from the repository itself.
- Corrected the topic-group list in `llms.txt`, which named 6 of the 14 groups under `python/`.

### Removed
- Makefile `heroku` and `logs` targets.

### Fixed
- `ContentTests` now calls `correctAnswers()` as a function, matching the upgraded `readingbat-kotest` API (previously a property).

### Upgrade notes
- `common-utils` crossed a major version (2.9.3 → 3.2.2) during this cycle. The build and full test suite pass against it, but treat it as the highest-risk item if you pin transitively.

## [1.0.0] - 2026-05-08

Tagged retroactively on 2026-08-01. The repository carried `version=1.0.0`
from PR #11 onward but was never tagged at the time, and no changelog was kept
during this period — the entries below are reconstructed from Git history and
are less complete than later ones. Structured changelog tracking begins with
1.0.1.

### Added
- 80 new challenges across 8 new topic groups, bringing the repository to 14 topic groups under `python/`: `warmup1`, `math_ops`, `boolean_exprs`, `type_conv`, `if_stmts`, `string_ops`, `string_methods`, `for_loops`, `while_loops`, `lists`, `nested_loops`, `tuples`, `dictionaries`, `list_comps`.
- Student hints across all Python challenge files, with a consistent `@desc` format.
- `readingbat-kotest` test dependency.

### Changed
- Migrated dependency resolution from JitPack to Maven Central.
- Consolidated string literals and centralized versions in `gradle/libs.versions.toml` (#12).
- Fixed the Gradle 9.5 build, refreshed dependencies, and aligned make targets (#11).
- Bumped the Gradle wrapper to 9.5.0; JVM toolchain on Java 17.
- Dependency versions as of this tag: Kotlin 2.3.21, Ktor 3.4.3, Kotest 6.1.11, `readingbat-core` 3.1.5, `common-utils` 2.8.2, `kotlin-logging` 8.0.02.
- Rewrote tests in Kotest's `StringSpec()` `init` style.
- Reordered challenge groups by difficulty — warmups first, list comprehensions last.

### Removed
- `list_comp10` challenge.

### Fixed
- `andor7` function name mismatch, and the unregistered `front_back` challenge.
- Several incorrect challenge return types.

[Unreleased]: https://github.com/readingbat/readingbat-python-content/compare/1.1.0...master
[1.1.0]: https://github.com/readingbat/readingbat-python-content/compare/1.0.1...1.1.0
[1.0.1]: https://github.com/readingbat/readingbat-python-content/compare/1.0.0...1.0.1
[1.0.0]: https://github.com/readingbat/readingbat-python-content/commits/1.0.0
