import itertools


def get_zbir(m):
    rec = dict()
    rec["P(T=1)"] = 0.02
    rec["P(T=0)"] = 0.98

    rec["P(R=1)"] = 0.1
    rec["P(R=0)"] = 0.9

    rec["P(G=1)"] = 0.002
    rec["P(G=0)"] = 0.998

    rec["P(A=1|U=1,G=1)"] = 1
    rec["P(A=1|U=1,G=0)"] = 1
    rec["P(A=1|U=0,G=1)"] = 1
    rec["P(A=1|U=0,G=0)"] = 0

    rec["P(A=0|U=1,G=1)"] = 0
    rec["P(A=0|U=1,G=0)"] = 0
    rec["P(A=0|U=0,G=1)"] = 0
    rec["P(A=0|U=0,G=0)"] = 1

    rec["P(U=1|T=1,R=1)"] = 0.5
    rec["P(U=1|T=1,R=0)"] = 0.999
    rec["P(U=1|T=0,R=1)"] = 0.2
    rec["P(U=1|T=0,R=0)"] = 0.001

    rec["P(U=0|T=1,R=1)"] = 0.5
    rec["P(U=0|T=1,R=0)"] = 0.001
    rec["P(U=0|T=0,R=1)"] = 0.8
    rec["P(U=0|T=0,R=0)"] = 0.999

    nums = [rec[i] for i in get_uslovna_niza(m)]
    return ("*".join(map(str, nums)))


def get_uslovna_niza(m):
    return get_uslovna(m).split("*")


def get_uslovna(m):
    return (
        f"P(R={m['R']})*P(T={m['T']})*P(G={m['G']})*P(A={m['A']}|U={m['U']},G={m['G']})*P(U={m['U']}|T={m['T']},R={m['R']})")


if __name__ == "__main__":
    print("+".join(f"P(A=1,G=0,R=0,U={x},T={y})" for x, y in itertools.product([0, 1], repeat=2)),end="=\n")
    uslovni = []
    zbirni = []
    for x, y in itertools.product([0, 1], repeat=2):
        mapa = dict()
        mapa["A"] = 1
        mapa["T"] = y
        mapa["R"] = 0
        mapa["U"] = x
        mapa["G"] = 0
        uslovni.append(get_uslovna(mapa))
        zbirni.append(get_zbir(mapa))
    joiner = "+\n+"
    print(f'={joiner.join(uslovni)}=')
    print(f'={joiner.join(zbirni)}=')
    sums = [eval(x) for x in zbirni]
    print(f"={sum(sums)}")
