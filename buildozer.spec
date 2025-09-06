[app]
title = BakeryCalculator
package.name = BakeryCalculator
package.domain = org.roman
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,spec
icon.filename = %(source.dir)s/data/icon.png
version = 1.0
requirements = python3,kivy==2.1.0
android.api = 34
android.minapi = 21
android.build_tools = 34.0.0
android.ndk = 25.1.8937393
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/25.1.8937393

# Java 17 compatibility
android.gradle_source_compatibility = 17
android.gradle_target_compatibility = 17

android.archs = arm64-v8a, armeabi-v7a
fullscreen = 0
description = Простий калькулятор для пекарні
orientation = portrait
android.permissions = INTERNET

# Skip checks
android.skip_update = True
p4a.skip_ant = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
