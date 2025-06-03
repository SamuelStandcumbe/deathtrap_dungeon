import tkinter as tk
import dungeon_data
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

class DungeonGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.current_id = "1"
        self.title("Deathtrap Dungeon")
        self.geometry("600x400")

        # Label for displaying the current paragraph
        self.text_label = tk.Label(self, text="", wraplength=550, justify="left")
        self.text_label.pack(pady=20)

        # Frame for the choices buttons
        self.choices_frame = tk.Frame(self)
        self.choices_frame.pack(pady=10)

        # Start the game
        self.update_game()

    def update_game(self):
        current_paragraph = dungeon_data.dungeon[self.current_id]
        self.text_label.config(text=current_paragraph["text"])

        # Clear any previous buttons
        for widget in self.choices_frame.winfo_children():
            widget.destroy()

        choices = current_paragraph.get("choices", {})

        if not choices:
            # End the game if there are no more choices
            self.text_label.config(text=self.text_label.cget("text"))
            return

        # Create a button for each choice
        for key, choice in choices.items():
            button = tk.Button(self.choices_frame, text=choice['text'], command=lambda choice_key=key: self.make_choice(choice_key))
            button.pack(fill='x', pady=5)

    def make_choice(self, choice_key):
        current_paragraph = dungeon_data.dungeon[self.current_id]
        self.current_id = current_paragraph['choices'][choice_key]['next']
        self.update_game()

if __name__ == "__main__":
    game = DungeonGame()
    game.mainloop()
