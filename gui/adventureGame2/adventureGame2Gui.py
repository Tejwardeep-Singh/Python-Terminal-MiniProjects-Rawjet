import tkinter as tk
from tkinter import messagebox


class LastSignalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("THE LAST SIGNAL")
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg="#050505")
        self.name = ""

        self.title_font = ("Consolas", 34, "bold")
        self.story_font = ("Consolas", 18)
        self.button_font = ("Consolas", 16, "bold")

        self.title = tk.Label(
            root, text="THE LAST SIGNAL",
            font=self.title_font, fg="#d8d8d8", bg="#050505"
        )
        self.title.pack(pady=(45, 20))

        self.story = tk.Text(
            root, font=self.story_font, fg="#d0d0d0", bg="#0b0b0b",
            insertbackground="#d0d0d0", relief="flat", wrap="word",
            padx=35, pady=25
        )
        self.story.pack(fill="both", expand=True, padx=45, pady=10)
        self.story.config(state="disabled")

        self.buttons = tk.Frame(root, bg="#050505")
        self.buttons.pack(fill="x", padx=60, pady=(10, 35))

        self.exit_btn = tk.Button(
            root, text="EXIT", command=self.close,
            font=("Consolas", 12, "bold"), fg="#aaaaaa", bg="#151515",
            activebackground="#252525", activeforeground="white",
            relief="flat", padx=15, pady=7
        )
        self.exit_btn.place(relx=0.98, rely=0.02, anchor="ne")

        self.show_intro()

    def clear_buttons(self):
        for w in self.buttons.winfo_children():
            w.destroy()

    def write(self, text, clear=False):
        self.story.config(state="normal")
        if clear:
            self.story.delete("1.0", "end")
        self.story.insert("end", text + "\n\n")
        self.story.see("end")
        self.story.config(state="disabled")

    def choices(self, options):
        self.clear_buttons()
        for label, command in options:
            tk.Button(
                self.buttons, text=label, command=command,
                font=self.button_font, fg="#eeeeee", bg="#171717",
                activebackground="#303030", activeforeground="white",
                relief="flat", bd=0, padx=25, pady=14,
                cursor="hand2"
            ).pack(side="left", expand=True, fill="x", padx=8)

    def show_intro(self):
        self.write(
            "THE LAST SIGNAL\n"
            "==================================================\n\n"
            "You are about to enter a place that nobody has entered for 15 years.\n"
            "Your mission: Find the source of a mysterious distress signal.\n"
            "Survive. Find the truth. Get out alive.",
            clear=True
        )
        self.clear_buttons()
        entry_frame = tk.Frame(self.buttons, bg="#050505")
        entry_frame.pack(fill="x")

        tk.Label(
            entry_frame, text="ENTER YOUR NAME:",
            font=("Consolas", 16, "bold"), fg="#aaa", bg="#050505"
        ).pack(pady=5)

        name_entry = tk.Entry(
            entry_frame, font=("Consolas", 18), fg="white", bg="#151515",
            insertbackground="white", relief="flat", justify="center"
        )
        name_entry.pack(pady=8, ipadx=10, ipady=8)
        name_entry.focus_set()

        tk.Button(
            entry_frame, text="BEGIN", command=lambda: self.begin(name_entry),
            font=self.button_font, fg="white", bg="#252525",
            activebackground="#404040", relief="flat", padx=45, pady=12
        ).pack(pady=10)

    def begin(self, entry):
        self.name = entry.get().strip() or "Traveler"
        self.write(
            f"Welcome, {self.name}.\n\n"
            "Are you ready to begin?\n\n"
            "You arrive at an abandoned research facility at 11:47 PM.\n"
            "Rain is hammering against your car.\n"
            "The facility has no electricity.\n"
            "Suddenly, your radio turns on by itself.\n\n"
            'RADIO: "......HELP......LEVEL THREE......HE IS STILL HERE..."\n'
            "The signal disappears.\n\n"
            "You enter the facility.\n"
            "The main door slams shut behind you.",
            clear=True
        )
        self.choices([
            ("ENTER SECURITY ROOM", self.security_room),
            ("GO TO ELEVATOR", self.elevator)
        ])

    def security_room(self):
        self.write(
            "You enter the security room.\n"
            "Old monitors suddenly flicker on.\n"
            "Most of the cameras are dead.\n\n"
            "One camera is still working.\n"
            "It shows a hallway on LEVEL THREE.\n\n"
            "You notice something strange.\n"
            "A person is standing at the end of the hallway.\n"
            "You zoom in...\n\n"
            "The person disappears.",
            clear=True
        )
        self.choices([
            ("CHECK RECORDINGS", self.recordings),
            ("GO TO LEVEL THREE", self.security_go_level3)
        ])

    def recordings(self):
        self.write(
            "You open the security recordings.\n"
            "The latest recording is dated...\n"
            "TODAY.\n\n"
            "You play it.\n\n"
            'RECORDING: "If you\'re watching this, DO NOT GO TO LEVEL THREE."\n'
            "The screen suddenly goes black.\n\n"
            "Behind you, you hear footsteps.\n\n"
            "Someone is approaching.",
            clear=True
        )
        self.choices([
            ("HIDE UNDER THE DESK", self.hide_desk),
            ("RUN INTO THE HALLWAY", self.run_hallway)
        ])

    def hide_desk(self):
        self.write(
            "You hide under the desk.\n"
            "The footsteps enter the room.\n"
            "You see a pair of boots stop directly in front of you.\n\n"
            "Silence...\n\n"
            "The person walks away.\n"
            "You wait for several minutes.\n"
            "Then you carefully leave the room.\n\n"
            "You find a keycard on the floor.\n"
            "It says: LEVEL THREE - RESTRICTED",
            clear=True
        )
        self.choices([
            ("USE KEYCARD", self.keycard),
            ("LEAVE FACILITY", self.leave_locked)
        ])

    def keycard(self):
        self.write(
            "You take the keycard.\n"
            "You reach the elevator.\n"
            "The elevator doors open.\n\n"
            'Inside, someone has written:\n"DON\'T LET HIM SEE YOU."',
            clear=True
        )
        self.choices([
            ("GO TO LEVEL THREE", self.level3_elevator),
            ("RETURN OUTSIDE", self.escape_outside)
        ])

    def level3_elevator(self):
        self.write(
            "The elevator descends.\n"
            "Level 1...\n"
            "Level 2...\n\n"
            "The lights suddenly turn off.\n"
            "You hear breathing inside the elevator.\n\n"
            "The lights return.\n"
            "You are alone.\n\n"
            "DING.\n"
            "LEVEL THREE.\n\n"
            "The doors open.\n"
            "A long dark hallway stretches before you.\n\n"
            "You hear a radio broadcasting from the hallway.",
            clear=True
        )
        self.choices([
            ("INVESTIGATE RADIO", self.radio),
            ("STAY IN ELEVATOR", self.elevator_self)
        ])

    def radio(self):
        self.write(
            "You walk toward the radio.\n"
            "The signal becomes louder.\n\n"
            'RADIO: "You finally came."\n\n'
            "You freeze.\n"
            "The voice continues...\n\n"
            f'"I\'ve been waiting for you, {self.name}."\n\n'
            "You realize something terrifying.\n"
            "The voice knows your name.\n\n"
            "You turn around.\n"
            "The elevator is gone.\n\n"
            "You are trapped.\n\n"
            "A door appears at the end of the hallway.",
            clear=True
        )
        self.choices([
            ("OPEN THE DOOR", self.lab),
            ("KEEP WALKING", self.long_hallway)
        ])

    def lab(self):
        self.game_over(
            "You open the door.\n\n"
            "Inside is a massive laboratory.\n"
            "Hundreds of monitors cover the walls.\n"
            "Every monitor shows YOU.\n\n"
            "Your arrival.\n"
            "Your car.\n"
            "You entering the facility.\n\n"
            "Someone has been watching you the entire time.\n\n"
            'A final monitor turns on:\n"EXPERIMENT 27 - SUBJECT HAS ARRIVED."\n\n'
            "A figure steps out from the darkness.\n"
            "You recognize the face.\n\n"
            "It's YOU.\n\n"
            'The figure smiles.\n\n"You\'re late."'
        )

    def long_hallway(self):
        self.game_over(
            "You keep walking.\n"
            "The hallway seems to get longer.\n\n"
            "You hear footsteps behind you.\n"
            "Then another set.\n"
            "Then another.\n\n"
            "You start running.\n"
            "The lights turn red.\n"
            "Something grabs your shoulder."
        )

    def elevator_self(self):
        self.game_over(
            "You stay inside the elevator.\n"
            "The doors slowly close.\n\n"
            "Before they shut completely...\n"
            "You see someone standing at the end of the hallway.\n\n"
            "It's you."
        )

    def security_go_level3(self):
        self.write(
            "You decide to ignore the warning.\n"
            "You take the stairs to Level Three.\n\n"
            "Halfway down, you hear someone whisper:\n"
            '"Turn around."',
            clear=True
        )
        self.choices([
            ("TURN AROUND", self.turn_around),
            ("KEEP GOING", self.keep_going)
        ])

    def turn_around(self):
        self.game_over(
            "You turn around.\n"
            "Nobody is there.\n"
            "You continue down.\n"
            "The lights suddenly turn off.\n"
            "Something touches your neck."
        )

    def keep_going(self):
        self.game_over(
            "You keep walking.\n"
            "You reach Level Three.\n"
            "A door opens automatically.\n\n"
            "Inside you find hundreds of photographs.\n"
            "Every photograph shows you.\n"
            "But some were taken years ago.\n\n"
            'You hear a voice behind you:\n"You finally remembered."'
        )

    def leave_locked(self):
        self.game_over(
            "You decide to leave the facility.\n"
            "You reach the entrance.\n"
            "The door won't open.\n\n"
            "A message appears on the security screen:\n"
            '"YOU SHOULD HAVE STAYED."'
        )

    def escape_outside(self):
        self.game_over(
            "You decide to leave.\n"
            "You run toward the main entrance.\n"
            "The door opens.\n"
            "You step outside.\n\n"
            "Your car is gone.\n"
            "Your phone has no signal.\n\n"
            "Behind you, the facility lights turn on.\n"
            "Every window is illuminated.\n"
            "Someone is watching you from every floor.\n\n"
            "You survived the facility...\n"
            "but you are not getting home."
        )

    # ---------------- DIRECT ELEVATOR PATH ----------------

    def elevator(self):
        self.write(
            "You enter the elevator.\n\n"
            "The control panel has four buttons:\n"
            "B - Basement\n"
            "1 - Level One\n"
            "2 - Level Two\n"
            "3 - Level Three",
            clear=True
        )
        self.choices([
            ("B — BASEMENT", self.basement),
            ("1 — LEVEL ONE", self.level_one),
            ("2 — LEVEL TWO", self.level_two),
            ("3 — LEVEL THREE", self.direct_level3)
        ])

    def basement(self):
        self.write(
            "The elevator descends into the basement.\n"
            "The temperature suddenly drops.\n\n"
            "The doors open.\n"
            "You see a huge metal door.\n"
            "A red light above it is blinking.",
            clear=True
        )
        self.choices([
            ("OPEN METAL DOOR", self.control_room),
            ("RETURN TO ELEVATOR", self.basement_return)
        ])

    def control_room(self):
        self.write(
            "You open the door.\n\n"
            "Inside is a control room.\n"
            "A computer is still running after 15 years.\n"
            "The screen displays:\n\n"
            '"CONTAINMENT FAILURE."\n\n'
            "Suddenly, the entire facility begins shaking.\n"
            "An alarm starts screaming.\n\n"
            'SYSTEM: "CONTAINMENT BREACH."\n\n'
            "You run toward the elevator.\n"
            "Something enormous moves behind you.\n"
            "You don't look back.\n\n"
            "You reach the elevator.\n"
            "The doors close just before something hits them.\n\n"
            "You escape the facility.\n"
            "Outside, the storm has stopped.\n"
            "You look back.\n"
            "The facility is completely dark.\n\n"
            "You survived.\n\n"
            "BUT...\n\n"
            "Your radio turns on.\n"
            'RADIO: "SUBJECT 28 HAS ESCAPED."\n\n'
            "YOU WIN... OR DO YOU?",
            clear=True
        )
        self.end_buttons(win=True)

    def basement_return(self):
        self.game_over(
            "You return to the elevator.\n"
            "The elevator doors close.\n"
            "You press Level One.\n"
            "Nothing happens.\n"
            "The elevator starts going DOWN.\n\n"
            "You have no control."
        )

    def level_one(self):
        self.write(
            "You reach Level One.\n"
            "You find the emergency exit.",
            clear=True
        )
        self.choices([
            ("LEAVE FACILITY", self.win_level1),
            ("INVESTIGATE STRANGE NOISE", self.office)
        ])

    def win_level1(self):
        self.write(
            "You escape through the emergency exit.\n"
            "You survived.\n\n"
            "YOU WIN!",
            clear=True
        )
        self.end_buttons(win=True)

    def office(self):
        self.game_over(
            "You follow the noise.\n"
            "It leads to an empty office.\n\n"
            "A phone is ringing.\n"
            "You answer it.\n\n"
            'VOICE: "Why did you come here?"\n\n'
            "The call ends.\n"
            "The door locks."
        )

    def level_two(self):
        self.game_over(
            "You reach Level Two.\n"
            "The hallway is covered in old photographs.\n\n"
            "One photograph catches your attention.\n"
            "It shows the facility staff.\n"
            "Everyone is smiling.\n"
            "Except one person.\n\n"
            "You."
        )

    def direct_level3(self):
        self.game_over(
            "You reach Level Three.\n"
            "The elevator doors open.\n\n"
            'A voice whispers:\n"Welcome back."\n\n'
            "You have never been here before."
        )

    def game_over(self, text):
        self.write(text + "\n\nGAME OVER.", clear=True)
        self.end_buttons(win=False)

    def end_buttons(self, win=False):
        self.clear_buttons()
        tk.Button(
            self.buttons, text="PLAY AGAIN", command=self.show_intro,
            font=self.button_font, fg="white", bg="#252525",
            activebackground="#404040", relief="flat",
            padx=35, pady=12
        ).pack(side="left", expand=True, padx=10)
        tk.Button(
            self.buttons, text="EXIT", command=self.close,
            font=self.button_font, fg="white", bg="#151515",
            activebackground="#303030", relief="flat",
            padx=35, pady=12
        ).pack(side="left", expand=True, padx=10)

    def close(self):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = LastSignalGUI(root)
    root.mainloop()
