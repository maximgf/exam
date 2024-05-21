import tkinter as tk
from observer import Observer


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Калькулятор на Tkinter")
        self.geometry("400x400")
        self.result_var = tk.StringVar()
        self._create_widgets()
        # Создание наблюдателя
        self.observer = Observer()

    def _create_widgets(self):
        entry = tk.Entry(self, textvariable=self.result_var, font=('Helvetica', 24), justify='right')
        entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        entry.focus_set()
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '+', '=', 'Clear'
        ]
        row_val = 1
        col_val = 0
        for button_text in buttons:
            tk.Button(self, text=button_text, command=lambda text=button_text: self._on_button_click(text)).grid(row=row_val, column=col_val, sticky='news', padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def _on_button_click(self, text):
        current_result = self.result_var.get()
        if text == 'Clear':
            self.result_var.set('')
        elif text == '=':
            try:
                result = str(eval(current_result))
                self.result_var.set(result)
            except:
                self.result_var.set("Ошибка")
        else:
            self.result_var.set(current_result + text)
            # Уведомление наблюдателя о нажатии кнопки
        
        self.observer.update(text)

app = Calculator()
app.mainloop()