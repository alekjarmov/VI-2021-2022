from constraint import *


def same(a, b, c):
    return (a + b) % 10 == c


def oneOff(a, b, c,prev1,prev2):
    if prev1+prev2>=10:
        return (a+b+1)%10==c
    else:
        return (a+b)%10==c


def mconstaint(s, m):
    if s + m < 10:
        return m == 0
    else:
        return m == 1


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(same, ["D", "E", "Y"])
    problem.addConstraint(AllDifferentConstraint())
    problem.addConstraint(oneOff, ["N", "R", "E","D","E"])
    problem.addConstraint(oneOff, ["E", "O", "N","N","R"])
    problem.addConstraint(oneOff, ["S", "M", "O","E","O"])
    problem.addConstraint(mconstaint, ["S", "M"])
    # ----------------------------------------------------
    [dict(sorted(solution.items())) for solution in problem.getSolutions()]
    print(dict(sorted(problem.getSolution().items())))
