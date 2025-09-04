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
android.ndk = 25b

# Arch підтримка
android.archs = arm64-v8a, armeabi-v7a

# Вимкнути fullscreen якщо не треба
fullscreen = 0

# Опис (необов’язково)
description = Простий калькулятор для пекарні

# Орієнтація
orientation = portrait

# android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE

[buildozer]

# Увімкни щоб показувало лог під час збірки
log_level = 2

warn_on_root = 1
