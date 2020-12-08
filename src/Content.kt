import com.github.pambrose.common.util.FileSystemSource
import com.github.pambrose.common.util.GitHubRepo
import com.github.pambrose.common.util.OwnerType.Organization
import com.github.readingbat.dsl.ReturnType.*
import com.github.readingbat.dsl.isProduction
import com.github.readingbat.dsl.readingBatContent

val content =
  readingBatContent {
    repo =
      if (isProduction())
        GitHubRepo(Organization, "readingbat", "readingbat-python-content")
      else
        FileSystemSource("./")

    python {

      group("Boolean Expressions") {
        packageName = "boolean_exprs"
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

        includeFilesWithType = "andor*.py" returns BooleanType
      }

      group("String Operations") {
        packageName = "string_ops"
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

      group("If Statements") {
        packageName = "if_stmts"
        description = "Basic if statements"

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

      group("For Loops") {
        packageName = "for_loops"
        description = "Basic for loops"

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
        description = "Basic list challenges"

        includeFilesWithType = "list*.py" returns IntType
      }

      group("Warmup 1") {
        packageName = "warmup1"
        description = "Warmup 1 challenges"

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

        challenge("replace1") {
          returnType = StringType
        }

        challenge("replace2") {
          returnType = StringType
        }

        challenge("replace3") {
          returnType = StringType
        }

        challenge("replace4") {
          returnType = StringType
        }

        challenge("count1") {
          returnType = IntType
        }
      }
    }
  }