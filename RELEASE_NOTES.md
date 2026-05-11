# Release Notes

## Unreleased — Kotlinter, detekt, and Makefile help

This release focuses on developer ergonomics and code-style enforcement. No
runtime behavior, content, or public DSL has changed.

### Highlights

- **Kotlin linting and formatting.** The build now applies the
  [kotlinter](https://github.com/jeremymailen/kotlinter-gradle) Gradle plugin.
  Run `make lint` to check Kotlin sources, and `make format` to apply fixes.
- **Detekt static analysis.** Detekt is wired up via the `dev.detekt` plugin
  and a `detekt { ... }` block in `build.gradle.kts`. Use `make detekt` to run
  it standalone, or `make detekt-baseline` to (re)generate the baseline.
- **Self-documenting Makefile.** Run `make help` for a colorized list of every
  target, generated from `## ` annotations in the Makefile itself.
- **`.editorconfig`.** New file pinning charset, EOL, indent width, and the
  set of ktlint rules disabled to match the existing Kotlin style.
- **Dependency bump.** `readingbat-core` updated from 3.1.5 to 3.1.8.

### Source-level changes

- `Content.kt` no longer wildcard-imports `ReturnType.*`; all return types are
  qualified (e.g., `ReturnType.IntType`). When adding new challenges, use the
  qualified form.
- The Makefile uses the canonical `-x test` flag (with a space) in `build` and
  `cc` targets, replacing the deprecated `-xtest` short form.

### Upgrade notes

- After pulling, run `./gradlew --refresh-dependencies` (or `make build`) once
  so the new plugins resolve.
- Existing developer workflows are unchanged; the new `lint` / `format`
  targets are optional but recommended before pushing.

### Full diff

See the [compare view on
GitHub](https://github.com/readingbat/readingbat-python-content/compare/179e26e...master)
for the complete set of changes since the previous merge.
