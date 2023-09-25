from tkinter import Tk, Frame, Entry, Button, StringVar


class SimpleCalculator:
    """Clase que implementa una calculadora básica con una interfaz gráfica de usuario."""

    def __init__(self, master):
        """
        Inicializa la calculadora.
        
        Args:
        - master (Tk): La ventana principal de la aplicación.
        """
        self.master = master
        self.master.title("Calculadora Básica")
        self.master.geometry('400x250')
        self.current_input = ""
        self.operation = ""
        self.previous_input = ""
        self.display = StringVar()
        self.display.set("0.0")
        
        self.initialize_ui()

    def initialize_ui(self):
        """Configura y muestra los widgets de la interfaz de usuario."""
        miframe = Frame(self.master)
        miframe.pack()

        entry = Entry(miframe, textvariable=self.display, font=("Roboto Cn", 14))
        entry.grid(row=0, column=1, columnspan=8)
        entry.config(background="black", fg="#03f943", justify="right")

        buttons = [
            ("C", 1, 4), ("7", 2, 1), ("8", 2, 2), ("9", 2, 3), ("/", 2, 4),
            ("4", 3, 1), ("5", 3, 2), ("6", 3, 3), ("*", 3, 4),
            ("1", 4, 1), ("2", 4, 2), ("3", 4, 3), ("-", 4, 4),
            ("0", 5, 1), (".", 5, 2), ("=", 5, 3), ("+", 5, 4)
        ]

        for (text, row, col) in buttons:
            button = Button(
                miframe, text=text, width=8, font=("Roboto Cn", 14),
                command=lambda t=text: self.button_pressed(t)
            )
            button.grid(row=row, column=col)

    def button_pressed(self, button_text):
        """
        Maneja los eventos de presión de botón.
        
        Args:
        - button_text (str): El texto del botón que fue presionado.
        """
        if button_text in "0123456789.":
            self.current_input += button_text
        elif button_text in "+-*/":
            self.previous_input = self.current_input
            self.operation = button_text
            self.current_input = ""
        elif button_text == "=":
            if self.operation and self.previous_input:
                try:
                    self.current_input = str(eval(f"{self.previous_input}{self.operation}{self.current_input}"))
                except ZeroDivisionError:
                    self.current_input = "ERROR"
            self.operation = ""
            self.previous_input = ""
        elif button_text == "C":
            self.current_input = ""
            self.operation = ""
            self.previous_input = ""

        self.display.set(self.current_input or "0.0")


if __name__ == "__main__":
    root = Tk()
    SimpleCalculator(root)
    root.mainloop()
