import com.github.readingbat.dsl.ReturnType.*
import com.github.readingbat.dsl.readingBatContent

val content =
  readingBatContent {

    python {
      repoRoot = "https://github.com/readingbat/readingbat-python-content"
      branchName = "dev"

      group("Expressions") {
        packageName = "expressions"
        description = "Collection of expressions"

        challenge("ltexpr") {
          description = """Determine if one value is less than another with the **<** operator."""
          returnType = BooleanType
        }

        challenge("gtexpr") {
          description = """Determine if one value is greater than another with the **>** operator."""
          returnType = BooleanType
        }

        challenge("lteqexpr") {
          description =
            """Determine if one value is greater than or equal to another with the **<=** operator. Notice the "=" comes after the ">"."""
          returnType = BooleanType
        }

        challenge("gteqexpr") {
          description =
            """Determine if one value is greater than or equal to another with the **>=** operator. *Notice the "=" comes after the ">".*"""
          returnType = BooleanType
        }

        challenge("eqexpr") {
          description = """Determine if two value are equal with the **==** operator. *Notice the 2 "=" characters.*"""
          returnType = BooleanType
        }

        challenge("neqexpr") {
          description = """Determine if two value are not equal with the **!=** operator."""
          returnType = BooleanType
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
