# THE LAST SIGNAL - A Python Text Adventure Game

while True:
    print("\n" + "=" * 50)
    print("             THE LAST SIGNAL")
    print("=" * 50)

    name = input("Enter your name: ")
    print("\nWelcome, " + name + ".")
    print("You are about to enter a place that nobody has entered for 15 years.")
    print("Your mission: Find the source of a mysterious distress signal.")
    print("Survive. Find the truth. Get out alive.\n")

    ready = input("Are you ready to begin? (y/n): ").lower()

    if ready == 'n':
        print("\nMaybe another time...")
        break

    elif ready != 'y':
        print("Invalid input. Please enter 'y' or 'n'.")
        continue

    print("\nYou arrive at an abandoned research facility at 11:47 PM.")
    print("Rain is hammering against your car.")
    print("The facility has no electricity.")
    print("Suddenly, your radio turns on by itself.")

    print('\nRADIO: "......HELP......LEVEL THREE......HE IS STILL HERE..."')
    print("The signal disappears.")

    print("\nYou enter the facility.")
    print("The main door slams shut behind you.")

    c1 = input(
        "\nThere are two ways forward:\n"
        "1. Enter the security room (s)\n"
        "2. Go directly to the elevator (e)\n"
        "Choose: "
    ).lower()

    # ---------------- SECURITY ROOM ----------------

    if c1 == 's':

        print("\nYou enter the security room.")
        print("Old monitors suddenly flicker on.")
        print("Most of the cameras are dead.")

        print("One camera is still working.")
        print("It shows a hallway on LEVEL THREE.")

        print("\nYou notice something strange.")
        print("A person is standing at the end of the hallway.")
        print("You zoom in...")

        print("The person disappears.")

        c2 = input(
            "\nWhat will you do?\n"
            "1. Check the security recordings (r)\n"
            "2. Go to Level Three immediately (g)\n"
            "Choose: "
        ).lower()

        if c2 == 'r':

            print("\nYou open the security recordings.")
            print("The latest recording is dated...")
            print("TODAY.")

            print("You play it.")

            print('\nRECORDING: "If you\'re watching this, DO NOT GO TO LEVEL THREE."')
            print("The screen suddenly goes black.")

            print("Behind you, you hear footsteps.")

            c3 = input(
                "\nSomeone is approaching.\n"
                "1. Hide under the desk (h)\n"
                "2. Run into the hallway (r)\n"
                "Choose: "
            ).lower()

            if c3 == 'h':

                print("\nYou hide under the desk.")
                print("The footsteps enter the room.")
                print("You see a pair of boots stop directly in front of you.")

                print("Silence...")

                print("The person walks away.")

                print("You wait for several minutes.")
                print("Then you carefully leave the room.")

                c4 = input(
                    "\nYou find a keycard on the floor.\n"
                    "It says: LEVEL THREE - RESTRICTED\n"
                    "\nUse the keycard (k) or leave the facility (l)? "
                ).lower()

                if c4 == 'k':

                    print("\nYou take the keycard.")
                    print("You reach the elevator.")
                    print("The elevator doors open.")

                    print("Inside, someone has written:")
                    print('"DON\'T LET HIM SEE YOU."')

                    c5 = input(
                        "\nGo to Level Three (g) or return outside (o)? "
                    ).lower()

                    if c5 == 'g':

                        print("\nThe elevator descends.")
                        print("Level 1...")
                        print("Level 2...")

                        print("The lights suddenly turn off.")

                        print("You hear breathing inside the elevator.")

                        print("The lights return.")

                        print("You are alone.")

                        print("DING.")

                        print("LEVEL THREE.")

                        print("\nThe doors open.")

                        print("A long dark hallway stretches before you.")

                        c6 = input(
                            "\nYou hear a radio broadcasting from the hallway.\n"
                            "Investigate the radio (i) or stay in the elevator (e)? "
                        ).lower()

                        if c6 == 'i':

                            print("\nYou walk toward the radio.")
                            print("The signal becomes louder.")

                            print('\nRADIO: "You finally came."')

                            print("You freeze.")

                            print("The voice continues...")

                            print('"I\'ve been waiting for you, ' + name + '."')

                            print("\nYou realize something terrifying.")

                            print("The voice knows your name.")

                            print("You turn around.")

                            print("The elevator is gone.")

                            print("\nYou are trapped.")

                            c7 = input(
                                "\nA door appears at the end of the hallway.\n"
                                "Open it (o) or keep walking (w)? "
                            ).lower()

                            if c7 == 'o':

                                print("\nYou open the door.")

                                print("Inside is a massive laboratory.")

                                print("Hundreds of monitors cover the walls.")

                                print("Every monitor shows YOU.")

                                print("Your arrival.")
                                print("Your car.")
                                print("You entering the facility.")

                                print("Someone has been watching you the entire time.")

                                print("\nA final monitor turns on.")

                                print('"EXPERIMENT 27 - SUBJECT HAS ARRIVED."')

                                print("\nA figure steps out from the darkness.")

                                print("You recognize the face.")

                                print("It's YOU.")

                                print("\nThe figure smiles.")

                                print('"You\'re late."')

                                print("\nGAME OVER.")
                                quit()

                            elif c7 == 'w':

                                print("\nYou keep walking.")
                                print("The hallway seems to get longer.")

                                print("You hear footsteps behind you.")

                                print("Then another set.")

                                print("Then another.")

                                print("You start running.")

                                print("The lights turn red.")

                                print("Something grabs your shoulder.")

                                print("\nGAME OVER.")
                                quit()

                            else:
                                print("Invalid choice.")
                                continue

                        elif c6 == 'e':

                            print("\nYou stay inside the elevator.")
                            print("The doors slowly close.")

                            print("Before they shut completely...")
                            print("You see someone standing at the end of the hallway.")

                            print("It's you.")

                            print("\nGAME OVER.")
                            quit()

                        else:
                            print("Invalid choice.")
                            continue

                    elif c5 == 'o':

                        print("\nYou decide to leave.")
                        print("You run toward the main entrance.")

                        print("The door opens.")

                        print("You step outside.")

                        print("Your car is gone.")

                        print("Your phone has no signal.")

                        print("Behind you, the facility lights turn on.")

                        print("Every window is illuminated.")

                        print("Someone is watching you from every floor.")

                        print("\nYou survived the facility...")
                        print("but you are not getting home.")

                        print("\nGAME OVER.")
                        quit()

                    else:
                        print("Invalid choice.")
                        continue

                elif c4 == 'l':

                    print("\nYou decide to leave the facility.")
                    print("You reach the entrance.")

                    print("The door won't open.")

                    print("A message appears on the security screen:")

                    print('"YOU SHOULD HAVE STAYED."')

                    print("\nGAME OVER.")
                    quit()

                else:
                    print("Invalid choice.")
                    continue

            elif c3 == 'r':

                print("\nYou run into the hallway.")
                print("The footsteps immediately start chasing you.")

                print("You run toward the elevator.")

                print("The elevator doors open.")

                print("You jump inside.")

                print("The doors close.")

                print("You breathe heavily.")

                print("Then you notice something.")

                print("The elevator has no buttons.")

                print("It starts moving downward by itself.")

                print("\nYou have no control.")

                print("\nGAME OVER.")
                quit()

            else:
                print("Invalid choice.")
                continue

        elif c2 == 'g':

            print("\nYou decide to ignore the warning.")
            print("You take the stairs to Level Three.")

            print("Halfway down, you hear someone whisper:")

            print('"Turn around."')

            c3 = input(
                "\nTurn around (t) or keep going (k)? "
            ).lower()

            if c3 == 't':

                print("\nYou turn around.")

                print("Nobody is there.")

                print("You continue down.")

                print("The lights suddenly turn off.")

                print("Something touches your neck.")

                print("\nGAME OVER.")
                quit()

            elif c3 == 'k':

                print("\nYou keep walking.")

                print("You reach Level Three.")

                print("A door opens automatically.")

                print("Inside you find hundreds of photographs.")

                print("Every photograph shows you.")

                print("But some were taken years ago.")

                print("\nYou hear a voice behind you.")

                print('"You finally remembered."')

                print("\nGAME OVER.")
                quit()

            else:
                print("Invalid choice.")
                continue

        else:
            print("Invalid choice.")
            continue

    # ---------------- ELEVATOR ----------------

    elif c1 == 'e':

        print("\nYou enter the elevator.")

        print("The control panel has four buttons:")
        print("B - Basement")
        print("1 - Level One")
        print("2 - Level Two")
        print("3 - Level Three")

        c2 = input("Which floor do you choose? (b/1/2/3): ").lower()

        if c2 == 'b':

            print("\nThe elevator descends into the basement.")
            print("The temperature suddenly drops.")

            print("The doors open.")

            print("You see a huge metal door.")

            print("A red light above it is blinking.")

            c3 = input(
                "\nOpen the metal door (o) or return to the elevator (r)? "
            ).lower()

            if c3 == 'o':

                print("\nYou open the door.")

                print("Inside is a control room.")

                print("A computer is still running after 15 years.")

                print("The screen displays:")

                print('"CONTAINMENT FAILURE."')

                print("\nSuddenly, the entire facility begins shaking.")

                print("An alarm starts screaming.")

                print('\nSYSTEM: "CONTAINMENT BREACH."')

                print("You run toward the elevator.")

                print("Something enormous moves behind you.")

                print("You don't look back.")

                print("You reach the elevator.")

                print("The doors close just before something hits them.")

                print("\nYou escape the facility.")

                print("Outside, the storm has stopped.")

                print("You look back.")

                print("The facility is completely dark.")

                print("\nYou survived.")

                print("BUT...")

                print("Your radio turns on.")

                print('\nRADIO: "SUBJECT 28 HAS ESCAPED."')

                print("\nYOU WIN... OR DO YOU?")
                quit()

            elif c3 == 'r':

                print("\nYou return to the elevator.")

                print("The elevator doors close.")

                print("You press Level One.")

                print("Nothing happens.")

                print("The elevator starts going DOWN.")

                print("\nGAME OVER.")
                quit()

            else:
                print("Invalid choice.")
                continue

        elif c2 == '1':

            print("\nYou reach Level One.")

            print("You find the emergency exit.")

            c3 = input(
                "Leave the facility (l) or investigate the strange noise (i)? "
            ).lower()

            if c3 == 'l':

                print("\nYou escape through the emergency exit.")

                print("You survived.")

                print("\nYOU WIN!")
                quit()

            elif c3 == 'i':

                print("\nYou follow the noise.")

                print("It leads to an empty office.")

                print("A phone is ringing.")

                print("You answer it.")

                print('\nVOICE: "Why did you come here?"')

                print("The call ends.")

                print("The door locks.")

                print("\nGAME OVER.")
                quit()

            else:
                print("Invalid choice.")
                continue

        elif c2 == '2':

            print("\nYou reach Level Two.")

            print("The hallway is covered in old photographs.")

            print("One photograph catches your attention.")

            print("It shows the facility staff.")

            print("Everyone is smiling.")

            print("Except one person.")

            print("You.")

            print("\nGAME OVER.")
            quit()

        elif c2 == '3':

            print("\nYou reach Level Three.")

            print("The elevator doors open.")

            print("A voice whispers:")

            print('"Welcome back."')

            print("You have never been here before.")

            print("\nGAME OVER.")
            quit()

        else:
            print("Invalid floor.")
            continue

    else:
        print("Invalid choice. Please choose 's' or 'e'.")
        continue