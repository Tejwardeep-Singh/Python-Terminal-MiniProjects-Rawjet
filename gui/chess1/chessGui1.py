# ==========================================
# TERMINAL CHESS -> TKINTER CHESS
# Two Player Chess Game
# ==========================================

# by Tejwardeep Singh


import tkinter as tk
from tkinter import messagebox


# ==========================================
# CONSTANTS
# ==========================================

BOARD_SIZE = 8
SQUARE_SIZE = 80

LIGHT_SQUARE = "#F0D9B5"
DARK_SQUARE = "#B58863"

SELECTED_COLOR = "#F7EC5E"

WINDOW_BG = "#222222"

FONT_PIECE = ("Segoe UI Symbol", 42)


# ==========================================
# INITIAL CHESS BOARD
# ==========================================

initial_board = [
    ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],
    ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],

    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],

    ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],
    ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
]


# ==========================================
# CURRENT GAME BOARD
# ==========================================

board = [row[:] for row in initial_board]


# ==========================================
# GAME VARIABLES
# ==========================================

current_player = "White"

selected_square = None


# ==========================================
# TKINTER WINDOW
# ==========================================

root = tk.Tk()

root.title("Terminal Chess - Tkinter Edition")

root.configure(bg=WINDOW_BG)

root.resizable(False, False)


# ==========================================
# TITLE
# ==========================================

title_label = tk.Label(
    root,
    text="♔  CHESS  ♚",
    font=("Arial", 26, "bold"),
    bg=WINDOW_BG,
    fg="white"
)

title_label.pack(pady=(15, 5))


# ==========================================
# STATUS
# ==========================================

status_label = tk.Label(
    root,
    text="White's turn",
    font=("Arial", 16, "bold"),
    bg=WINDOW_BG,
    fg="white"
)

status_label.pack(pady=(0, 10))


# ==========================================
# BOARD FRAME
# ==========================================

board_frame = tk.Frame(
    root,
    bg=WINDOW_BG
)

board_frame.pack()


# ==========================================
# CANVAS
# ==========================================

canvas = tk.Canvas(
    board_frame,
    width=BOARD_SIZE * SQUARE_SIZE,
    height=BOARD_SIZE * SQUARE_SIZE,
    highlightthickness=0
)

canvas.pack()


# ==========================================
# CONVERT BOARD POSITION TO COORDINATE
# ==========================================

def coordinate_to_index(position):

    column = ord(position[0]) - ord('a')

    row = 8 - int(position[1])

    return row, column


# ==========================================
# CONVERT INDEX TO CHESS COORDINATE
# ==========================================

def index_to_coordinate(row, column):

    letter = chr(ord('a') + column)

    number = 8 - row

    return letter + str(number)


# ==========================================
# CHECK PIECE COLOR
# ==========================================

def get_piece_color(piece):

    white_pieces = "♙♖♘♗♕♔"

    black_pieces = "♟♜♞♝♛♚"

    if piece in white_pieces:
        return "White"

    if piece in black_pieces:
        return "Black"

    return None


# ==========================================
# DRAW BOARD
# ==========================================

def draw_board():

    canvas.delete("all")

    for row in range(BOARD_SIZE):

        for column in range(BOARD_SIZE):

            x1 = column * SQUARE_SIZE
            y1 = row * SQUARE_SIZE

            x2 = x1 + SQUARE_SIZE
            y2 = y1 + SQUARE_SIZE

            # Determine square color

            if (row + column) % 2 == 0:
                color = LIGHT_SQUARE
            else:
                color = DARK_SQUARE

            # Highlight selected square

            if selected_square == (row, column):
                color = SELECTED_COLOR

            canvas.create_rectangle(
                x1,
                y1,
                x2,
                y2,
                fill=color,
                outline=color
            )

            # Get piece

            piece = board[row][column]

            if piece != " ":

                canvas.create_text(
                    x1 + SQUARE_SIZE / 2,
                    y1 + SQUARE_SIZE / 2,
                    text=piece,
                    font=FONT_PIECE,
                    fill="black"
                )

    # Draw coordinates

    for column in range(BOARD_SIZE):

        letter = chr(ord('a') + column)

        x = column * SQUARE_SIZE + 5

        y = BOARD_SIZE * SQUARE_SIZE - 15

        canvas.create_text(
            x,
            y,
            text=letter,
            anchor="sw",
            font=("Arial", 10, "bold"),
            fill="#333333"
        )

    for row in range(BOARD_SIZE):

        number = 8 - row

        x = 5

        y = row * SQUARE_SIZE + 5

        canvas.create_text(
            x,
            y,
            text=str(number),
            anchor="nw",
            font=("Arial", 10, "bold"),
            fill="#333333"
        )


