[app]

# Назва апки
title = BakeryCalculator
package.name = BakeryCalculator
package.domain = org.roman

# Файл з твоїм кодом
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Основний файл програми
main.py = main.py

# Іконка (можна замінити на свою)
icon.filename = %(source.dir)s/data/icon.png

# Версія
version = 1.0

# Бібліотеки
requirements = python3,kivy

# Min/Target SDK
android.api = 34
android.minapi = 21

# Arch підтримка
android.archs = arm64-v8a, armeabi-v7a

# Вимкнути fullscreen якщо не треба
fullscreen = 0

# Опис (необов’язково)
description = Простий калькулятор для пекарні

# Орієнтація
orientation = portrait

# Якщо треба доступ до файлів/інтернету, можна додати:
# android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE

[buildozer]

# Увімкни щоб показувало лог під час збірки
log_level = 2

warn_on_root = 1