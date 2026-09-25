import random as rd
import  customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
class ModernGuessingGame(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🎯 Number Guessing Game Pro")
        self.geometry("800x820")
        self.resizable(False,False)
        self.secret_num=0
        self.attempts=0
        self.max_attempts=10
        self.bg_color = "#10002B"
        self.card_color = "#240046"
        self.purple = "#7B2CBF"
        self.pink = "#FF4ECD"
        self.cyan = "#00F5FF"
        self.green = "#39FF88"
        self.red = "#FF4B5C"
        self.yellow = "#FFD166"
        self.configure(fg_color=self.bg_color)
        self.create_widgets()
        self.reset_game()
    def create_widgets(self):
        self.main_frame = ctk.CTkFrame(self,width=440,height=470,corner_radius=25,fg_color=self.card_color,border_width=2,border_color=self.purple)
        self.main_frame.pack(pady=25)
        self.main_frame.pack_propagate(False)
        self.title_label=ctk.CTkLabel(self.main_frame,text="🎯Guess the Number !",font=ctk.CTkFont(size=27,weight="bold"),text_color=self.cyan)
        self.title_label.pack(pady=(25,5))
        self.subtitle_label=ctk.CTkLabel(self.main_frame,text="⚡ NEON ARCADE MODE ⚡",font=ctk.CTkFont(size=13,weight="bold"),text_color=self.pink)
        self.subtitle_label.pack(pady=(0,15))
        self.instructions_label=ctk.CTkLabel(self.main_frame,text=f"I'm thinking of a number between 1 and 100...... ",font=ctk.CTkFont(size=14),text_color="#D8B4FE")
        self.instructions_label.pack(pady=5)
        self.attempts_label=ctk.CTkLabel(self.main_frame,text="🔥 Total Attempts  : 10 🔥",font=ctk.CTkFont(size=16,weight="bold"),text_color=self.yellow)
        self.attempts_label.pack(pady=10)
        self.guess_entry=ctk.CTkEntry(self.main_frame,placeholder_text="Enter your guess . . .",width=240,height=55,corner_radius=18,border_width=2,border_color=self.cyan,fg_color="#16002E",text_color="white",placeholder_text_color="#8E7CC3",font=ctk.CTkFont(size=20,weight="bold"),justify="center")
        self.guess_entry.pack(pady=15)
        self.guess_entry.bind("<Return>",lambda event : self.check_guess())
        self.submit_btn=ctk.CTkButton(self.main_frame,text="🚀 Submit Guess",width=240,height=50,corner_radius=18,fg_color=self.purple,hover_color=self.pink,font=ctk.CTkFont(size=14,weight="bold"),command=self.check_guess)
        self.submit_btn.pack(pady=5)
        self.feedback_label=ctk.CTkLabel(self.main_frame,text="✨ Make your first guess ! ✨",font=ctk.CTkFont(size=15,weight="bold"),text_color=self.cyan,wraplength=380)
        self.feedback_label.pack(pady=18)
        self.reset_btn=ctk.CTkButton(self.main_frame,text="🔃 Restart Game",width=180,height=38,corner_radius=15,fg_color="transparent",border_width=2,border_color=self.pink,hover_color=self.pink,text_color="white",font=ctk.CTkFont(size=13,weight="bold"),command=self.reset_game)
        self.reset_btn.pack(pady=5)
        self.footer_label=ctk.CTkLabel(self.main_frame,text="💜 Have fun • Think smart • Guess fast  💜",font=ctk.CTkFont(size=11),text_color="#9D8AC7")
        self.footer_label.pack(pady=(12,0))
    def check_guess(self):
        user_input=self.guess_entry.get().strip()
        if not user_input.isdigit():
            self.feedback_label.configure(text="⚠Please enter a whole number !",text_color=self.red)
            return
        guess=int(user_input)
        if(guess < 1 or guess > 100):
             self.feedback_label.configure(text="Range must be between 1 and 100 !",text_color=self.red)
             return
        self.attempts+=1
        remaining_attempts=(self.max_attempts-self.attempts)
        if(guess == self.secret_num):
            self.feedback_label.configure(text=f"🎉Jackpot 🎉 !\n You guessed it in {self.attempts} tries !",text_color=self.green)
            self.attempts_label.configure(text="🏆 YOU WON ! 🏆",text_color=self.green)
            self.end_game()
        elif(remaining_attempts <= 0):
             self.feedback_label.configure(text=f"💀 Game Over !\n The number was {self.secret_num} .",text_color=self.red)
             self.attempts_label.configure(text="💀 NO ATTEMPTS LEFT  ! 💀",text_color=self.red)
             self.end_game()
        elif(guess < self.secret_num):
             self.feedback_label.configure(text="📉 Too Low ! Try higher",text_color=self.cyan)
             self.instructions_label.configure(text=f"🔥 Attempts left : {remaining_attempts} 🔥")
        else:
            self.feedback_label.configure(text="📈 Too High ! Try lower",text_color=self.yellow)
            self.instructions_label.configure(text=f"🔥 Attempts left : {remaining_attempts} 🔥")
        self.guess_entry.delete(0,ctk.END)
        self.guess_entry.focus()
    def end_game(self):
        self.guess_entry.configure(state="disabled")
        self.submit_btn.configure(state="disabled")
    def reset_game(self):
        self.secret_num=rd.randint(1,100)
        self.attempts=0
        self.instructions_label.configure(text="I'm thinking of a number between 1 and 100 . . .")
        self.attempts_label.configure(text=f"🔥 ATTEMPTS LEFT : {self.max_attempts} 🔥",text_color=self.yellow)
        self.feedback_label.configure(text="✨ Make your first guess ! ✨",text_color=self.cyan)
        self.guess_entry.configure(state="normal")
        self.submit_btn.configure(state="normal")
        self.guess_entry.delete(0,ctk.END)
        self.guess_entry.focus()
if(__name__ == "__main__"):
    app=ModernGuessingGame()
    app.mainloop()
            
