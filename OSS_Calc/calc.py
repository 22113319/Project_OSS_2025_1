import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""
        self.history = []

        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=', '기록 보기', '기록 삭제']  # 新增“기록 삭제”按钮
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.history.append(f"{self.expression} = {result}")
                self.expression = result
            except Exception:
                self.history.append(f"{self.expression} = 에러")
                self.expression = "에러"
        elif char == '기록 보기':
            self.show_history()
            return
        elif char == '기록 삭제':
            self.history.clear()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "기록 삭제 완료")
            return
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def show_history(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("계산 기록")
        history_window.geometry("300x300")

        text_area = tk.Text(history_window, font=("Arial", 14))
        text_area.pack(expand=True, fill="both")

        if self.history:
            text_area.insert(tk.END, "\n".join(self.history))
        else:
            text_area.insert(tk.END, "기록이 없습니다.")


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
