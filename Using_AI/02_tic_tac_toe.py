"""Simple Tic-Tac-Toe CLI game.

Features implemented:
- 3x3 board
- Print board and current state
- Player input with validation
- Win and draw detection
- Switch players
- Play loop with replay option
- Non-interactive `--test` mode for automated smoke tests

Run `python 02_tic_tac_toe.py` to play.
"""

import sys
from typing import List, Optional, Tuple

BOARD_SIZE = 3
EMPTY_CELL = " "


def create_board() -> List[List[str]]:
    return [[EMPTY_CELL for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def print_board(board: List[List[str]]) -> None:
	print("\nCurrent board:")
	for r in range(3):
		row = " | ".join(board[r])
		print(f" {row} ")
		if r < 2:
			print("---+---+---")


def check_win(board: List[List[str]]) -> Optional[str]:
	# rows
	for r in range(3):
		if board[r][0] != " " and board[r][0] == board[r][1] == board[r][2]:
			return board[r][0]
	# cols
	for c in range(3):
		if board[0][c] != " " and board[0][c] == board[1][c] == board[2][c]:
			return board[0][c]
	# diagonals
	if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
		return board[0][0]
	if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
		return board[0][2]
	return None


def check_draw(board: List[List[str]]) -> bool:
	return all(cell != " " for row in board for cell in row) and check_win(board) is None


def switch_player(current: str) -> str:
	return "O" if current == "X" else "X"


def is_valid_move(board: List[List[str]], pos: int) -> bool:
	if pos < 1 or pos > 9:
		return False
	r, c = divmod(pos - 1, 3)
	return board[r][c] == " "


def apply_move(board: List[List[str]], pos: int, player: str) -> None:
	r, c = divmod(pos - 1, 3)
	board[r][c] = player


def get_player_move(board: List[List[str]], player: str) -> int:
	while True:
		try:
			raw = input(f"Player {player}, enter move (1-9): ")
			pos = int(raw)
			if is_valid_move(board, pos):
				return pos
			else:
				print("Invalid move. Cell is occupied or out of range.")
		except ValueError:
			print("Please enter a number between 1 and 9.")


def display_instructions() -> None:
	print("Tic-Tac-Toe positions are numbered as follows:")
	print(" 1 | 2 | 3 \n---+---+---\n 4 | 5 | 6 \n---+---+---\n 7 | 8 | 9 ")


def play_game(interactive: bool = True, moves: Optional[List[int]] = None) -> Tuple[Optional[str], List[List[str]]]:
	board = create_board()
	current = "X"
	move_iter = iter(moves) if moves is not None else None
	while True:
		print_board(board)
		winner = check_win(board)
		if winner:
			print(f"\nPlayer {winner} wins!")
			return winner, board
		if check_draw(board):
			print("\nIt's a draw!")
			return None, board

		if interactive:
			pos = get_player_move(board, current)
		else:
			try:
				pos = next(move_iter)  # type: ignore
				print(f"Auto move for {current}: {pos}")
			except StopIteration:
				print("No more moves provided for test run.")
				return None, board

		apply_move(board, pos, current)
		current = switch_player(current)


def reset_board(board: List[List[str]]) -> None:
	for r in range(3):
		for c in range(3):
			board[r][c] = " "


def main() -> None:
	print("Welcome to Tic-Tac-Toe!")
	display_instructions()
	while True:
		choice = input("Enter P to play, Q to quit: ").strip().upper()
		if choice == "Q":
			print("Goodbye!")
			break
		if choice == "P":
			winner, _ = play_game(interactive=True)
			# After game ends, ask to replay
			again = input("Play again? (Y/N): ").strip().upper()
			if again != "Y":
				print("Thanks for playing!")
				break


def self_test() -> None:
	# Automated test: X should win with moves 1,2,3
	print("Running self-test...")
	moves = [1, 4, 2, 5, 3]
	winner, board = play_game(interactive=False, moves=moves)
	print_board(board)
	assert winner == "X", f"Expected winner X, got {winner}"
	print("Self-test passed: X wins as expected.")


if __name__ == "__main__":
	if "--test" in sys.argv:
		self_test()
	else:
		main()




