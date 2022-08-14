from constraint import *
import itertools


def no_attack(a, b):
    if a[0] == b[0] or a[1] == b[1]:
        return False
    if abs(a[0] - b[0]) == abs(a[1] - b[1]):
        return False
    return True


if __name__ == '__main__':
    num = int(input())

    problem = Problem(BacktrackingSolver())
    domain = list(itertools.product(range(num), repeat=2))
    variables = range(1, num + 1)
    problem.addVariables(variables, domain)

    for el in itertools.permutations(variables, 2):
        problem.addConstraint(no_attack, el)

    if num > 6:
        print(problem.getSolution())
    else:
        print(len(problem.getSolutions()))
