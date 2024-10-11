import tkinter as tk
import customtkinter as ctk

class WordCounterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Word Counter")
        self.geometry("600x400")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_widgets()

    def create_widgets(self):
        main_frame = ctk.CTkFrame(self)
        main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)

        self.text_input = ctk.CTkTextbox(main_frame, wrap="word")
        self.text_input.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="nsew")
        self.text_input.bind("<KeyRelease>", self.update_count)

        button_frame = ctk.CTkFrame(main_frame)
        button_frame.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="ew")
        button_frame.grid_columnconfigure((0, 1, 2), weight=1)

        clear_button = ctk.CTkButton(button_frame, text="Clear", command=self.clear_text)
        clear_button.grid(row=0, column=0, padx=5, pady=5)

        font_size_label = ctk.CTkLabel(button_frame, text="Font Size:")
        font_size_label.grid(row=0, column=1, padx=5, pady=5)

        self.font_size_var = tk.StringVar(value="12")
        font_size_menu = ctk.CTkOptionMenu(
            button_frame,
            values=["8", "10", "12", "14", "16", "18", "20"],
            variable=self.font_size_var,
            command=self.change_font_size
        )
        font_size_menu.grid(row=0, column=2, padx=5, pady=5)

        self.count_label = ctk.CTkLabel(main_frame, text="Characters: 0 | Words: 0")
        self.count_label.grid(row=2, column=0, padx=10, pady=(5, 10), sticky="w")

    def update_count(self, event=None):
        text = self.text_input.get("1.0", "end-1c")
        char_count = len(text)
        word_count = len(text.split())
        self.count_label.configure(text=f"Characters: {char_count} | Words: {word_count}")

    def clear_text(self):
        self.text_input.delete("1.0", "end")
        self.update_count()

    def change_font_size(self, size):
        self.text_input.configure(font=("TkDefaultFont", int(size)))

if __name__ == "__main__":
    app = WordCounterApp()
    app.mainloop()
