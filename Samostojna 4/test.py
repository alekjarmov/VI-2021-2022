from constraint import *

if __name__ == '__main__':
    team_members_n = int(input())

    team_members = {}
    team_members_weights = []
    for i in range(0, team_members_n):
        line = input()
        parts = line.split(" ")
        weight = float(parts[0])
        member = parts[1]
        team_members[weight] = member
        team_members_weights.append(weight)

    team_leaders_n = int(input())

    team_leaders = {}
    team_leaders_weights = []
    for i in range(0, team_leaders_n):
        line = input()
        parts = line.split(" ")
        weight = float(parts[0])
        member = parts[1]
        team_leaders[weight] = member
        team_leaders_weights.append(weight)

    problem_members = Problem()
    print(team_members_weights)
    problem_members.addVariables(range(1, 6), team_members_weights)
    problem_members.addVariables([6], team_leaders_weights)
    problem_members.addConstraint(MaxSumConstraint(100))
    problem_members.addConstraint(AllDifferentConstraint())
    sol_combos = problem_members.getSolutions()
    max_sum = -1
    combo = []

    for combination in sol_combos:
        sum_tmp = 0
        for x in combination:
            sum_tmp += combination[x]
        if 100 >= sum_tmp > max_sum:
            max_sum = max(sum_tmp, max_sum)
            combo = combination

    print(combo)
    print(f"Total score: {max_sum}")
    # print(combo)
    print(f"Team leader: {team_leaders[combo[6]]}")
    for i in range(1, 6):
        print(f"Participant {i}: {team_members[combo[i]]}")
