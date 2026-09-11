import tkinter as tk
from tkinter import messagebox
import random


class DiceGame:

    def __init__(self, root):
        self.root = root

        # Window
        self.root.title("🎲 Multiplayer Dice Game")
        self.root.geometry("1100x700")
        self.root.resizable(False, False)

        # Game data
        self.players = []
        self.scores = []
        self.current_player = 0
        self.number_of_players = 0

        self.show_start_screen()

    # =========================================================
    # UTILITY
    # =========================================================

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # =========================================================
    # START SCREEN
    # =========================================================

    def show_start_screen(self):

        self.clear_screen()

        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        title = tk.Label(
            main_frame,
            text="🎲 MULTIPLAYER DICE GAME",
            font=("Arial", 36, "bold")
        )
        title.pack(pady=30)

        subtitle = tk.Label(
            main_frame,
            text="Enter the number of players",
            font=("Arial", 20)
        )
        subtitle.pack(pady=10)

        self.player_count_entry = tk.Entry(
            main_frame,
            font=("Arial", 22),
            width=8,
            justify="center"
        )
        self.player_count_entry.pack(pady=15)

        start_button = tk.Button(
            main_frame,
            text="START GAME",
            font=("Arial", 18, "bold"),
            width=18,
            height=2,
            command=self.get_player_count
        )
        start_button.pack(pady=25)

    # =========================================================
    # GET PLAYER COUNT
    # =========================================================

    def get_player_count(self):

        try:
            n = int(self.player_count_entry.get())

            if n < 2:
                messagebox.showerror(
                    "Invalid Input",
                    "Minimum 2 players are required."
                )
                return

            if n > 10:
                messagebox.showerror(
                    "Invalid Input",
                    "Maximum 10 players are allowed."
                )
                return

            self.number_of_players = n

            self.show_name_screen()

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid number."
            )

    # =========================================================
    # PLAYER NAME SCREEN
    # =========================================================

    def show_name_screen(self):

        self.clear_screen()

        title = tk.Label(
            self.root,
            text="👥 ENTER PLAYER NAMES",
            font=("Arial", 32, "bold")
        )
        title.pack(pady=25)

        subtitle = tk.Label(
            self.root,
            text=f"Enter names for {self.number_of_players} players",
            font=("Arial", 18)
        )
        subtitle.pack(pady=5)

        # Frame containing player names
        names_frame = tk.Frame(self.root)
        names_frame.pack(pady=15)

        self.name_entries = []

        for i in range(self.number_of_players):

            player_frame = tk.Frame(names_frame)
            player_frame.pack(pady=5)

            label = tk.Label(
                player_frame,
                text=f"Player {i + 1}",
                font=("Arial", 17, "bold"),
                width=12,
                anchor="e"
            )
            label.pack(side="left", padx=10)

            entry = tk.Entry(
                player_frame,
                font=("Arial", 17),
                width=35
            )
            entry.pack(side="left", padx=10)

            self.name_entries.append(entry)

        start_button = tk.Button(
            self.root,
            text="🎲 START PLAYING",
            font=("Arial", 18, "bold"),
            width=20,
            height=2,
            command=self.start_game
        )
        start_button.pack(pady=20)

    # =========================================================
    # START GAME
    # =========================================================

    def start_game(self):

        self.players = []

        for entry in self.name_entries:

            name = entry.get().strip()

            if name == "":
                messagebox.showerror(
                    "Invalid Name",
                    "Please enter a name for every player."
                )
                return

            self.players.append(name)

        # Initial scores
        self.scores = [0] * len(self.players)

        # First player
        self.current_player = 0

        self.show_game_screen()

    # =========================================================
    # GAME SCREEN
    # =========================================================

    def show_game_screen(self):

        self.clear_screen()

        # -----------------------------------------------------
        # TITLE
        # -----------------------------------------------------

        title = tk.Label(
            self.root,
            text="🎲 MULTIPLAYER DICE GAME",
            font=("Arial", 30, "bold")
        )
        title.pack(pady=15)

        # -----------------------------------------------------
        # MAIN GAME AREA
        # -----------------------------------------------------

        game_area = tk.Frame(self.root)
        game_area.pack(fill="both", expand=True, padx=30, pady=10)

        # =====================================================
        # LEFT PANEL
        # =====================================================

        left_panel = tk.Frame(
            game_area,
            width=650
        )
        left_panel.pack(
            side="left",
            fill="both",
            expand=True,
            padx=15
        )

        # Current player
        self.turn_label = tk.Label(
            left_panel,
            text="",
            font=("Arial", 24, "bold")
        )
        self.turn_label.pack(pady=10)

        # Dice
        self.dice_label = tk.Label(
            left_panel,
            text="🎲",
            font=("Arial", 90)
        )
        self.dice_label.pack(pady=10)

        # Guess area
        guess_frame = tk.Frame(left_panel)
        guess_frame.pack(pady=10)

        guess_label = tk.Label(
            guess_frame,
            text="Your Guess:",
            font=("Arial", 19, "bold")
        )
        guess_label.pack(side="left", padx=10)

        self.guess_entry = tk.Entry(
            guess_frame,
            font=("Arial", 20),
            width=5,
            justify="center"
        )
        self.guess_entry.pack(side="left", padx=10)

        number_label = tk.Label(
            left_panel,
            text="Enter a number between 1 and 6",
            font=("Arial", 14)
        )
        number_label.pack(pady=3)

        # Roll button
        self.roll_button = tk.Button(
            left_panel,
            text="🎲 ROLL DICE",
            font=("Arial", 19, "bold"),
            width=18,
            height=2,
            command=self.roll_dice
        )
        self.roll_button.pack(pady=15)

        # Result
        self.result_label = tk.Label(
            left_panel,
            text="",
            font=("Arial", 17, "bold"),
            wraplength=550
        )
        self.result_label.pack(pady=5)

        # =====================================================
        # RIGHT PANEL - SCOREBOARD
        # =====================================================

        right_panel = tk.Frame(
            game_area,
            width=350,
            relief="groove",
            borderwidth=2
        )
        right_panel.pack(
            side="right",
            fill="y",
            padx=15
        )

        scoreboard_title = tk.Label(
            right_panel,
            text="📊 SCOREBOARD",
            font=("Arial", 24, "bold")
        )
        scoreboard_title.pack(pady=25)

        # Target score
        target_label = tk.Label(
            right_panel,
            text="First player to reach 5 points wins",
            font=("Arial", 13),
            wraplength=280
        )
        target_label.pack(pady=5)

        # Scoreboard container
        self.scoreboard_frame = tk.Frame(right_panel)
        self.scoreboard_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.update_game_screen()

    # =========================================================
    # UPDATE SCOREBOARD
    # =========================================================

    def update_game_screen(self):

        # Current player
        self.turn_label.config(
            text=f"🎯 {self.players[self.current_player]}'s TURN"
        )

        # Clear scoreboard
        for widget in self.scoreboard_frame.winfo_children():
            widget.destroy()

        # Create player cards
        for i in range(len(self.players)):

            player_frame = tk.Frame(
                self.scoreboard_frame,
                relief="ridge",
                borderwidth=2,
                padx=10,
                pady=8
            )
            player_frame.pack(
                fill="x",
                pady=6
            )

            # Player name
            name_label = tk.Label(
                player_frame,
                text=self.players[i],
                font=("Arial", 16, "bold"),
                anchor="w"
            )
            name_label.pack(side="left", fill="x", expand=True)

            # Score
            score_label = tk.Label(
                player_frame,
                text=f"{self.scores[i]} / 5",
                font=("Arial", 16, "bold")
            )
            score_label.pack(side="right")

            # Highlight current player
            if i == self.current_player:

                player_frame.config(
                    borderwidth=3
                )

    # =========================================================
    # ROLL DICE
    # =========================================================

    def roll_dice(self):

        # Get guess
        try:

            guess = int(self.guess_entry.get())

            if guess < 1 or guess > 6:

                messagebox.showerror(
                    "Invalid Guess",
                    "Please enter a number between 1 and 6."
                )

                return

        except ValueError:

            messagebox.showerror(
                "Invalid Guess",
                "Please enter a number between 1 and 6."
            )

            return

        # Generate dice value
        dice_value = random.randint(1, 6)

        # Dice faces
        dice_faces = {
            1: "⚀",
            2: "⚁",
            3: "⚂",
            4: "⚃",
            5: "⚄",
            6: "⚅"
        }

        # Display dice
        self.dice_label.config(
            text=dice_faces[dice_value]
        )

        # -----------------------------------------------------
        # CHECK GUESS
        # -----------------------------------------------------

        if guess == dice_value:

            self.scores[self.current_player] += 1

            self.result_label.config(
                text=f"✅ CORRECT!\n"
                     f"You guessed {guess}. +1 POINT!"
            )

        else:

            self.result_label.config(
                text=f"❌ WRONG!\n"
                     f"The dice was {dice_value}."
            )

        # Update scoreboard
        self.update_game_screen()

        # -----------------------------------------------------
        # CHECK WINNER
        # -----------------------------------------------------

        if self.scores[self.current_player] >= 5:

            winner = self.players[self.current_player]

            self.show_winner_screen(winner)

            return

        # -----------------------------------------------------
        # NEXT PLAYER
        # -----------------------------------------------------

        self.current_player += 1

        if self.current_player >= len(self.players):
            self.current_player = 0

        # Clear guess
        self.guess_entry.delete(0, tk.END)

        # Update turn
        self.update_game_screen()

    # =========================================================
    # WINNER SCREEN
    # =========================================================

    def show_winner_screen(self, winner):

        self.clear_screen()

        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True)

        title = tk.Label(
            main_frame,
            text="🏆 GAME OVER 🏆",
            font=("Arial", 42, "bold")
        )
        title.pack(pady=40)

        winner_label = tk.Label(
            main_frame,
            text=f"🎉 {winner} WINS! 🎉",
            font=("Arial", 34, "bold")
        )
        winner_label.pack(pady=25)

        score_label = tk.Label(
            main_frame,
            text="Congratulations!",
            font=("Arial", 22)
        )
        score_label.pack(pady=10)

        new_game_button = tk.Button(
            main_frame,
            text="🔄 NEW GAME",
            font=("Arial", 19, "bold"),
            width=18,
            height=2,
            command=self.show_start_screen
        )
        new_game_button.pack(pady=35)


# =============================================================
# MAIN
# =============================================================

root = tk.Tk()

game = DiceGame(root)

root.mainloop()