# ==========================================
# MOVE PIECE
# ==========================================

def move_piece(start, end):

    start_row, start_col = start

    end_row, end_col = end

    piece = board[start_row][start_col]

    if piece == " ":

        return False

    board[end_row][end_col] = piece

    board[start_row][start_col] = " "

    return True


# ==========================================
# HANDLE BOARD CLICK
# ==========================================

def handle_click(event):

    global selected_square
    global current_player

    # Determine clicked square

    column = event.x // SQUARE_SIZE
    row = event.y // SQUARE_SIZE

    # Safety check

    if not (0 <= row < 8 and 0 <= column < 8):
        return

    clicked_piece = board[row][column]

    # --------------------------------------
    # Nothing selected
    # --------------------------------------

    if selected_square is None:

        if clicked_piece == " ":

            return

        piece_color = get_piece_color(clicked_piece)

        # Make sure player selects own piece

        if piece_color != current_player:

            status_label.config(
                text=f"It's {current_player}'s turn!"
            )

            return

        selected_square = (row, column)

        status_label.config(
            text=f"{current_player}: Select destination"
        )

        draw_board()

        return

    # --------------------------------------
    # Something already selected
    # --------------------------------------

    start_row, start_col = selected_square

    # Clicking same square cancels selection

    if selected_square == (row, column):

        selected_square = None

        status_label.config(
            text=f"{current_player}'s turn"
        )

        draw_board()

        return

    # --------------------------------------
    # Move to destination
    # --------------------------------------

    move_piece(
        selected_square,
        (row, column)
    )

    # Clear selection

    selected_square = None

    # Switch player

    if current_player == "White":

        current_player = "Black"

    else:

        current_player = "White"

    status_label.config(
        text=f"{current_player}'s turn"
    )

    draw_board()


# ==========================================
# RESTART GAME
# ==========================================

def restart_game():

    global board
    global current_player
    global selected_square

    result = messagebox.askyesno(
        "Restart Game",
        "Are you sure you want to restart the game?"
    )

    if not result:
        return

    board = [row[:] for row in initial_board]

    current_player = "White"

    selected_square = None

    status_label.config(
        text="White's turn"
    )

    draw_board()


# ==========================================
# QUIT GAME
# ==========================================

def quit_game():

    result = messagebox.askyesno(
        "Quit Game",
        "Are you sure you want to quit?"
    )

    if result:

        root.destroy()


# ==========================================
# BUTTON FRAME
# ==========================================

button_frame = tk.Frame(
    root,
    bg=WINDOW_BG
)

button_frame.pack(
    pady=15
)


# ==========================================
# RESTART BUTTON
# ==========================================

restart_button = tk.Button(
    button_frame,
    text="Restart",
    font=("Arial", 12, "bold"),
    width=10,
    command=restart_game
)

restart_button.pack(
    side="left",
    padx=5
)


# ==========================================
# QUIT BUTTON
# ==========================================

quit_button = tk.Button(
    button_frame,
    text="Quit",
    font=("Arial", 12, "bold"),
    width=10,
    command=quit_game
)

quit_button.pack(
    side="left",
    padx=5
)


# ==========================================
# MOUSE EVENT
# ==========================================

canvas.bind(
    "<Button-1>",
    handle_click
)


# ==========================================
# INITIAL DRAW
# ==========================================

draw_board()


# ==========================================
# START APPLICATION
# ==========================================

root.mainloop()