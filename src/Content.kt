import com.github.pambrose.common.util.FileSystemSource
import com.github.pambrose.common.util.GitHubRepo
import com.github.readingbat.dsl.ReturnType.*
import com.github.readingbat.dsl.isProduction
import com.github.readingbat.dsl.readingBatContent

val content =
  readingBatContent {
    repo = if (isProduction()) GitHubRepo("readingbat", "readingbat-python-content") else FileSystemSource("./")
    branchName = "master"

    python {

      group("Boolean Expressions") {
        packageName = "boolean_expressions"
        description = "Basic boolean expressions"

        challenge("less_than") {
          returnType = BooleanType
        }

        challenge("greater_than") {
          returnType = BooleanType
        }

        challenge("less_than_or_equal") {
          returnType = BooleanType
        }

        challenge("greater_than_or_equal") {
          returnType = BooleanType
        }

        challenge("equal") {
          returnType = BooleanType
        }

        challenge("not_equal") {
          returnType = BooleanType
        }

        challenge("modulo1") {
          returnType = IntType
        }

        challenge("modulo2") {
          returnType = BooleanType
        }

        challenge("modulo3") {
          returnType = BooleanType
        }

        challenge("andor1") {
          returnType = BooleanType
        }

        challenge("andor2") {
          returnType = BooleanType
        }

        challenge("andor3") {
          returnType = BooleanType
        }

        challenge("andor4") {
          returnType = BooleanType
        }

        challenge("andor5") {
          returnType = BooleanType
        }

        challenge("andor6") {
          returnType = BooleanType
        }

        challenge("andor7") {
          returnType = BooleanType
        }
      }

      group("String Operations") {
        packageName = "string_operations"
        description = "Basic string operations"

        challenge("goodbye_name") {
          returnType = StringType
        }

        challenge("combine1") {
          returnType = StringType
        }

        challenge("combine2") {
          returnType = StringType
        }

        challenge("concat1") {
          returnType = StringType
        }

        challenge("concat2") {
          returnType = StringType
        }

        challenge("concat3") {
          returnType = StringType
        }

        challenge("strlen1") {
          returnType = IntType
        }

        challenge("strlen2") {
          returnType = IntType
        }

        challenge("strlen3") {
          returnType = IntType
        }

        challenge("in_oper") {
          returnType = BooleanType
        }

        challenge("starts_with") {
          returnType = BooleanType
        }

        challenge("ends_with") {
          returnType = BooleanType
        }

        challenge("slice1") {
          returnType = StringType
        }

        challenge("slice2") {
          returnType = StringType
        }

        challenge("slice3") {
          returnType = StringType
        }

        challenge("slice4") {
          returnType = StringType
        }

        challenge("slice5") {
          returnType = StringType
        }

        challenge("split") {
          returnType = StringType
        }
      }

      group("For Loops") {
        packageName = "for_loops"
        description = "This is a description of For Loops"

        challenge("for_loop1") {
          returnType = IntType
        }

        challenge("for_loop2") {
          returnType = IntType
        }

        challenge("for_loop3") {
          returnType = IntType
        }

        challenge("for_loop4") {
          returnType = IntType
        }

        challenge("for_loop5") {
          returnType = IntType
        }

        challenge("for_loop6") {
          returnType = IntType
        }
      }

      group("Lists") {
        packageName = "lists"
        description = "This is a description of Lists"

        challenge("list3") {
          description = "This is a description of Lists"
          returnType = IntType
        }

        challenge("list4") {
          description = "This is a description of Lists"
          returnType = IntType
        }

        challenge("list5") {
          description = "This is a description of Lists"
          returnType = IntType
        }
      }

      group("Warmup 1") {
        packageName = "warmup1"
        description = "This is a description of Warmup 1"

        challenge("simple_choice1") {
          returnType = BooleanType
        }

        challenge("simple_choice2") {
          codingBatEquiv = "p173401"
          returnType = BooleanType
        }

        challenge("boolean_list") {
          returnType = BooleanListType
        }

        challenge("int_list") {
          returnType = IntListType
        }

        challenge("string_list") {
          returnType = StringListType
        }

        challenge("x_and_y") {
          returnType = IntType
        }

        challenge("simple_choice1") {
          returnType = StringType
        }
      }

      group("If statements") {
        packageName = "if_stmts"
        description = "This is a description of if statements"

        challenge("if_stmt1") {
          returnType = IntType
        }

        challenge("if_stmt2") {
          returnType = IntType
        }

        challenge("if_stmt3") {
          returnType = IntType
        }

        challenge("if_stmt4") {
          returnType = IntType
        }
      }
    }
  }