[app]

# Назва папки
title = BakeryCalculator
package.name = BakeryCalculator
package.domain = org.roman

# Файл з твоїм кодом
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,spec

# Іконка (переконайтесь, що файл data/icon.png існує)
icon.filename = %(source.dir)s/data/icon.png

# Версія
version = 1.0

# Бібліотеки
requirements = python3,kivy==2.1.0

# Min/Target SDK
android.api = 34
android.minapi = 21

# Версії інструментів для збірки
android.build_tools = 34.0.0
android.ndk = 25.1.8937393

# Шляхи до SDK та NDK (ВАЖЛИВО!)
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/25.1.8937393

# Arch підтримка
android.archs = arm64-v8a, armeabi-v7a

# Вимкнути fullscreen якщо не треба
fullscreen = 0

# Опис (необов'язково)
description = Простий калькулятор для пекарні

# Орієнтація
orientation = portrait

# Дозволи
android.permissions = INTERNET

# Додаткові налаштування для уникнення помилок
p4a.branch = develop
android.accept_sdk_license = True

[buildozer]

# Увімкни щоб показувало лог під час збірки
log_level = 2
warn_on_root = 1
