import unittest
from game import TicTacToeLogic 

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        """Šis metodas paleidžiamas prieš kiekvieną testą — sukuriamas naujas žaidimo objektas."""
        self.game = TicTacToeLogic()

    def test_horizontal_win(self):
        """Patikrina, ar teisingai nustatoma pergalė horizontalioje eilutėje."""
        self.game.make_move(0, 0, "X")
        self.game.make_move(0, 1, "X")
        self.game.make_move(0, 2, "X")
        self.assertTrue(self.game.check_winner("X"))

    def test_vertical_win(self):
        """Patikrina, ar teisingai nustatoma pergalė vertikaliame stulpelyje."""
        self.game.make_move(0, 1, "O")
        self.game.make_move(1, 1, "O")
        self.game.make_move(2, 1, "O")
        self.assertTrue(self.game.check_winner("O"))

    def test_diagonal_win(self):
        """Patikrina, ar teisingai nustatoma pergalė įstrižainėje."""
        self.game.make_move(0, 0, "X")
        self.game.make_move(1, 1, "X")
        self.game.make_move(2, 2, "X")
        self.assertTrue(self.game.check_winner("X"))

    def test_occupied_cell(self):
        """Patikrina, ar sistema neleidžia atlikti ėjimo į jau užimtą langelį."""
        self.game.make_move(1, 1, "X")
      
        result = self.game.make_move(1, 1, "O")
        self.assertFalse(result)
       
        self.assertEqual(self.game.get_board()[1][1], "X")

    def test_is_draw(self):
        """Patikrina, ar teisingai atpažįstamos lygiosios."""
        moves = [
            (0,0,"X"), (0,1,"O"), (0,2,"X"),
            (1,0,"X"), (1,1,"X"), (1,2,"O"),
            (2,0,"O"), (2,1,"X"), (2,2,"O")
        ]
        for r, c, s in moves:
            self.game.make_move(r, c, s)
        self.assertTrue(self.game.is_draw())

if __name__ == '__main__':
    unittest.main()