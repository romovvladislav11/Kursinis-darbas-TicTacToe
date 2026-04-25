import tkinter as tk
import random
from abc import ABC, abstractmethod

# --- 1. ABSTRACTION & INHERITANCE ---
class Player(ABC):
    def __init__(self, symbol):
        self.symbol = symbol

    @abstractmethod
    def get_move(self, board):
        pass

class HumanPlayer(Player):
    def get_move(self, board):
        return None

class BotPlayer(Player):
    def get_move(self, board):
        empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
        return random.choice(empty_cells) if empty_cells else None

# --- 2. DESIGN PATTERN: FACTORY METHOD ---
class PlayerFactory:
    @staticmethod
    def create_players(mode):
        if mode == "botas":
            return [HumanPlayer("X"), BotPlayer("O")]
        return [HumanPlayer("X"), HumanPlayer("O")]

# --- 3. GAME LOGIC (ENCAPSULATION) ---
class TicTacToeLogic:
    def __init__(self):
        self.__board = [[" " for _ in range(3)] for _ in range(3)]
        
    def get_board(self):
        return self.__board

    def make_move(self, r, c, symbol):
        if self.__board[r][c] == " ":
            self.__board[r][c] = symbol
            return True
        return False

    def check_winner(self, s):
        b = self.__board
        win_conditions = [
            [(0,0), (0,1), (0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)],
            [(0,0), (1,0), (2,0)], [(0,1), (1,1), (2,1)], [(0,2), (1,2), (2,2)],
            [(0,0), (1,1), (2,2)], [(0,2), (1,1), (2,0)]
        ]
        return any(all(b[r][c] == s for r, c in line) for line in win_conditions)

    def is_draw(self):
        return all(self.__board[r][c] != " " for r in range(3) for c in range(3))

    def reset(self):
        self.__board = [[" " for _ in range(3)] for _ in range(3)]

# --- 4. COMPOSITION & GUI ---
class TicTacToeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kryžiukai–nuliukai OOP")
        self.attributes("-fullscreen", True)
        self.bind("<Escape>", lambda e: self.destroy())
        
        self.logic = TicTacToeLogic()
        self.players = []
        self.current_idx = 0
        
        self.init_menu()

    def init_menu(self):
        self.menu_frame = tk.Frame(self)
        self.menu_frame.pack(fill="both", expand=True)
        tk.Label(self.menu_frame, text="Kryžiukai–nuliukai", font=("Arial", 40)).pack(pady=50)
        
        tk.Button(self.menu_frame, text="Prieš kompiuterį", font=("Arial", 20), 
                  command=lambda: self.start_game("botas")).pack(pady=10)
        tk.Button(self.menu_frame, text="2 žaidėjai", font=("Arial", 20), 
                  command=lambda: self.start_game("2zaidejai")).pack(pady=10)
        tk.Button(self.menu_frame, text="Išeiti", font=("Arial", 20), 
                  command=self.destroy).pack(pady=10)

    def start_game(self, mode):
        self.players = PlayerFactory.create_players(mode)
        self.current_idx = 0
        self.menu_frame.pack_forget()
        self.setup_grid()

    def setup_grid(self):
        self.game_frame = tk.Frame(self)
        self.game_frame.pack(fill="both", expand=True)
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        for r in range(3):
            self.game_frame.rowconfigure(r, weight=1)
            for c in range(3):
                self.game_frame.columnconfigure(c, weight=1)
                btn = tk.Button(self.game_frame, text=" ", font=("Arial", 60),
                                command=lambda r=r, c=c: self.handle_click(r, c))
                btn.grid(row=r, column=c, sticky="nsew")
                self.buttons[r][c] = btn
        
        self.status_label = tk.Label(self.game_frame, text="X ėjimas", font=("Arial", 20))
        self.status_label.grid(row=3, column=0, columnspan=3)

    def handle_click(self, r, c):
        player = self.players[self.current_idx]
        if self.logic.make_move(r, c, player.symbol):
            self.update_ui()
            if self.process_game_result(player.symbol): return
            
            self.current_idx = 1 - self.current_idx
            next_player = self.players[self.current_idx]
            self.status_label["text"] = f"{next_player.symbol} ėjimas"

            if isinstance(next_player, BotPlayer):
                self.after(500, self.execute_bot_move)

    def execute_bot_move(self):
        bot = self.players[self.current_idx]
        move = bot.get_move(self.logic.get_board())
        if move:
            self.handle_click(move[0], move[1])

    def update_ui(self):
        board = self.logic.get_board()
        for r in range(3):
            for c in range(3):
                self.buttons[r][c]["text"] = board[r][c]

    def process_game_result(self, symbol):
        if self.logic.check_winner(symbol):
            msg = f"{symbol} laimėjo! 🎉" if symbol == "X" else "O laimėjo! 🤖"
            self.finalize_game(msg)
            self.save_log(f"Laimėtojas: {symbol}")
            return True
        if self.logic.is_draw():
            self.finalize_game("Lygiosios!")
            self.save_log("Rezultatas: Lygiosios")
            return True
        return False

    def save_log(self, entry):
        try:
            with open("zaidimo_istorija.txt", "a", encoding="utf-8") as f:
                f.write(entry + "\n")
        except IOError as e:
            print(f"Klaida įrašant failą: {e}")

    def finalize_game(self, message):
        self.status_label["text"] = message
        for r in range(3):
            for c in range(3):
                self.buttons[r][c]["state"] = "disabled"
        self.after(2000, self.return_to_menu)

    def return_to_menu(self):
        self.game_frame.destroy()
        self.logic.reset()
        self.init_menu()

if __name__ == "__main__":
    app = TicTacToeApp()
    app.mainloop()