import curses

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """Отобразить рамку."""
        screen.border()

    def draw_grid(self, screen) -> None:
        """Отобразить состояние клеток."""
        height, width = screen.getmaxyx()
        max_rows = min(self.life.rows, height - 2)
        max_cols = min(self.life.cols, width - 2)
        for i in range(max_rows):
            row_str = ""
            for j in range(max_cols):
                if self.life.curr_generation[i][j] == 1:
                    row_str += "*"
                else:
                    row_str += " "
            if i + 1 < height - 1:
                screen.addstr(i + 1, 1, row_str)

    def run(self) -> None:
        screen = curses.initscr()
        try:
            screen.nodelay(True)
            screen.timeout(500)
            while True:
                screen.clear()
                self.draw_borders(screen)
                self.draw_grid(screen)
                screen.addstr(0, 2, f"Gen: {self.life.generations}")
                screen.addstr(0, 40, "Press 'q' to quit")
                screen.refresh()
                self.life.step()
                if screen.getch() in (ord("q"), ord("Q"), 27):
                    break
        finally:
            curses.endwin()
