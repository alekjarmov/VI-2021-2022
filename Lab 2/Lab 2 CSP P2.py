import itertools

from constraint import *

termini = dict()


def marijasimona(marija, simona, vreme):
    if marija != simona:
        return True
    return vreme in termini["Marija_prisustvo"] and vreme in termini["Simona_prisustvo"]


def petarsimona(mem1, mem2, vreme):
    if mem1 != mem2:
        return True
    return vreme in termini["Petar_prisustvo"] and vreme in termini["Simona_prisustvo"]


def petarmarija(mem1, mem2, vreme):
    if mem1 != mem2:
        return True
    return vreme in termini["Marija_prisustvo"] and vreme in termini["Simona_prisustvo"]


def petar(mem1, vreme):
    if (mem1 == 0):
        return True
    return vreme in termini["Petar_prisustvo"]


def marija(mem1, vreme):
    if (mem1 == 0):
        return True
    return vreme in termini["Marija_prisustvo"]


def simona(mem1, vreme):
    if (mem1 == 0):
        return True
    return vreme in termini["Simona_prisustvo"]


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----

    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("Simona_prisustvo", [1])
    problem.addVariable("Marija_prisustvo", [0, 1])

    problem.addVariable("vreme_sostanok", [i for i in range(12, 21)])
    prisustva = ["Marija_prisustvo", "Simona_prisustvo", "Petar_prisustvo"]
    vreme = ["vreme_sostanok"]

    termini["Simona_prisustvo"] = (13, 14, 16, 19)
    termini["Marija_prisustvo"] = (14, 15, 18)
    termini["Petar_prisustvo"] = (12, 13, 16, 17, 18, 19)

    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(MinSumConstraint(2), prisustva)

    # print(prisustva[0:2] + vreme)
    # print([prisustva[2], prisustva[0]] + vreme)
    # print(prisustva[1:3] + vreme)
    # problem.addConstraint(petarmarija, [prisustva[2], prisustva[0]] + vreme)
    # problem.addConstraint(marijasimona, prisustva[0:2] + vreme)
    # problem.addConstraint(petarsimona, prisustva[1:3] + vreme)
    problem.addConstraint(simona, [prisustva[1]] + vreme)
    problem.addConstraint(petar, [prisustva[2]] + vreme)
    problem.addConstraint(marija, [prisustva[0]] + vreme)

    # ----------------------------------------------------
    solutions = problem.getSolutions()
    solutions.sort(key=lambda d:d['Petar_prisustvo'])
    # [print(solution) for solution in problem.getSolutions()]
    # [print(solution) for solution in problem.getSolutions()]

    for solution in solutions:
        print(f"{'{'}'Simona_prisustvo': {solution['Simona_prisustvo']}, 'Marija_prisustvo': {solution['Marija_prisustvo']}, 'Petar_prisustvo': {solution['Petar_prisustvo']}, 'vreme_sostanok': {solution['vreme_sostanok']}{'}'}")
