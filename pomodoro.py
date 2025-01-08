import time

class PomodoroManager:
    def __init__(self):
        self.steps = [
            {"type": "Travail", "duration": 50 * 60},
            {"type": "Pause courte", "duration": 10 * 60},
            {"type": "Travail", "duration": 50 * 60},
            {"type": "Pause courte", "duration": 10 * 60},
            {"type": "Travail", "duration": 50 * 60},
            {"type": "Grande pause", "duration": 30 * 60}
        ]
        self.current_step = 0

    def start_pomodoro(self):
        self.current_step = 0
        print("Pomodoro démarré !")
        self.run_step()

    def next_step(self):
        self.current_step += 1
        if self.current_step >= len(self.steps):
            print("Cycle terminé. Recommençons depuis le début.")
            self.current_step = 0
        self.run_step()

    def current_duration(self):
        return self.steps[self.current_step]["duration"]

    def run_step(self):
        current_step_info = self.steps[self.current_step]
        print(f"\n--- {current_step_info['type']} ---")
        duration = current_step_info["duration"]

        for remaining in range(duration, 0, -1):
            minutes, seconds = divmod(remaining, 60)
            print(f"Temps restant : {minutes:02}:{seconds:02}", end="\r")
            time.sleep(1)
        print(f"\n{current_step_info['type']} terminé !")

        if self.current_step < len(self.steps) - 1:
            print("Étape suivante prête.")
        else:
            print("Fin du cycle Pomodoro.")
