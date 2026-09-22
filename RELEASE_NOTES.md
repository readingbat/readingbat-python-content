# Release Notes

## 1.1.0 — dependency refresh and line-ending normalization

A maintenance release: current versions of the build toolchain and runtime
dependencies, plus a `.gitattributes` file that normalizes line endings across
platforms. No runtime behavior, challenge content, or public DSL has changed.

### Highlights

- **Gradle wrapper → 9.7.1.** Up from 9.6.1.
- **Dependency upgrades.** Ktor → 3.6.0, Kotest → 6.2.5, `readingbat-core` →
  3.4.0. Kotlin (2.4.10), `common-utils` (3.2.2), and `kotlin-logging` (8.0.4)
  are unchanged from 1.0.1.
- **Build plugin upgrades.** kotlinter → 5.7.0, detekt → 2.0.0-alpha.6,
  versions plugin → 0.64.0.
- **`.gitattributes`.** Line endings are now normalized on commit: `text=auto`
  by default, LF enforced for `gradlew`, `*.sh`, and `*.py`, CRLF for `*.bat`,
  and `*.jar` treated as binary. This keeps the Python challenge files and the
  Gradle wrapper scripts stable regardless of the contributor's platform.

### Documentation

- The changelog now carries a reconstructed `[1.0.0]` section (built from Git
  history after the tag was created retroactively), replacing the former
  catch-all "Pre-1.0.1 history" heading, plus compare links for every release.
- `README.md`, `CLAUDE.md`, and `llms.txt` document the new line-ending policy.
- `llms.txt` now mentions the GitHub Actions CI workflow alongside the other
  development commands.

### Upgrade notes

- Contributors on Windows may see `gradlew.bat` show as modified the first time
  they pull, as Git renormalizes it to CRLF under the new `.gitattributes`.
  Running `git add --renormalize .` once resolves it.
- Run `./gradlew --refresh-dependencies` (or `make build`) once after pulling so
  the new plugin and dependency versions resolve.
- The Java 25 toolchain requirement from 1.0.1 is unchanged.

### Full diff

See the [compare view on
GitHub](https://github.com/readingbat/readingbat-python-content/compare/1.0.1...1.1.0)
for the complete set of changes in this release.

## 1.0.1 — tooling, CI, and dependency upgrades

This release focuses on developer ergonomics, continuous integration, and
toolchain/dependency upgrades. No runtime behavior, challenge content, or
public DSL has changed.

### Highlights

- **Kotlin linting and formatting.** The build applies the
  [kotlinter](https://github.com/jeremymailen/kotlinter-gradle) Gradle plugin
  (5.6.0). Run `make lint` to check Kotlin sources, and `make format` to apply
  fixes.
- **Detekt static analysis.** Detekt is wired up via the `dev.detekt` plugin
  (2.0.0-alpha.5) and a `detekt { ... }` block in `build.gradle.kts`. Use
  `make detekt` to run it standalone, or `make detekt-baseline` to (re)generate
  the baseline.
- **GitHub Actions CI.** A new `.github/workflows/ci.yml` runs `make lint` and
  `make tests` as parallel jobs on every push and pull request to `master`,
  with Gradle caching, concurrency cancellation, and uploaded reports.
- **Self-documenting Makefile.** Run `make help` for a colorized list of every
  target, generated from `## ` annotations in the Makefile itself.
- **`.editorconfig`.** Pins charset, EOL, indent width, and the set of ktlint
  rules disabled to match the existing Kotlin style.
- **JVM toolchain → Java 25.** The Gradle toolchain now targets Java 25
  (previously Java 17); Gradle can auto-provision it.
- **Dependency upgrades.** Kotlin → 2.4.10, Ktor → 3.5.1, Kotest → 6.2.3,
  `readingbat-core` → 3.3.1, `common-utils` → 3.2.2, `kotlin-logging` → 8.0.4.
  The Gradle wrapper moved from 9.5.0 to 9.6.1.
- **Build script cleanup.** `build.gradle.kts` is reorganized into per-concern
  helper functions, the fat jar is built via Ktor's `fatJar` task, the Kotlin
  unused-return-value checker runs over production code, and `dependencyUpdates`
  now filters out pre-release candidates for stable dependencies.

### Source-level changes

- `Content.kt` no longer wildcard-imports `ReturnType.*`; all return types are
  qualified (e.g., `ReturnType.IntType`). When adding new challenges, use the
  qualified form.
- The dependency-updates plugin moved from the retired
  `com.github.ben-manes.versions` id to `io.github.ben-manes.versions` (0.57.0).
- The `gradle` version key in `gradle/libs.versions.toml` was renamed to
  `gradle-wrapper`.
- The Makefile `versioncheck` target was renamed to `versions`, `help` is now
  the default target, and the dependency-update check runs with
  `--no-configuration-cache --no-parallel`.
- The Makefile uses the canonical `-x test` flag (with a space) in `build` and
  `cc` targets, replacing the deprecated `-xtest` short form.

### Documentation

- `CLAUDE.md` was trimmed to the guidance the codebase cannot teach on its own.
  The source-file layout, Python file-pattern code block, Test Structure
  paragraph, `make` target table, toolchain/lint stack line, and CI section
  were removed — each is derivable from the repository itself. The Content DSL
  section, the `ReturnType` qualification note, the `main()`-prints test-case
  contract, and the Adding a New Challenge checklist remain.
- `llms.txt` listed 6 of the 14 topic groups under `python/`; the list is now
  complete.

### Upgrade notes

- Java 25 is now the toolchain target. Gradle will auto-provision a matching
  JDK; ensure toolchain auto-download is enabled or a Java 25 JDK is installed.
- `common-utils` crossed a major version during this cycle (2.9.3 → 3.2.2). The
  build and full test suite pass against it, but treat it as the highest-risk
  item if you pin it transitively.
- If you referenced the dependency-updates plugin by id anywhere outside
  `libs.versions.toml`, update it to `io.github.ben-manes.versions`.
- After pulling, run `./gradlew --refresh-dependencies` (or `make build`) once
  so the new plugins and dependencies resolve.
- Existing developer workflows are unchanged; the new `lint` / `format`
  targets are optional but recommended before pushing.

### Full diff

See the [compare view on
GitHub](https://github.com/readingbat/readingbat-python-content/compare/1.0.0...1.0.1)
for the complete set of changes in this release.
