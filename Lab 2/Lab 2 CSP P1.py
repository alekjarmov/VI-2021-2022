from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    n = int(input())
    domparticipants = [list(input().split(" ")) for _ in range(n)]
    m = int(input())
    domleaders = [list(input().split(" ")) for _ in range(m)]
    dictmembers = dict()

    for i in domparticipants:
        i[0] = float(i[0])
        dictmembers[i[0]] = i[1]
    for i in domleaders:
        i[0] = float(i[0])
        dictmembers[i[0]] = i[1]
    members = [f"Participant {i + 1}" for i in range(5)]
    leader = ["Team leader"]
    domainleader = [l[0] for l in domleaders]
    domainvariables = [l[0] for l in domparticipants]

    problem.addVariables(leader, domainleader)
    problem.addVariables(members, domainvariables)
    problem.addConstraint(MaxSumConstraint(100))
    problem.addConstraint(AllDifferentConstraint())

    solutions = problem.getSolutions()
    score = 0
    # print(len(solutions))problem.addConstraint(MaxSumConstraint(100))
    solution = None
    for sol in solutions:
        newscore = sum(v for k, v in sol.items())
        if newscore <= 100:
            if newscore > score:
                #print(newscore)
                score = newscore
                solution = sol
    #print(solution)
    print(f"Total score: {score:.1f}")
    print(f"Team leader: {dictmembers[solution['Team leader']]}")
    for key, value in solution.items():
        if (key != "Team leader"):
            print(f"{key}: {dictmembers[value]}")
