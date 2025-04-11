from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.graphics import Color, RoundedRectangle
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.model import app

class RoundedBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(0.95, 0.95, 0.95, 1)
            self.rect = RoundedRectangle(radius=[0], size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos


class SavingsCalculator(RoundedBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kwargs)

        amount_layout = BoxLayout(orientation='horizontal', spacing=10, padding=10)
        amount_label = Label(text="Cantidad mensual:", color=(0.27, 0.24, 0.56, 1))  # Color #453D8F
        self.amount_input = TextInput(hint_text="Ingrese la cantidad de ahorro mensual", multiline=False, background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1), padding=[10, 10])
        amount_layout.add_widget(amount_label)
        amount_layout.add_widget(self.amount_input)
        self.add_widget(amount_layout)

        months_layout = BoxLayout(orientation='horizontal', spacing=10, padding=10)
        months_label = Label(text="Cantidad de meses:", color=(0.37, 0.24, 0.56, 1))  # Color #5F3D8F
        self.months_input = TextInput(hint_text="Ingrese la cantidad de meses", multiline=False, background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1), padding=[10, 10])
        months_layout.add_widget(months_label)
        months_layout.add_widget(self.months_input)
        self.add_widget(months_layout)

        interest_layout = BoxLayout(orientation='horizontal', spacing=10, padding=10)
        interest_label = Label(text="Tasa de interés:", color=(0.56, 0.24, 0.52, 1))  # Color #8F3D84
        self.interest_input = TextInput(hint_text="Ingrese la tasa de interes", multiline=False, background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1), padding=[10, 10])
        interest_layout.add_widget(interest_label)
        interest_layout.add_widget(self.interest_input)
        self.add_widget(interest_layout)

        self.calculate_button = Button(
            text="Calcular Ahorro",
            background_color=(0.27, 0.24, 0.56, 1),
            color=(1, 1, 1, 1),
            size_hint=(1, None),
            height=50,
            background_normal='',
        )
        with self.calculate_button.canvas.before:
            Color(0.27, 0.24, 0.56, 1)
            self.calculate_button_rect = RoundedRectangle(
            radius=[14],
            size=self.calculate_button.size,
            pos=self.calculate_button.pos
            )
        self.calculate_button.bind(
            size=lambda instance, value: setattr(self.calculate_button_rect, 'size', value),
            pos=lambda instance, value: setattr(self.calculate_button_rect, 'pos', value)
        )
        self.calculate_button.bind(on_press=self.calculate)
        self.add_widget(self.calculate_button)

        self.result_label = Label(text="Resultado aparecerá aquí", color=(0.12, 0.12, 0.12, 1))  # Color #1E1E1E
        self.add_widget(self.result_label)

    def show_error_popup(self, message):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text=message, color=(1, 0, 0, 1)))  # Red color for error
        close_button = Button(text="Cerrar", background_color=(0.27, 0.24, 0.56, 1), color=(1, 1, 1, 1))
        content.add_widget(close_button)

        popup = Popup(title="Error", content=content, size_hint=(0.8, 0.4))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

    def calculate(self, instance):
        MinimunValue = 0
        PercentageConvertor = 100
        MaximunValue = 64
        try:
            amount = float(self.amount_input.text)
            if amount <= MinimunValue:
                raise ValueError("La cantidad de ahorro debe ser mayor a 0.")

            months = int(self.months_input.text)
            if months <= MinimunValue:
                raise app.Invalidmonths("La cantidad de meses debe ser mayor a 0.")

            interest = float(self.interest_input.text) / PercentageConvertor
            if interest < MinimunValue or interest > MaximunValue:
                raise app.Invalidinterest("La tasa de interés debe estar entre 0 y 100.")

            result = app.Calculate_programmed_savings(amount, interest, months)
            self.result_label.text = f"Ahorro Total: {result:.2f}"
        except (ValueError, app.Invalidinterest, app.Invalidmonths) as e:
            self.show_error_popup(str(e))


class SavingsApp(App):
    def build(self):
        return SavingsCalculator()


if __name__ == "__main__":
    SavingsApp().run()