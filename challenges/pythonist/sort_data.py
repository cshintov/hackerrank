def read_line():
    return raw_input().split()


def read_row():
    return [int(n) for n in read_line()]


def read_table(rows):
    for row in range(rows):
        yield read_row()


def print_table(table):
    for row in table:
        for col in row:
            print col,

        print


def sort_by_column(table, column=0):
    """ sort based on a column """
    return sorted(table, key=lambda row: row[column])


if __name__ == '__main__':
    rows, cols = read_row()
    table = list(read_table(rows))
    column = int(raw_input())

    print_table(sort_by_column(table, column))
