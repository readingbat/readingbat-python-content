# CLAUDE.md

## Project Overview

ReadingBat Python content repository — Python programming challenges served via a Kotlin-based ReadingBat server. Students solve challenges in the browser; the server evaluates answers by running the Python functions against test cases defined in each file's `main()`.

## Architecture

**Two-language system**: Kotlin defines and serves challenges; Python files *are* the challenges.

### Content DSL (Content.kt)

Challenges are registered two ways:
1. **Individually**: `challenge("name") { returnType = ReturnType.BooleanType }` — explicit per-file
2. **Bulk via glob**: `includeFilesWithType = "pattern*.py" returns ReturnType.Type` — auto-includes matching files

Return types (referenced via the `ReturnType` enum): `BooleanType`, `StringType`, `IntType`, `BooleanListType`, `IntListType`, `StringListType`. `Content.kt` imports `ReturnType` directly rather than wildcard-importing its members, so always qualify (e.g., `ReturnType.IntType`) when adding entries.

**Source switching**: Production reads from GitHub (`GitHubRepo`); development reads from local filesystem (`FileSystemSource`), controlled by `isProduction()`.

### Python Challenge File Pattern

The `main()` prints define the test cases — each `print()` call produces an expected answer that the server checks against student submissions.

## Development Commands

Run `make help` for a self-documenting list of the build, test, lint, run, and packaging targets.

## Line Endings

`.gitattributes` normalizes line endings on commit: LF for `*.py`, `*.sh`, and `gradlew`; CRLF for `*.bat`. Write new challenge files with LF and let Git handle the rest — do not hand-convert.

## Adding a New Challenge

1. Create `python/<group_dir>/challenge_name.py` following the file pattern above
2. Register in `Content.kt` — either add a `challenge()` call or ensure filename matches an existing `includeFilesWithType` glob (qualify return types as `ReturnType.IntType`, etc.)
3. The return type in `Content.kt` must match what the Python function actually returns
4. Run `make lint` to catch style issues, then `make tests` to verify the challenge works end-to-end
