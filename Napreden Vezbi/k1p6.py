from constraint import *
import itertools


def diff(a, b):
    return a != b


if __name__ == '__main__':
    problem = Problem(globals()[input()]())
    variables = range(81)
    domain = range(1, 10)
    problem.addVariables(variables, domain)
    for el in itertools.combinations(variables, 2):
        x, y = el
        if x // 9 == y // 9:
            problem.addConstraint(diff, (x, y))
        elif x % 9 == y % 9:
            problem.addConstraint(diff, el)

    for trired in range(3):
        for kvadrat in range(3):
            diffs = []
            for red in range(3):
                for kolona in range(3):
                    diffs.append(trired * 27 + red * 9 + 3*kvadrat + kolona)
            print(diffs)
            problem.addConstraint(AllDifferentConstraint(), diffs)
    print(problem.getSolution())
