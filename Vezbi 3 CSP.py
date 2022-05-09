import itertools

from constraint import *

globaln = 0


def noattack(q1, q2):
    x1 = q1[0]
    y1 = q1[1]
    x2 = q2[0]
    y2 = q2[1]
    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return False
    return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    n = int(input())
    globaln = n
    variables = [i + 1 for i in range(n)]
    domain = [i for i in itertools.product(range(n), repeat=2)]
    #print(domain)
    problem.addVariables(variables, domain)

    for i, q1 in enumerate(variables):
        for j, q2 in enumerate(variables):
            if j < i:
                problem.addConstraint(noattack, (q1, q2))

    # ---Tuka dodadete gi ogranichuvanjata----------------

    # ----------------------------------------------------
    if n <= 6:
        print(len(problem.getSolutions()))

    else:
        print(problem.getSolution())
