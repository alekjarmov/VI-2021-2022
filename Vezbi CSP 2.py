import itertools

from constraint import *

n = 81
if __name__ == '__main__':
    str=input()
    if(str=="BacktrackingSolver"):
        problem = Problem(BacktrackingSolver())
    elif str== "RecursiveBacktrackingSolver":
        problem = Problem(RecursiveBacktrackingSolver())
    else:
        problem = Problem(MinConflictsSolver())
    variables = [i for i in range(81)]
    # print(variables)

    domain = [i+1 for i in range(9)]
    problem.addVariables(variables,domain)
    # ---Tuka dodadete gi ogranichuvanjata----------------
    for i in range(9):
        lista = [9 * i + k for k in range(9)]
        lista2 = [i + 9 * k for k in range(9)]
        #print(lista)
        problem.addConstraint(AllDifferentConstraint(),lista)
        problem.addConstraint(AllDifferentConstraint(), lista2)
    for t in range(0,81,27):
        for  i in range(t,t+9,3):
            lista=[]
            for j in range (3):
                for k in range(3):
                    lista.append(i+9*k+j)
            #print(lista)
            problem.addConstraint(AllDifferentConstraint(),lista)
    # ----------------------------------------------------

    print(problem.getSolution())
