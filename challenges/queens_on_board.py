""" solves https://www.hackerrank.com/challenges/queens-on-board """

def print_grid(grid):
    """ display a grid """
    row = len(grid)
    if row == 0:
        print 'empty grid'
        return
    for row in grid:
        for itm in row:
            print itm,
            print ' ',
        print '\n'


def create_grid(row, col):
    """ creates and empty grid of row * col """
    grid = []
    for _ in range(row):
        row_i = ['.'] * col
        grid.append(row_i)

    return grid

QUEEN = 'Q'
BLOCK = '#'

def insert_items(item):
    """ inserts items at given positions """
    def inner(grid, positions):
        """ inner fun """
        for row, col in positions:
            grid[row][col] = item
    return inner

insert_queens = insert_items(QUEEN)
insert_blocks = insert_items(BLOCK)


grid = create_grid(3, 3)

def place_qn_at(grid, pos):
    """ places queen at the position if possible """

