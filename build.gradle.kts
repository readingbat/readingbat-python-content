plugins {
  java
  application
  alias(libs.plugins.kotlin.jvm)
  alias(libs.plugins.versions)
}

// This is for ./gradlew run
application {
  mainClass.set("ContentServer")
}

group = "com.github.pambrose.readingbat"
version = "1.0"

repositories {
  google()
  mavenCentral()
  maven { url = uri("https://jitpack.io") }
}

dependencies {
  implementation(libs.readingbat.core)
  implementation(libs.common.utils.core)
  implementation(libs.kotlin.logging)

  testImplementation(libs.readingbat.core)
  testImplementation(libs.kotest.runner)
  testImplementation(libs.kotest.assertions)
  testImplementation(libs.ktor.server.test)
}

kotlin {
  jvmToolchain(17)
}

tasks.test {
  useJUnitPlatform()

  testLogging {
    events("passed", "skipped", "failed", "standardOut", "standardError")
    exceptionFormat = org.gradle.api.tasks.testing.logging.TestExceptionFormat.FULL
    showStandardStreams = true
  }
}

tasks.withType<Tar> {
  duplicatesStrategy = DuplicatesStrategy.EXCLUDE
}

tasks.withType<Zip> {
  duplicatesStrategy = DuplicatesStrategy.EXCLUDE
}