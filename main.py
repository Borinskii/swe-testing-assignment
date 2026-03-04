import tkinter as tk
from calculator import Calculator


class QuickCalcApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quick-Calc")
        self.root.resizable(False, False)
        self.calc = Calculator()
        self.first_operand = None
        self.operator = None
        self.reset_next = False
        self._build_ui()

    def _build_ui(self):
        self.display_var = tk.StringVar(value="0")
        tk.Entry(
            self.root,
            textvariable=self.display_var,
            font=("Arial", 24),
            justify="right",
            state="readonly",
            readonlybackground="white",
        ).grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        # (label, row, col, colspan, color)
        buttons = [
            ("C", 1, 0, 1, "#e74c3c"),
            ("",  1, 1, 1, None),
            ("",  1, 2, 1, None),
            ("/", 1, 3, 1, "#f0a500"),
            ("7", 2, 0, 1, "white"),
            ("8", 2, 1, 1, "white"),
            ("9", 2, 2, 1, "white"),
            ("*", 2, 3, 1, "#f0a500"),
            ("4", 3, 0, 1, "white"),
            ("5", 3, 1, 1, "white"),
            ("6", 3, 2, 1, "white"),
            ("-", 3, 3, 1, "#f0a500"),
            ("1", 4, 0, 1, "white"),
            ("2", 4, 1, 1, "white"),
            ("3", 4, 2, 1, "white"),
            ("+", 4, 3, 1, "#f0a500"),
            ("0", 5, 0, 2, "white"),
            (".", 5, 2, 1, "white"),
            ("=", 5, 3, 1, "#27ae60"),
        ]

        for (text, row, col, colspan, color) in buttons:
            if not text:
                continue
            tk.Button(
                self.root,
                text=text,
                font=("Arial", 16),
                bg=color,
                relief="groove",
                command=lambda t=text: self._on_button(t),
            ).grid(row=row, column=col, columnspan=colspan,
                   sticky="nsew", padx=2, pady=2, ipady=10)

        for i in range(6):
            self.root.rowconfigure(i, weight=1)
        for i in range(4):
            self.root.columnconfigure(i, weight=1)

    def _on_button(self, text):
        if text == "C":
            self._do_clear()
        elif text == "=":
            self._do_equals()
        elif text in ("+", "-", "*", "/"):
            self._do_operator(text)
        else:
            self._do_digit(text)

    def _do_digit(self, digit):
        if self.reset_next:
            self.display_var.set("")
            self.reset_next = False
        current = self.display_var.get()
        if current == "0" and digit != ".":
            current = ""
        self.display_var.set(current + digit)

    def _do_operator(self, op):
        self.first_operand = float(self.display_var.get())
        self.operator = op
        self.reset_next = True

    def _do_equals(self):
        if self.operator is None or self.first_operand is None:
            return
        try:
            second = float(self.display_var.get())
            if self.operator == "+":
                result = self.calc.add(self.first_operand, second)
            elif self.operator == "-":
                result = self.calc.subtract(self.first_operand, second)
            elif self.operator == "*":
                result = self.calc.multiply(self.first_operand, second)
            elif self.operator == "/":
                result = self.calc.divide(self.first_operand, second)

            self.display_var.set(int(result) if result == int(result) else result)
            self.calc.result = result
            self.operator = None
            self.first_operand = None
            self.reset_next = True
        except ValueError:
            self.display_var.set("Error")
            self.reset_next = True

    def _do_clear(self):
        self.calc.clear()
        self.display_var.set("0")
        self.first_operand = None
        self.operator = None
        self.reset_next = False


def main():
    root = tk.Tk()
    QuickCalcApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()