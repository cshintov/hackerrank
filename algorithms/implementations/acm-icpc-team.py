""" solves https://www.hackerrank.com/challenges/acm-icpc-team """

def read_strings(num):
    """ strings """
    for _ in range(num):
        yield raw_input()


def num_lines(num):
    """ read lines of numbers """
    for line in read_strings(num):
        yield map(int, line.strip().split())


def read_matrix(row):
    """ read a matrix of four rows """
    rows = read_strings(row)
    return [[int(c) for c in row_] for row_ in rows]


def find_teams(people):
    """ finds the possible teams """
    teams = []
    for person in range(people-1):
        teams.extend([
            (person, person_b)
            for person_b in range(person+1, people)
        ])
    return teams


def acm_icpc_team(teams, knowledge_grid):
    """ 
    find the maximum number of topics any team can know 
    and the number of teams that knows that many topics
    """ 
    def knowledge(team):
        """ calculate knowledge of a team """
        pers_a, pers_b = team
        pers_a_knows = [
                topic for topic, knows in enumerate(knowledge_grid[pers_a]) if knows
            ]
        pers_b_knows = [
                topic for topic, knows in enumerate(knowledge_grid[pers_b]) if knows
            ]
        return len(set(pers_a_knows + pers_b_knows))

    knowledge = [knowledge(team) for team in teams]
    max_knowledge = max(knowledge)

    return max_knowledge, knowledge.count(max_knowledge)



def solve():
    """ solve it """
    inputs = num_lines(1)
    people, topics = next(inputs)
    knowledge_grid = read_matrix(people)
    teams = find_teams(people)
    num_topics, num_teams = acm_icpc_team(teams, knowledge_grid)
    print num_topics
    print num_teams


solve()
