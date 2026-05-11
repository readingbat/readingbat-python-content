import org.gradle.api.tasks.testing.logging.TestLogEvent

plugins {
  application
  alias(libs.plugins.kotlin.jvm)
  alias(libs.plugins.versions)
  alias(libs.plugins.ktor.plugin)
  alias(libs.plugins.detekt)
  alias(libs.plugins.kotlinter)
}

// This is for ./gradlew run
application {
  mainClass = "ContentServerKt"
}

description = "ReadingBat Site"

dependencies {
  implementation(libs.readingbat.core)
  implementation(libs.core.utils)
  implementation(libs.kotlin.logging)

  testImplementation(libs.bundles.testing)
}

kotlin {
  jvmToolchain(libs.versions.jvm.get().toInt())
}

detekt {
  source.setFrom("src/main/kotlin", "src/test/kotlin")
  buildUponDefaultConfig = true
  parallel = true
}

val cleanTask = "clean"
val buildTask = "build"

tasks.register("stage") {
  dependsOn(cleanTask, buildTask)
}

tasks.named(buildTask) {
  mustRunAfter(cleanTask)
}

tasks.shadowJar {
  archiveFileName.set("server.jar")
  isZip64 = true
  duplicatesStrategy = DuplicatesStrategy.EXCLUDE
  listOf("META-INF/*.SF", "META-INF/*.DSA", "META-INF/*.RSA", "LICENSE*").forEach(::exclude)
}

tasks.test {
  useJUnitPlatform()

  testLogging {
    events = setOf(TestLogEvent.PASSED, TestLogEvent.SKIPPED, TestLogEvent.FAILED)
    exceptionFormat = org.gradle.api.tasks.testing.logging.TestExceptionFormat.FULL
    showStandardStreams = false
  }
}
