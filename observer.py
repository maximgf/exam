class Observer:
    def __init__(self):
        self.button_clicks = []

    def update(self, button_text):
        self.button_clicks.append(button_text)
        print(f"Кнопка {button_text} нажата")



        
