from constraint import *
import itertools


def diff(termin1, termin2):
    t1 = termin1.split("_")
    t2 = termin2.split("_")
    # print(f"{t1} {t2}")
    if (t1[0] == t2[0]) and abs(int(t1[1]) - int(t2[1])) < 2:
        return False
    return True


def mle(m1, m2):
    t1 = m1.split("_")
    t2 = m2.split("_")
    # print(f"{t1[1]} {t2[1]}")
    # print(f"{t1} {t2}")
    if t1[1] == t2[1]:
        return False
    return True


def check_valid(t1, t2):
    return (t1[:3] != t2[:3]) or (abs(int(t1[-2:]) - int(t2[-2:])) >= 2)


def check_valid_ml(t1, t2):
    return (t1[-2:] != t2[-2:])

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = int(input())
    casovi_ML = int(input())
    casovi_R = int(input())
    casovi_BI = int(input())

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Tuka dodadete gi promenlivite--------------------
    allvariables = []
    ai = []
    for i in range(casovi_AI):
        ai.append(f"AI_cas_{i + 1}")
        problem.addVariable(f"AI_cas_{i + 1}",AI_predavanja_domain)
        allvariables.append(f"AI_cas_{i + 1}")
    #problem.addVariables(ai, AI_predavanja_domain)

    ml = []
    for i in range(casovi_AI):
        ml.append(f"ML_cas_{i + 1}")
        problem.addVariable(f"ML_cas_{i + 1}",ML_predavanja_domain)
        allvariables.append(f"ML_cas_{i + 1}")
    #problem.addVariables(ml, ML_predavanja_domain)

    r = []
    for i in range(casovi_AI):
        r.append(f"R_cas_{i + 1}")
        problem.addVariable(f"R_cas_{i + 1}",R_predavanja_domain)
        allvariables.append(f"R_cas_{i + 1}")
    #problem.addVariables(r, R_predavanja_domain)

    bi = []
    for i in range(casovi_AI):
        bi.append(f"BI_cas_{i + 1}")
        problem.addVariable(f"BI_cas_{i + 1}",BI_predavanja_domain)
        allvariables.append(f"BI_cas_{i + 1}")
    #problem.addVariables(bi, BI_predavanja_domain)

    problem.addVariable("AI_vezbi", AI_vezbi_domain)
    problem.addVariable("ML_vezbi", ML_vezbi_domain)
    # print(ML_vezbi_domain)
    problem.addVariable("BI_vezbi", BI_vezbi_domain)
    allvariables.append("AI_vezbi")
    allvariables.append("ML_vezbi")
    allvariables.append("BI_vezbi")
    ml.append("ML_vezbi")

    for c in itertools.combinations(allvariables, 2):
        problem.addConstraint(check_valid, c)

    for c in itertools.combinations(ml, 2):
        problem.addConstraint(check_valid_ml, c)
    # print(problem._variables)

    # ---Tuka dodadete gi ogranichuvanjata----------------
    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)