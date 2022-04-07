/*
 * Copyright © 2020 Paul Ambrose (pambrose@mac.com)
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

import com.github.readingbat.kotest.TestSupport.answerAllWith
import com.github.readingbat.kotest.TestSupport.answerAllWithCorrectAnswer
import com.github.readingbat.kotest.TestSupport.forEachAnswer
import com.github.readingbat.kotest.TestSupport.forEachChallenge
import com.github.readingbat.kotest.TestSupport.forEachGroup
import com.github.readingbat.kotest.TestSupport.forEachLanguage
import com.github.readingbat.kotest.TestSupport.shouldHaveAnswer
import com.github.readingbat.kotest.TestSupport.testModule
import com.github.readingbat.posts.AnswerStatus.*
import io.kotest.core.spec.style.StringSpec
import io.kotest.matchers.shouldBe
import io.kotest.matchers.string.shouldBeBlank
import io.ktor.server.testing.*

class ContentTests : StringSpec({

  "Test all challenges" {
    withTestApplication({ testModule(content) }) {
      content.forEachLanguage {
        forEachGroup {
          forEachChallenge {
            answerAllWith(this@withTestApplication, "") {
              answerStatus shouldBe NOT_ANSWERED
              hint.shouldBeBlank()
            }

            answerAllWith(this@withTestApplication, "wrong answer") {
              answerStatus shouldBe INCORRECT
            }

            answerAllWithCorrectAnswer(this@withTestApplication) {
              answerStatus shouldBe CORRECT
              hint.shouldBeBlank()
            }
          }
        }
      }
    }
  }

  "Test with correct answers" {
    withTestApplication({ testModule(content) }) {
      content.forEachLanguage {
        forEachGroup {
          forEachChallenge {
            forEachAnswer {
              it shouldHaveAnswer correctAnswers[it.index]
            }
          }
        }
      }
    }
  }

  "Test individual challenges" {
    withTestApplication({ testModule(content) }) {
      /*
      content.pythonChallenge("Group 1", "find_it") {
        answerFor(0) shouldNotHaveAnswer "true"
        answerFor(1) shouldNotHaveAnswer "false"

        answerFor(0) shouldHaveAnswer "False"
        answerFor(1) shouldHaveAnswer "True"
        answerFor(2) shouldHaveAnswer "False"
        answerFor(3) shouldHaveAnswer "True"
        answerFor(4) shouldHaveAnswer "False"
      }
      */
    }
  }
})