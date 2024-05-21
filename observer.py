class Observer():
    def __init__(self, calculator):
        self.calculator = calculator
        self.calculator.attach(self)

    def update(self, subject):
        if subject is self.calculator:
            self.display_result()

    def display_result(self):
        result = self.calculator.result_var.get()
        print(f"Результат: {result}")

class HistoryLogger(Observer):
    def __init__(self, calculator, filename="history.txt"):
        self.calculator = calculator
        self.calculator.attach(self)
        self.filename = filename
        self.file = None

    def update(self, subject):
        if subject is self.calculator:
            self.log_operation()

    def log_operation(self):
        if not self.file:
            self.file = open(self.filename, "w")
        result = self.calculator.result_var.get()
        self.file.write(f"result: {result}\n")
        self.file.flush()