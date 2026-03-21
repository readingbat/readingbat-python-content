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

        challenge("front_back") { returnType = StringType }
      }

      group("Math Operations") {
        packageName = "math_ops"
        description = "Arithmetic operators, order of operations, and built-in math functions"
        includeFilesWithType = "math*.py" returns IntType
      }

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

      group("Type Conversion") {
        packageName = "type_conv"
        description = "Converting between integers, strings, floats, and booleans"

        challenge("type_conv1") { returnType = IntType }
        challenge("type_conv2") { returnType = StringType }
        challenge("type_conv3") { returnType = StringType }
        challenge("type_conv4") { returnType = IntType }
        challenge("type_conv5") { returnType = BooleanType }
        challenge("type_conv6") { returnType = StringType }
        challenge("type_conv7") { returnType = StringType }
        challenge("type_conv8") { returnType = IntType }
        challenge("type_conv9") { returnType = IntType }
        challenge("type_conv10") { returnType = IntType }
      }

      group("If Statements") {
        packageName = "if_stmts"
        description = "Basic if statements"
        includeFilesWithType = "if_stmt*.py" returns IntType
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

      group("String Methods") {
        packageName = "string_methods"
        description = "Built-in string methods like upper(), lower(), replace(), and more"

        challenge("upper1") { returnType = StringType }
        challenge("lower1") { returnType = StringType }
        challenge("strip1") { returnType = StringType }
        challenge("replace_str1") { returnType = StringType }
        challenge("find1") { returnType = IntType }
        challenge("count_str1") { returnType = IntType }
        challenge("title1") { returnType = StringType }
        challenge("capitalize1") { returnType = StringType }
        challenge("join1") { returnType = StringType }
        challenge("isdigit1") { returnType = BooleanType }
        challenge("swapcase1") { returnType = StringType }
        challenge("split1") { returnType = StringListType }
      }

      group("For Loops") {
        packageName = "for_loops"
        description = "Basic for loops"
        includeFilesWithType = "for_loop*.py" returns IntType
      }

      group("While Loops") {
        packageName = "while_loops"
        description = "Loops that repeat while a condition is true"

        challenge("while_loop1") { returnType = IntType }
        challenge("while_loop2") { returnType = IntType }
        challenge("while_loop3") { returnType = IntType }
        challenge("while_loop4") { returnType = IntType }
        challenge("while_loop5") { returnType = IntType }
        challenge("while_loop6") { returnType = IntType }
        challenge("while_loop7") { returnType = StringType }
        challenge("while_loop8") { returnType = StringType }
        challenge("while_loop9") { returnType = IntType }
        challenge("while_loop10") { returnType = StringType }
      }

      group("Lists") {
        packageName = "lists"
        description = "Basic list challenges"
        includeFilesWithType = "list*.py" returns IntType
      }

      group("Nested Loops") {
        packageName = "nested_loops"
        description = "Loops inside loops"

        challenge("nested1") { returnType = IntType }
        challenge("nested2") { returnType = IntType }
        challenge("nested3") { returnType = IntType }
        challenge("nested4") { returnType = IntType }
        challenge("nested5") { returnType = StringType }
        challenge("nested6") { returnType = IntType }
        challenge("nested7") { returnType = IntType }
        challenge("nested8") { returnType = BooleanType }
        challenge("nested9") { returnType = IntType }
      }

      group("Tuples") {
        packageName = "tuples"
        description = "Immutable sequences and tuple operations"

        challenge("tuple1") { returnType = StringType }
        challenge("tuple2") { returnType = IntType }
        challenge("tuple3") { returnType = StringType }
        challenge("tuple4") { returnType = BooleanType }
        challenge("tuple5") { returnType = StringType }
        challenge("tuple6") { returnType = IntType }
        challenge("tuple7") { returnType = IntType }
        challenge("tuple8") { returnType = IntType }
        challenge("tuple9") { returnType = IntType }
      }

      group("Dictionaries") {
        packageName = "dictionaries"
        description = "Key-value data storage with Python dictionaries"

        challenge("dict1") { returnType = IntType }
        challenge("dict2") { returnType = IntType }
        challenge("dict3") { returnType = BooleanType }
        challenge("dict4") { returnType = StringType }
        challenge("dict5") { returnType = IntType }
        challenge("dict6") { returnType = StringListType }
        challenge("dict7") { returnType = IntListType }
        challenge("dict8") { returnType = IntType }
        challenge("dict9") { returnType = IntType }
        challenge("dict10") { returnType = StringType }
      }

      group("List Comprehensions") {
        packageName = "list_comps"
        description = "Building lists with concise one-line expressions"

        challenge("list_comp1") { returnType = StringListType }
        challenge("list_comp2") { returnType = IntListType }
        challenge("list_comp3") { returnType = IntListType }
        challenge("list_comp4") { returnType = StringListType }
        challenge("list_comp5") { returnType = IntListType }
        challenge("list_comp6") { returnType = IntListType }
        challenge("list_comp7") { returnType = IntListType }
        challenge("list_comp8") { returnType = StringListType }
        challenge("list_comp9") { returnType = IntListType }
      }
    }
  }