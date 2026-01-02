import random
from copy import deepcopy
from random import choice, randint
from typing import List, Optional, Tuple, Union

import pandas as pd


def create_grid(rows: int = 15, cols: int = 15) -> List[List[Union[str, int]]]:
    return [["■"] * cols for _ in range(rows)]


def remove_wall(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> List[List[Union[str, int]]]:
    """

    :param new_grid:
    :param coord:
    :return:
    """
    result = [row[:] for row in grid]
    row, col = coord
    direction = random.choice(["up", "right"])
    if direction == "right":
        if col + 2 < len(result[0]) and result[row][col + 1] == "■":
            result[row][col + 1] = " "
        elif row - 1 > 0 and result[row - 1][col] == "■":
            result[row - 1][col] = " "
    else:
        if row - 1 > 0 and result[row - 1][col] == "■":
            result[row - 1][col] = " "
        elif col + 2 < len(result[0]) and result[row][col + 1] == "■":
            result[row][col + 1] = " "

    return result


def bin_tree_maze(rows: int = 15, cols: int = 15, random_exit: bool = True) -> List[List[Union[str, int]]]:
    """

    :param rows:
    :param cols:
    :param random_exit:
    :return:
    """

    grid = create_grid(rows, cols)
    empty_cells = []
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if x % 2 == 1 and y % 2 == 1:
                grid[x][y] = " "
                empty_cells.append((x, y))

    # 1. выбрать любую клетку
    # 2. выбрать направление: наверх или направо.
    # Если в выбранном направлении следующая клетка лежит за границами поля,
    # выбрать второе возможное направление
    # 3. перейти в следующую клетку, сносим между клетками стену
    # 4. повторять 2-3 до тех пор, пока не будут пройдены все клетки
    for cell in empty_cells:
        grid = remove_wall(grid, cell)
    # генерация входа и выхода
    if random_exit:
        x_in, x_out = randint(0, rows - 1), randint(0, rows - 1)
        y_in = randint(0, cols - 1) if x_in in (0, rows - 1) else choice((0, cols - 1))
        y_out = randint(0, cols - 1) if x_out in (0, rows - 1) else choice((0, cols - 1))
    else:
        x_in, y_in = 0, cols - 2
        x_out, y_out = rows - 1, 1

    grid[x_in][y_in], grid[x_out][y_out] = "X", "X"

    return grid


def get_exits(grid: List[List[Union[str, int]]]) -> List[Tuple[int, int]]:
    """

    :param new_grid:
    :return:
    """
    exits = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == "X":
                exits.append((x, y))

    return exits


def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """

    :param new_grid:
    :param k:
    :return:
    """
    new_grid = deepcopy(grid)
    rows = len(new_grid)
    cols = len(new_grid[0])
    for i in range(rows):
        for j in range(cols):
            if new_grid[i][j] == k:
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for x, y in directions:
                    new_i, new_j = i + x, j + y
                    if 0 <= new_i < rows and 0 <= new_j < cols:
                        if new_grid[new_i][new_j] == 0:
                            new_grid[new_i][new_j] = k + 1

    return new_grid


def shortest_path(
    grid: List[List[Union[str, int]]], exit_coord: Tuple[int, int]
) -> Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]:
    """

    :param new_grid:
    :param exit_coord:
    :return:
    """
    new_grid = deepcopy(grid)
    x, y = exit_coord
    cell_value = new_grid[x][y]
    if isinstance(cell_value, int):
        k = cell_value
    elif isinstance(cell_value, str) and cell_value.isdigit():
        k = int(cell_value)
    else:
        return []
    expected_length = k
    path = [(x, y)]
    while k != 1:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i, j in directions:
            new_x, new_y = x + i, y + j
            if new_grid[new_x][new_y] == k - 1:
                path.append((new_x, new_y))
                k -= 1
                x, y = new_x, new_y
    if len(path) != expected_length:
        x, y = path[-1]
        new_grid[x][y] = " "
        shortest_path(new_grid, exit_coord)

    return path


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """

    :param new_grid:
    :param coord:
    :return:
    """
    rows = len(grid)
    cols = len(grid[0])
    x, y = coord
    if (x, y) in [(0, 0), (0, cols - 1), (rows - 1, 0), (rows - 1, cols - 1)]:
        return True
    if y == 0:
        if y + 1 < cols and grid[x][y + 1] != " ":
            return True
    if y == cols - 1:
        if y - 1 >= 0 and grid[x][y - 1] != " ":
            return True
    if x == 0:
        if x + 1 < rows and grid[x + 1][y] != " ":
            return True
    if x == rows - 1:
        if x - 1 >= 0 and grid[x - 1][y] != " ":
            return True
    return False


def solve_maze(
    grid: List[List[Union[str, int]]],
) -> Tuple[List[List[Union[str, int]]], Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]]:
    """

    :param new_grid:
    :return:
    """

    exits = get_exits(grid)
    if len(exits) < 2:
        return grid, exits
    entrance = exits[1]
    exit = exits[0]
    new_grid = deepcopy(grid)
    if encircled_exit(new_grid, exit):
        return new_grid, None
    for i in range(len(new_grid)):
        for j in range(len(new_grid[0])):
            if new_grid[i][j] == " ":
                new_grid[i][j] = 0
    new_grid[entrance[0]][entrance[1]] = 1
    new_grid[exit[0]][exit[1]] = 0
    k = 1
    while new_grid[exit[0]][exit[1]] == 0:
        new_grid = make_step(new_grid, k)
        k += 1
    way_back = shortest_path(new_grid, exit)
    if way_back is None:
        return new_grid, None
    result = way_back[::-1]

    return new_grid, result


def add_path_to_grid(
    grid: List[List[Union[str, int]]], path: Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]
) -> List[List[Union[str, int]]]:
    """

    :param new_grid:
    :param path:
    :return:
    """
    if path:
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if (i, j) in path:
                    grid[i][j] = "*"
    return grid


if __name__ == "__main__":
    print(pd.DataFrame(bin_tree_maze(15, 15)))
    GRID = bin_tree_maze(15, 15)
    print(pd.DataFrame(GRID))
    _, PATH = solve_maze(GRID)
    MAZE = add_path_to_grid(GRID, PATH)
    print(pd.DataFrame(MAZE))
