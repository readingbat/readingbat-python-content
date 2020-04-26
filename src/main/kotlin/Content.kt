import com.github.readingbat.dsl.readingBatContent

val content =
  readingBatContent {

      python {
          repoRoot = "https://github.com/readingbat/readingbat-python-content"

          group("Warmup 1") {
              packageName = "warmup1"
              description = "This is a description of Warmup 1"

              challenge("simple_choice1") {
                  description = "This is a description of **simple_choice1**"

                  true returns false
                  false returns false
              }

              challenge("simple_choice2") {
                  description = "This is a description of **simple_choice2**"
                  codingBatEquiv = "p173401"

                  listOf(true, true) returns true
                  listOf(true, false) returns true
                  listOf(false, true) returns false
                  listOf(false, false) returns true
              }
          }

          group("Warmup 2") {
              packageName = "warmup2"
              description = "This is a description of Warmup 2"
          }

          group("Logic 1") {
              packageName = "logic1"
              description = "This is a description of Logic 1"
          }
          group("Logic 2") {
              packageName = "logic2"
              description = "This is a description of Logic 2"
          }
          group("String 1") {
              packageName = "string1"
              description = "This is a description of String 1"
          }
          group("String 2") {
              packageName = "string2"
              description = "This is a description of String 2"
          }
          group("Array 1") {
              packageName = "array1"
              description = "This is a description of Array 1"
          }
          group("Array 2") {
              packageName = "array2"
              description = "This is a description of Array 2"
          }
      }
  }
