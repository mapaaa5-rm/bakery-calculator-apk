# -*- coding: utf-8 -*-
import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.utils import platform

# Щоб уникнути розтягування екрана при появі клавіатури
if platform == 'android':
    Window.softinput_mode = 'below_target'

class BakeryCalculator(App):
    def build(self):
        # --- ГОЛОВНИЙ МАКЕТ ---
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Створюємо область, що прокручується
        scroll_view = ScrollView()
        self.input_layout = GridLayout(cols=2, spacing=10, size_hint_y=None)
        self.input_layout.bind(minimum_height=self.input_layout.setter('height'))

        # --- ПОЛЯ ДЛЯ ВВЕДЕННЯ ДАНИХ ---
        self.inputs = {}
        labels_and_ids = {
            "1. (Звич.) Вага 4.250 кг:": "pieces_1",
            "2. (Звич.) Вага 2.330 кг:": "pieces_2",
            "3. (Звич.) Вага 3.250 кг:": "pieces_3",
            "4. (Цільн.) Вага 2.330 кг:": "pieces_4_ww",
            "5. (Цільн.) Вага 4.250 кг:": "pieces_5_ww",
        }

        for label_text, id_text in labels_and_ids.items():
            self.input_layout.add_widget(Label(text=label_text, halign='right'))
            text_input = TextInput(multiline=False, input_type='number', hint_text='0')
            self.inputs[id_text] = text_input
            self.input_layout.add_widget(text_input)

        scroll_view.add_widget(self.input_layout)
        self.main_layout.add_widget(scroll_view)

        # --- КНОПКА РОЗРАХУНКУ ---
        calc_button = Button(text="Розрахувати", size_hint_y=0.15, bold=True)
        calc_button.bind(on_press=self.calculate)
        self.main_layout.add_widget(calc_button)
        
        # --- МІТКА ДЛЯ ВИВЕДЕННЯ РЕЗУЛЬТАТІВ ---
        self.result_label = Label(text="Результати з'являться тут", size_hint_y=0.4)
        self.main_layout.add_widget(self.result_label)

        return self.main_layout

    def calculate(self, instance):
        try:
            # --- ОТРИМУЄМО ДАНІ З ПОЛІВ ВВОДУ ---
            p = {key: int(val.text or 0) for key, val in self.inputs.items()}

            # --- НАЛАШТУВАННЯ ---
            weight_A = 4.250
            weight_B = 2.330
            weight_C = 3.250
            flour_coeff = 1.59
            
            # --- РОЗРАХУНКИ ---
            normal_dough = (p['pieces_1'] * weight_A) + (p['pieces_2'] * weight_B) + (p['pieces_3'] * weight_C)
            normal_flour = normal_dough / flour_coeff
            
            ww_dough = (p['pieces_4_ww'] * weight_B) + (p['pieces_5_ww'] * weight_A)
            total_flour_for_ww = ww_dough / flour_coeff
            
            ww_part = total_flour_for_ww / 4
            normal_part_for_blend = ww_part * 3
            
            final_normal_flour = normal_flour + normal_part_for_blend
            final_ww_flour = ww_part
            
            # --- ФОРМУЄМО ТЕКСТ РЕЗУЛЬТАТУ ---
            result_text = (
                f"[b]--- Звичайне тісто ---[/b]\n"
                f"Загальна вага тіста: {normal_dough:.2f} кг\n"
                f"Потрібно звичайної муки: {normal_flour:.2f} кг\n\n"
                
                f"[b]--- Цільнозернове тісто ---[/b]\n"
                f"Загальна вага тіста: {ww_dough:.2f} кг\n"
                f"Всього муки для нього: {total_flour_for_ww:.2f} кг\n"
                f"   [i]Звичайної муки (3 частини):[/i] {normal_part_for_blend:.2f} кг\n"
                f"   [i]Цільнозернової (1 частина):[/i] {ww_part:.2f} кг\n\n"
                
                f"[b]--- ЗАГАЛЬНА КІЛЬКІСТЬ МУКИ ---[/b]\n"
                f"Всього звичайної муки: {final_normal_flour:.2f} кг\n"
                f"Всього цільнозернової: {final_ww_flour:.2f} кг"
            )
            # Вмикаємо розмітку для жирного тексту та курсиву
            self.result_label.markup = True
            self.result_label.text = result_text

        except ValueError:
            self.result_label.text = "ПОМИЛКА: Будь ласка, введіть тільки числа."
        except Exception as e:
            self.result_label.text = f"Сталася помилка: {e}"

if __name__ == '__main__':
    BakeryCalculator().run()
