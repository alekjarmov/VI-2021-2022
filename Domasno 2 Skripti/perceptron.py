import random

def product(w, f):
    return sum(x * y for x, y in zip(w, f))

def get_sub(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans(''.join(normal), ''.join(sub_s))
    return x.translate(res)


class Format:
    end = '\033[0m'
    underline = '\033[4m'
data = [[-1, -1, -1, -1]
    , [-1, -1, 1, 1]
    , [-1, 1, -1, -1]
    , [-1, 1, 1, 1]
    , [1, -1, -1, -1]
    , [1, -1, 1, +1]
    , [1, 1, -1, -1]
    , [1, 1, -1, +1]
    , [2, -1, 1, +1]
    , [2, 1, 1, -1]
        ]
karakteristiki = [a[:-1] for a in data]
actual = [a[-1] for a in data]
w = [1, -1, 2, 1]
mapa = dict()
mapa[-1] = "негативна"
mapa[1] = "позитивна"
for i, f in enumerate(karakteristiki):
    adjusted_f = [1] + f
    predicted = 1 if product(w, f) >= 0 else -1
    real = actual[i]
    print(f"{Format.underline}Примерок {i+1}:{Format.end} 𝑓(x)={adjusted_f}, w{get_sub(str(i+1))}={w}, y*={real}  ")
    print(f"𝑓(x)*w{get_sub(str(i+1))} = {adjusted_f}*{w} = {product(w,adjusted_f)}{' ≥ 0' if product(w, adjusted_f) >= 0 else ' < 0'}")
    print(f"Вистинската класа е {mapa[real]}{', додека пак' if real != predicted else ' и'} предвидената класа е {mapa[predicted]}.", end=" ")
    if real == predicted:
        print(f"{'Бидејќи'if random.randint(1,2) == 1 else 'Со оглед на тоа што'} предвидената класа се совпаѓа со вистинската класа нема промена во векторот на тежини.")
    else:
        print("Поради тоа што предвидената класа вистинската класа не се совпаѓаат соодветно се ажурира векторот на тежини.")
        w = [w[i] + real * adjusted_f[i] for i in range(len(w))]
        print(f"w←w+y'*𝑓 = w+({real})*𝑓 = {w}")
    # print()
print(f"Со десетиот примерок завршува првата епоха. По завршување на првата епоха го добиваме следниов вектор на тежини w={w}")