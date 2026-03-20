# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

ReadingBat Python content repository — Python programming challenges served via a Kotlin-based ReadingBat server. Students solve challenges in the browser; the server evaluates answers by running the Python functions against test cases defined in each file's `main()`.

## Architecture

**Two-language system**: Kotlin defines and serves challenges; Python files *are* the challenges.

- `src/main/kotlin/Content.kt` — DSL configuration defining all challenge groups, mapping Python files to return types
- `src/main/kotlin/ContentServer.kt` — Entry point, top-level `main` that delegates to `ReadingBatServer.start()`
- `python/` — Challenge files organized by topic subdirectory (e.g., `boolean_exprs/`, `string_ops/`)
- `src/test/kotlin/ContentTests.kt` — Validates all challenges accept correct answers and reject wrong ones
- `src/main/resources/application.conf` — HOCON config for Ktor server (port, production flag, content file location)

### Content DSL (Content.kt)

Challenges are registered two ways:
1. **Individually**: `challenge("name") { returnType = BooleanType }` — explicit per-file
2. **Bulk via glob**: `includeFilesWithType = "pattern*.py" returns Type` — auto-includes matching files

Return types: `BooleanType`, `StringType`, `IntType`, `BooleanListType`, `IntListType`, `StringListType`

**Source switching**: Production reads from GitHub (`GitHubRepo`); development reads from local filesystem (`FileSystemSource`), controlled by `isProduction()`.

### Python Challenge File Pattern

Each `.py` file follows this structure:
```python
# @desc Description with optional **markdown**

def challenge_name(param1, param2):
    # implementation
    return result

def main():
    print(challenge_name(arg1, arg2))  # each print = one test case

if __name__ == '__main__':
    main()
```

The `main()` prints define the test cases — each `print()` call produces an expected answer that the server checks against student submissions.

### Test Structure

Tests use Ktor's `testApplication` with ReadingBat's `TestSupport` DSL. The DSL iterates `content.forEachLanguage { forEachGroup { forEachChallenge { ... } } }` and verifies three things per challenge: empty answers → NOT_ANSWERED, wrong answers → INCORRECT, correct answers → CORRECT with no hint.

## Development Commands

```bash
make compile          # Build without tests (./gradlew build -x test)
make tests            # Run all tests (./gradlew --rerun-tasks check)
make run              # Start the server (./gradlew run), port 8080
make cc               # Continuous compilation, no tests
make versioncheck     # Check dependency updates
make upgrade-wrapper  # Upgrade Gradle wrapper
make uberjar          # Build fat jar
make uber             # Build and run fat jar (java -jar build/libs/server.jar)
```

JVM toolchain: Java 17. Testing: Kotest with JUnit5 platform.

## Adding a New Challenge

1. Create `python/<group_dir>/challenge_name.py` following the file pattern above
2. Register in `Content.kt` — either add a `challenge()` call or ensure filename matches an existing `includeFilesWithType` glob
3. The return type in `Content.kt` must match what the Python function actually returns
4. Run `make tests` to verify the challenge works end-to-end
