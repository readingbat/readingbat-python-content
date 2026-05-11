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

import com.pambrose.common.util.FileSystemSource
import com.pambrose.common.util.GitHubRepo
import com.pambrose.common.util.OwnerType.Organization
import com.readingbat.dsl.ReturnType
import com.readingbat.dsl.isProduction
import com.readingbat.dsl.readingBatContent

val content =
  readingBatContent {
    repo =
      if (isProduction())
        GitHubRepo(Organization, "readingbat", "readingbat-python-content")
      else
        FileSystemSource("./")

    python {

      group("Warmup 1") {
        packageName = "warmup1"
        description = "Warmup 1 challenges"

        challenge("simple_choice1") { returnType = ReturnType.BooleanType }

        challenge("simple_choice2") {
          codingBatEquiv = "p173401"
          returnType = ReturnType.BooleanType
        }

        challenge("boolean_list") { returnType = ReturnType.BooleanListType }

        challenge("int_list") { returnType = ReturnType.IntListType }

        challenge("string_list") { returnType = ReturnType.StringListType }

        challenge("x_and_y") { returnType = ReturnType.IntType }

        challenge("replace1") { returnType = ReturnType.StringType }

        challenge("replace2") { returnType = ReturnType.StringType }

        challenge("replace3") { returnType = ReturnType.StringType }

        challenge("replace4") { returnType = ReturnType.StringType }

        challenge("count1") { returnType = ReturnType.IntType }

        challenge("front_back") { returnType = ReturnType.StringType }
      }

      group("Math Operations") {
        packageName = "math_ops"
        description = "Arithmetic operators, order of operations, and built-in math functions"
        includeFilesWithType = "math*.py" returns ReturnType.IntType
      }

      group("Boolean Expressions") {
        packageName = "boolean_exprs"
        description = "Basic boolean expressions"

        challenge("less_than") { returnType = ReturnType.BooleanType }
        challenge("greater_than") { returnType = ReturnType.BooleanType }
        challenge("less_than_or_equal") { returnType = ReturnType.BooleanType }
        challenge("greater_than_or_equal") { returnType = ReturnType.BooleanType }
        challenge("equal") { returnType = ReturnType.BooleanType }
        challenge("not_equal") { returnType = ReturnType.BooleanType }
        challenge("modulo1") { returnType = ReturnType.IntType }
        challenge("modulo2") { returnType = ReturnType.BooleanType }
        challenge("modulo3") { returnType = ReturnType.BooleanType }

        includeFilesWithType = "andor*.py" returns ReturnType.BooleanType
      }

      group("Type Conversion") {
        packageName = "type_conv"
        description = "Converting between integers, strings, floats, and booleans"

        challenge("type_conv1") { returnType = ReturnType.IntType }
        challenge("type_conv2") { returnType = ReturnType.StringType }
        challenge("type_conv3") { returnType = ReturnType.StringType }
        challenge("type_conv4") { returnType = ReturnType.IntType }
        challenge("type_conv5") { returnType = ReturnType.BooleanType }
        challenge("type_conv6") { returnType = ReturnType.StringType }
        challenge("type_conv7") { returnType = ReturnType.StringType }
        challenge("type_conv8") { returnType = ReturnType.IntType }
        challenge("type_conv9") { returnType = ReturnType.IntType }
        challenge("type_conv10") { returnType = ReturnType.IntType }
      }

      group("If Statements") {
        packageName = "if_stmts"
        description = "Basic if statements"
        includeFilesWithType = "if_stmt*.py" returns ReturnType.IntType
      }

      group("String Operations") {
        packageName = "string_ops"
        description = "Basic string operations"

        challenge("goodbye_name") { returnType = ReturnType.StringType }
        challenge("combine1") { returnType = ReturnType.StringType }
        challenge("combine2") { returnType = ReturnType.StringType }
        includeFilesWithType = "concat*.py" returns ReturnType.StringType
        includeFilesWithType = "strlen*.py" returns ReturnType.IntType
        challenge("in_oper") { returnType = ReturnType.BooleanType }
        challenge("starts_with") { returnType = ReturnType.BooleanType }
        challenge("ends_with") { returnType = ReturnType.BooleanType }
        includeFilesWithType = "slice*.py" returns ReturnType.StringType
        challenge("split") { returnType = ReturnType.StringType }
      }

      group("String Methods") {
        packageName = "string_methods"
        description = "Built-in string methods like upper(), lower(), replace(), and more"

        challenge("upper1") { returnType = ReturnType.StringType }
        challenge("lower1") { returnType = ReturnType.StringType }
        challenge("strip1") { returnType = ReturnType.StringType }
        challenge("replace_str1") { returnType = ReturnType.StringType }
        challenge("find1") { returnType = ReturnType.IntType }
        challenge("count_str1") { returnType = ReturnType.IntType }
        challenge("title1") { returnType = ReturnType.StringType }
        challenge("capitalize1") { returnType = ReturnType.StringType }
        challenge("join1") { returnType = ReturnType.StringType }
        challenge("isdigit1") { returnType = ReturnType.BooleanType }
        challenge("swapcase1") { returnType = ReturnType.StringType }
        challenge("split1") { returnType = ReturnType.StringListType }
      }

      group("For Loops") {
        packageName = "for_loops"
        description = "Basic for loops"
        includeFilesWithType = "for_loop*.py" returns ReturnType.IntType
      }

      group("While Loops") {
        packageName = "while_loops"
        description = "Loops that repeat while a condition is true"

        challenge("while_loop1") { returnType = ReturnType.IntType }
        challenge("while_loop2") { returnType = ReturnType.IntType }
        challenge("while_loop3") { returnType = ReturnType.IntType }
        challenge("while_loop4") { returnType = ReturnType.IntType }
        challenge("while_loop5") { returnType = ReturnType.IntType }
        challenge("while_loop6") { returnType = ReturnType.IntType }
        challenge("while_loop7") { returnType = ReturnType.StringType }
        challenge("while_loop8") { returnType = ReturnType.StringType }
        challenge("while_loop9") { returnType = ReturnType.IntType }
        challenge("while_loop10") { returnType = ReturnType.StringType }
      }

      group("Lists") {
        packageName = "lists"
        description = "Basic list challenges"
        includeFilesWithType = "list*.py" returns ReturnType.IntType
      }

      group("Nested Loops") {
        packageName = "nested_loops"
        description = "Loops inside loops"

        challenge("nested1") { returnType = ReturnType.IntType }
        challenge("nested2") { returnType = ReturnType.IntType }
        challenge("nested3") { returnType = ReturnType.IntType }
        challenge("nested4") { returnType = ReturnType.IntType }
        challenge("nested5") { returnType = ReturnType.StringType }
        challenge("nested6") { returnType = ReturnType.IntType }
        challenge("nested7") { returnType = ReturnType.IntType }
        challenge("nested8") { returnType = ReturnType.BooleanType }
        challenge("nested9") { returnType = ReturnType.IntType }
      }

      group("Tuples") {
        packageName = "tuples"
        description = "Immutable sequences and tuple operations"

        challenge("tuple1") { returnType = ReturnType.StringType }
        challenge("tuple2") { returnType = ReturnType.IntType }
        challenge("tuple3") { returnType = ReturnType.StringType }
        challenge("tuple4") { returnType = ReturnType.BooleanType }
        challenge("tuple5") { returnType = ReturnType.StringType }
        challenge("tuple6") { returnType = ReturnType.IntType }
        challenge("tuple7") { returnType = ReturnType.IntType }
        challenge("tuple8") { returnType = ReturnType.IntType }
        challenge("tuple9") { returnType = ReturnType.IntType }
      }

      group("Dictionaries") {
        packageName = "dictionaries"
        description = "Key-value data storage with Python dictionaries"

        challenge("dict1") { returnType = ReturnType.IntType }
        challenge("dict2") { returnType = ReturnType.IntType }
        challenge("dict3") { returnType = ReturnType.BooleanType }
        challenge("dict4") { returnType = ReturnType.StringType }
        challenge("dict5") { returnType = ReturnType.IntType }
        challenge("dict6") { returnType = ReturnType.StringListType }
        challenge("dict7") { returnType = ReturnType.IntListType }
        challenge("dict8") { returnType = ReturnType.IntType }
        challenge("dict9") { returnType = ReturnType.IntType }
        challenge("dict10") { returnType = ReturnType.StringType }
      }

      group("List Comprehensions") {
        packageName = "list_comps"
        description = "Building lists with concise one-line expressions"

        challenge("list_comp1") { returnType = ReturnType.StringListType }
        challenge("list_comp2") { returnType = ReturnType.IntListType }
        challenge("list_comp3") { returnType = ReturnType.IntListType }
        challenge("list_comp4") { returnType = ReturnType.StringListType }
        challenge("list_comp5") { returnType = ReturnType.IntListType }
        challenge("list_comp6") { returnType = ReturnType.IntListType }
        challenge("list_comp7") { returnType = ReturnType.IntListType }
        challenge("list_comp8") { returnType = ReturnType.StringListType }
        challenge("list_comp9") { returnType = ReturnType.IntListType }
      }
    }
  }
