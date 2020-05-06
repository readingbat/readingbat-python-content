import com.github.readingbat.dsl.ReturnType.*
import com.github.readingbat.dsl.readingBatContent

val content =
  readingBatContent {

    python {
      repoRoot = "https://github.com/readingbat/readingbat-python-content"
      branchName = "master"

      group("Numeric Expressions") {
        packageName = "numeric_expressions"
        description = "Basic numeric expressions"

        challenge("lt-expr") {
          description = """Determine if one value is less than another with the "<" operator."""
          returnType = BooleanType
        }

        challenge("gt-expr") {
          description = """Determine if one value is greater than another with the ">" operator."""
          returnType = BooleanType
        }

        challenge("lteq-expr") {
          description =
            """Determine if one value is greater than or equal to another with the "<=" operator. *Notice the "=" comes after the "<".*"""
          returnType = BooleanType
        }

        challenge("gteq-expr") {
          description =
            """Determine if one value is greater than or equal to another with the ">=" operator. *Notice the "=" comes after the ">".*"""
          returnType = BooleanType
        }

        challenge("eq-expr") {
          description = """Determine if two value are equal with the "=="**" operator. *Notice the 2 "=" characters.*"""
          returnType = BooleanType
        }

        challenge("neq-expr") {
          description = """Determine if two value are not equal with the "!=" operator."""
          returnType = BooleanType
        }

      }

      group("String Operations") {
        packageName = "string_operations"
        description = "Basic string operations"

        challenge("len1") {
          description = """**len()** returns the length of a string."""
          returnType = IntType
        }

        challenge("len2") {
          description = """**len()** returns the length of a string."""
          returnType = IntType
        }

        challenge("len3") {
          description = """**len()** returns the length of a string."""
          returnType = IntType
        }

        challenge("slice1") {
          description = """Remember the first character in a string is at index 0."""
          returnType = StringType
        }

        challenge("slice2") {
          description = """Remember the last character in a string is at index -1."""
          returnType = StringType
        }

        challenge("slice3") {
          description = """Remember the first character in a string is at index 0."""
          returnType = StringType
        }

        challenge("slice4") {
          description = """Remember a slice is inclusive of the starting index and exclusive of the ending index."""
          returnType = StringType
        }

        challenge("slice5") {
          description = """Remember a slice is inclusive of the starting index and exclusive of the ending index."""
          returnType = StringType
        }


      }


      group("Warmup 1") {
        packageName = "warmup1"
        description = "This is a description of Warmup 1"

        challenge("simple_choice1") {
          description = "This is a description of **simple_choice1**"
          returnType = BooleanType
        }

        challenge("simple_choice2") {
          description = "This is a description of **simple_choice2**"
          codingBatEquiv = "p173401"
          returnType = BooleanType
        }

        challenge("boolean_list") {
          description = "This is a description of **boolean_list**"
          returnType = BooleanListType
        }

        challenge("int_list") {
          description = "This is a description of **int_list**"
          returnType = IntListType
        }

        challenge("string_list") {
          description = "This is a description of **string_list**"
          returnType = StringListType
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
    }
  }
