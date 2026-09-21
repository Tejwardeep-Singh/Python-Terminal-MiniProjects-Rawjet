# ==========================================
# TERMINAL CHESS
# Two Player Chess Game
# ==========================================


# ------------------------------------------
# Chess Board
# ------------------------------------------


import sys

sys.stdout.reconfigure(encoding="utf-8")

board = [
    ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],
    ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],
    ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
]


# ------------------------------------------
# Display Board
# ------------------------------------------

def display_board():

    print()
    print("       TERMINAL CHESS")
    print()

    print("    a   b   c   d   e   f   g   h")
    print("  +---+---+---+---+---+---+---+---+")

    for row in range(8):

        rank = 8 - row

        print(
            f"{rank} | "
            + " | ".join(board[row])
            + f" | {rank}"
        )

        print("  +---+---+---+---+---+---+---+---+")

    print("    a   b   c   d   e   f   g   h")
    print()


# ------------------------------------------
# Convert Chess Coordinate
# Example:
# e2 -> (6, 4)
# e4 -> (4, 4)
# ------------------------------------------

def coordinate_to_index(position):

    column = ord(position[0]) - ord('a')
    row = 8 - int(position[1])

    return row, column


# ------------------------------------------
# Move Piece
# ------------------------------------------

def move_piece(start, end):

    start_row, start_col = coordinate_to_index(start)
    end_row, end_col = coordinate_to_index(end)

    piece = board[start_row][start_col]

    if piece == " ":
        print("❌ There is no piece there.")
        return False

    board[end_row][end_col] = piece
    board[start_row][start_col] = " "

    return True


# ------------------------------------------
# Main Game
# ------------------------------------------

def main():

    current_player = "White"

    while True:

        display_board()

        print(f"{current_player}'s turn")

        move = input("Enter move (e.g. e2e4): ")

        # Exit game
        if move.lower() == "quit":
            print("Game ended.")
            break

        # Basic input validation
        if len(move) != 4:
            print("❌ Invalid format.")
            print("Use something like: e2e4")
            continue

        start = move[:2]
        end = move[2:]

        # Validate coordinates
        if (
            start[0] not in "abcdefgh"
            or end[0] not in "abcdefgh"
            or start[1] not in "12345678"
            or end[1] not in "12345678"
        ):
            print("❌ Invalid chess coordinates.")
            continue

        # Move
        if move_piece(start, end):

            # Switch player
            if current_player == "White":
                current_player = "Black"
            else:
                current_player = "White"


# ------------------------------------------
# Program Entry
# ------------------------------------------

if __name__ == "__main__":
    main()