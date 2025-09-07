[app]
title = BakeryCalculator
package.name = bakerycalculator
package.domain = org.roman
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.1.0
p4a.branch = master

# Android settings
android.api = 34
android.minapi = 21
android.archs = arm64-v8a,armeabi-v7a

# App configuration
orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# Build configuration
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
