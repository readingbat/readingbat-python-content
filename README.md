# ReadingBat Python Content

Python programming challenges served by the [ReadingBat](https://github.com/readingbat) platform. Students solve challenges in the browser; the server evaluates answers by running Python functions against test cases defined in each file.

## Prerequisites

- Java 17+

## Setup

```bash
make compile    # Build without tests
make tests      # Run all tests
make run        # Start the server on port 8080
```

## Adding a Challenge

1. Create a Python file in `python/<group_dir>/` following this pattern:

```python
# @desc Description of the challenge

def challenge_name(param1, param2):
    return result

def main():
    print(challenge_name(arg1, arg2))  # each print = one test case

if __name__ == '__main__':
    main()
```

2. Register the challenge in `src/main/kotlin/Content.kt` — either add a `challenge()` call or ensure the filename matches an existing `includeFilesWithType` glob.

3. Run `make tests` to verify.
