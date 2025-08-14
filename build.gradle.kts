plugins {
  java
  application
  kotlin("jvm") version "2.1.0"
  id("com.github.ben-manes.versions") version "0.52.0"
}

// This is for ./gradlew run
application {
  mainClass.set("ContentServer")
}

group = "com.github.pambrose.readingbat"
version = "1.0-SNAPSHOT"

repositories {
  google()
  mavenCentral()
  maven { url = uri("https://jitpack.io") }
}

dependencies {
  implementation("com.github.readingbat:readingbat-core:${property("readingbat_version")}")
  implementation("com.github.pambrose.common-utils:core-utils:${property("utils_version")}")
  implementation("io.github.oshai:kotlin-logging-jvm:${property("logging_version")}")

  testImplementation("com.github.readingbat:readingbat-core:${property("readingbat_version")}")
  testImplementation("io.kotest:kotest-runner-junit5:5.8.0")
  testImplementation("io.kotest:kotest-assertions-core:5.8.0")
  testImplementation("io.ktor:ktor-server-test-host:2.3.7")
}

sourceSets {
  main {
    kotlin.srcDirs("src")
    java.srcDirs("src")
    resources.srcDirs("resources")
  }
  test {
    kotlin.srcDirs("test")
    java.srcDirs("test")
    resources.srcDirs("testresources")
  }
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