""" solve lisa's workbook problem """

def read_strings(num):
    """ read lines of input """
    for _ in range(num):
        yield raw_input()


def num_lines(num):
    """ read lines of numbers """
    for line in read_strings(num):
        yield [int(numb) for numb in line.split()]


def group(lst, count):
    """ group elements of a list in groups of count size """
    return [lst[start: start + count] for start in range(0, len(lst), count)]


def workbook(max_count_prob, prob_counts):
    """ lisa's workbook problem distribution """
    pages = []
    for problems in prob_counts:
        pages.extend(group(range(1, problems+1), max_count_prob))

    return pages


def count_special_problems(work_book):
    """ count special problems """
    count = 0
    for page, problems in enumerate(work_book, start=1):
        if page in problems:
            count += 1
    return count


def solve():
    """ solves the problem """
    input_lines = list(num_lines(2))
    _, val_k = input_lines[0]
    problem_counts = input_lines[1]
    return count_special_problems(workbook(val_k, problem_counts))


if __name__ == '__main__':
    print solve()
