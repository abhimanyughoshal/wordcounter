import tkinter as tk
from tkinter import ttk
import re
import webbrowser

class WordCounterApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Word and Character Counter")
        self.geometry("600x420")
        
        # Configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Create text box with scrollbar
        self.text_frame = ttk.Frame(self)
        self.text_frame.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.text_frame.grid_rowconfigure(0, weight=1)
        self.text_frame.grid_columnconfigure(0, weight=1)
        
        self.text_box = tk.Text(self.text_frame, wrap="word", font=("Arial", 12))
        self.text_box.grid(row=0, column=0, sticky="nsew")
        
        self.scrollbar = ttk.Scrollbar(self.text_frame, orient="vertical", command=self.text_box.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.text_box.configure(yscrollcommand=self.scrollbar.set)
        
        # Create sidebar frame with widgets
        self.sidebar_frame = ttk.Frame(self, width=140)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        
        self.logo_label = ttk.Label(self.sidebar_frame, text="Word Counter", font=("Arial", 16, "bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.word_count_label = ttk.Label(self.sidebar_frame, text="0 Words")
        self.word_count_label.grid(row=1, column=0, padx=20, pady=(10, 0))
        
        self.char_count_label = ttk.Label(self.sidebar_frame, text="0 Characters")
        self.char_count_label.grid(row=2, column=0, padx=20, pady=(10, 0))
        
        self.clear_button = ttk.Button(self.sidebar_frame, text="Clear Text", command=self.clear_text)
        self.clear_button.grid(row=3, column=0, padx=20, pady=(10, 0))
        
        self.case_label = ttk.Label(self.sidebar_frame, text="Change Case:")
        self.case_label.grid(row=4, column=0, padx=20, pady=(10, 0))
        
        self.case_var = tk.StringVar()
        self.case_options = ["Title Case", "Sentence case", "UPPERCASE", "lowercase"]
        self.case_menu = ttk.Combobox(self.sidebar_frame, textvariable=self.case_var, values=self.case_options, state="readonly")
        self.case_menu.grid(row=5, column=0, padx=20, pady=(5, 0))
        self.case_menu.set("Select case")
        
        self.apply_case_button = ttk.Button(self.sidebar_frame, text="Apply Case", command=self.apply_case)
        self.apply_case_button.grid(row=6, column=0, padx=20, pady=(5, 0))
        
        # Add text size options
        self.size_label = ttk.Label(self.sidebar_frame, text="Text Size:")
        self.size_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        
        self.size_var = tk.StringVar()
        self.size_options = ["Small", "Medium", "Large"]
        self.size_menu = ttk.Combobox(self.sidebar_frame, textvariable=self.size_var, values=self.size_options, state="readonly")
        self.size_menu.grid(row=8, column=0, padx=20, pady=(5, 0))
        self.size_menu.set("Medium")
        self.size_menu.bind("<<ComboboxSelected>>", self.change_text_size)
        
        # Add 'About this app' link
        self.about_link = ttk.Label(self, text="About this app", cursor="hand2", foreground="blue")
        self.about_link.grid(row=1, column=1, sticky="se", padx=(0, 20), pady=(0, 10))
        self.about_link.bind("<Button-1>", self.open_about_link)
        
        # Bind the update_counts function to the text box
        self.text_box.bind("<KeyRelease>", self.update_counts)

    def update_counts(self, event=None):
        text = self.text_box.get("1.0", "end-1c")
        words = len(text.split())
        characters = len(text)
        
        self.word_count_label.config(text=f"{words} Words")
        self.char_count_label.config(text=f"{characters} Characters")

    def clear_text(self):
        self.text_box.delete("1.0", tk.END)
        self.update_counts()

    def apply_case(self):
        text = self.text_box.get("1.0", "end-1c")
        case_option = self.case_var.get()
        
        if case_option == "Title Case":
            modified_text = text.title()
        elif case_option == "Sentence case":
            modified_text = self.sentence_case(text)
        elif case_option == "UPPERCASE":
            modified_text = text.upper()
        elif case_option == "lowercase":
            modified_text = text.lower()
        else:
            return
        
        self.text_box.delete("1.0", tk.END)
        self.text_box.insert("1.0", modified_text)
        self.update_counts()

    def sentence_case(self, text):
        def capitalize_first_and_i(s):
            s = s.capitalize()
            return re.sub(r'\bi\b', 'I', s)

        sentences = re.split('([.!?\n]+)', text)
        
        result = []
        for i, sentence in enumerate(sentences):
            if i % 2 == 0:  # This is a sentence, not a separator
                sentence = capitalize_first_and_i(sentence.strip())
            result.append(sentence)
        
        return ''.join(result)

    def change_text_size(self, event=None):
        size = self.size_var.get()
        if size == "Small":
            self.text_box.configure(font=("Arial", 10))
        elif size == "Medium":
            self.text_box.configure(font=("Arial", 12))
        elif size == "Large":
            self.text_box.configure(font=("Arial", 14))

    def open_about_link(self, event):
        webbrowser.open_new("https://github.com/abhimanyughoshal/wordcounter")

if __name__ == "__main__":
    app = WordCounterApp()
    app.mainloop()
