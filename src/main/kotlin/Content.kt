/*
 * Copyright © 2025 Paul Ambrose (pambrose@mac.com)
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *       http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 */

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

        challenge("less_than") { returnType = BooleanType }
        challenge("greater_than") { returnType = BooleanType }
        challenge("less_than_or_equal") { returnType = BooleanType }
        challenge("greater_than_or_equal") { returnType = BooleanType }
        challenge("equal") { returnType = BooleanType }
        challenge("not_equal") { returnType = BooleanType }
        challenge("modulo1") { returnType = IntType }
        challenge("modulo2") { returnType = BooleanType }
        challenge("modulo3") { returnType = BooleanType }

        includeFilesWithType = "andor*.py" returns BooleanType
      }

      group("String Operations") {
        packageName = "string_ops"
        description = "Basic string operations"

        challenge("goodbye_name") { returnType = StringType }
        challenge("combine1") { returnType = StringType }
        challenge("combine2") { returnType = StringType }
        includeFilesWithType = "concat*.py" returns StringType
        includeFilesWithType = "strlen*.py" returns IntType
        challenge("in_oper") { returnType = BooleanType }
        challenge("starts_with") { returnType = BooleanType }
        challenge("ends_with") { returnType = BooleanType }
        includeFilesWithType = "slice*.py" returns StringType
        challenge("split") { returnType = StringType }
      }

      group("If Statements") {
        packageName = "if_stmts"
        description = "Basic if statements"
        includeFilesWithType = "if_stmt*.py" returns IntType
      }

      group("For Loops") {
        packageName = "for_loops"
        description = "Basic for loops"
        includeFilesWithType = "for_loop*.py" returns IntType
      }

      group("Lists") {
        packageName = "lists"
        description = "Basic list challenges"
        includeFilesWithType = "list*.py" returns IntType
      }

      group("Warmup 1") {
        packageName = "warmup1"
        description = "Warmup 1 challenges"

        challenge("simple_choice1") { returnType = BooleanType }

        challenge("simple_choice2") {
          codingBatEquiv = "p173401"
          returnType = BooleanType
        }

        challenge("boolean_list") { returnType = BooleanListType }

        challenge("int_list") { returnType = IntListType }

        challenge("string_list") { returnType = StringListType }

        challenge("x_and_y") { returnType = IntType }

        challenge("replace1") { returnType = StringType }

        challenge("replace2") { returnType = StringType }

        challenge("replace3") { returnType = StringType }

        challenge("replace4") { returnType = StringType }

        challenge("count1") { returnType = IntType }
      }
    }
  }