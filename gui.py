import tkinter as tk
from tkinter import messagebox
from pomodoro import PomodoroManager


class PomodoroGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pomodoro Timer")
        self.manager = PomodoroManager()

        # Variables
        self.timer_running = False
        self.time_remaining = 0

        # Interface
        self.label = tk.Label(self.root, text="Pomodoro Timer", font=("Arial", 20))
        self.label.pack(pady=10)

        self.step_label = tk.Label(self.root, text="", font=("Arial", 15))
        self.step_label.pack(pady=10)

        self.timer_label = tk.Label(self.root, text="00:00", font=("Arial", 30))
        self.timer_label.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Lancer Pomodoro", command=self.start_pomodoro, font=("Arial", 15))
        self.start_button.pack(pady=10)

        self.next_button = tk.Button(self.root, text="Étape suivante", command=self.next_step, font=("Arial", 15), state=tk.DISABLED)
        self.next_button.pack(pady=10)

        self.root.mainloop()

    def start_timer(self, duration, step_name):
        """
        Lance le décompte pour une durée donnée et affiche la progression dans l'interface.
        """
        self.time_remaining = duration
        self.timer_running = True
        self.step_label.config(text=f"Étape : {step_name}")
        self.update_timer()

    def update_timer(self):
        """
        Met à jour l'affichage du timer chaque seconde dans l'interface graphique.
        """
        if self.time_remaining > 0 and self.timer_running:
            minutes, seconds = divmod(self.time_remaining, 60)
            self.timer_label.config(text=f"{minutes:02}:{seconds:02}")
            self.time_remaining -= 1
            self.root.after(1000, self.update_timer)  # Met à jour toutes les secondes
        elif self.time_remaining == 0:
            self.timer_running = False
            self.timer_label.config(text="00:00")
            messagebox.showinfo("Terminé", "Étape terminée ! Passez à l'étape suivante.")
            self.next_button.config(state=tk.NORMAL)

    def start_pomodoro(self):
        """
        Démarre la première étape du cycle Pomodoro.
        """
        self.manager.start_pomodoro()
        self.start_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.DISABLED)
        current_step = self.manager.steps[self.manager.current_step]
        self.start_timer(current_step["duration"], current_step["type"])

    def next_step(self):
        """
        Passe à l'étape suivante du cycle Pomodoro.
        """
        if not self.timer_running:
            self.manager.next_step()
            self.next_button.config(state=tk.DISABLED)
            current_step = self.manager.steps[self.manager.current_step]
            self.start_timer(current_step["duration"], current_step["type"])
