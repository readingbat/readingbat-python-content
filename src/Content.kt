import com.github.pambrose.common.util.FileSystemSource
import com.github.pambrose.common.util.GitHubRepo
import com.github.readingbat.dsl.ReturnType.*
import com.github.readingbat.dsl.readingBatContent

val content =
  readingBatContent {

    python {
      repo = GitHubRepo("readingbat", "readingbat-python-content")
      //repo = FileSystemSource("./")
      branchName = "master"

      group("Boolean Expressions") {
        packageName = "boolean_expressions"
        description = "Basic boolean expressions"

        challenge("less_than") {
          description = "Determine if one value is less than another with the **<** operator."
          returnType = BooleanType
        }

        challenge("greater_than") {
          description = "Determine if one value is greater than another with the **>** operator."
          returnType = BooleanType
        }

        challenge("less_than_or_equal") {
          description =
            """Determine if one value is greater than or equal to another with the **<=** operator. *Notice the "=" comes after the "<".*"""
          returnType = BooleanType
        }

        challenge("greater_than_or_equal") {
          description =
            """Determine if one value is greater than or equal to another with the **>=** operator. *Notice the "=" comes after the ">".*"""
          returnType = BooleanType
        }

        challenge("equal") {
          description = """Determine if two value are equal with the **==** operator. *Notice the 2 "=" characters.*"""
          returnType = BooleanType
        }

        challenge("not_equal") {
          description = "Determine if two value are not equal with the **!=** operator."
          returnType = BooleanType
        }

        challenge("modulo1") {
          description =
            """
            The **%** operator returns the remainder after dividing two numbers. 
            See more details [here](https://blog.mattclemente.com/2019/07/12/modulus-operator-modulo-operation.html).
            """.trimIndent()
          returnType = IntType
        }

        challenge("modulo2") {
          description = """**%2** is an easy way of testing if a number is odd or even"""
          returnType = BooleanType
        }

        challenge("modulo3") {
          description = "**%2** is an easy way of testing if a number is odd or even"
          returnType = BooleanType
        }

        challenge("andor1") {
          description = ""
          returnType = BooleanType
        }

        challenge("andor2") {
          description = ""
          returnType = BooleanType
        }

        challenge("andor3") {
          description = "The **not** operator flips a boolean value"
          returnType = BooleanType
        }

        challenge("andor4") {
          description = "The **not** operator flips a boolean value"
          returnType = BooleanType
        }

        challenge("andor5") {
          description = "Which order are the **and** and the **or** evaluated?"
          returnType = BooleanType
        }

        challenge("andor6") {
          description = "Parentheses override the order of evaluation"
          returnType = BooleanType
        }

        challenge("andor7") {
          description = "Which order are the **and** and the **or** evaluated?"
          returnType = BooleanType
        }
      }

      group("String Operations") {
        packageName = "string_operations"
        description = "Basic string operations"

        challenge("concat1") {
          description = "Merge two strings."
          returnType = IntType
        }

        challenge("concat2") {
          description = "Merge three strings."
          returnType = IntType
        }

        challenge("concat3") {
          description = "Print a string a certain number of times."
          returnType = IntType
        }

        challenge("strlen1") {
          description = "**len()** returns the length of a string."
          returnType = IntType
        }

        challenge("strlen2") {
          description = "**len()** returns the length of a string."
          returnType = IntType
        }

        challenge("strlen3") {
          description = "**len()** returns the length of a string."
          returnType = IntType
        }

        challenge("slice1") {
          description = "Remember the first character in a string is at index 0."
          returnType = StringType
        }

        challenge("slice2") {
          description = "Remember the last character in a string is at index -1."
          returnType = StringType
        }

        challenge("slice3") {
          description = "Remember the first character in a string is at index 0."
          returnType = StringType
        }

        challenge("slice4") {
          description = "Remember a slice is inclusive of the starting index and exclusive of the ending index."
          returnType = StringType
        }

        challenge("slice5") {
          description = "Remember a slice is inclusive of the starting index and exclusive of the ending index."
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
    }
  }
