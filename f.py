d, c, r = map(int, (input().split()))

val = d
cansativa = []
revigorante = []

for cc in range(c):
    x = int(input())
    cansativa.append(x)

for rr in range(r):
    x = int(input())
    revigorante.append(x)


ativ = 0

can = len(cansativa)
rev = len(revigorante)

cn = 0
rn = 0

for n in range(can + rev):
    if cn < can:
        if val >= cansativa[cn]:
            val -= cansativa[cn]

            cn += 1
            ativ += 1

    elif cn >= can:
        ativ += len(revigorante[rn:])
        break

    if rn < rev:
        val += revigorante[rn]

        rn += 1
        ativ += 1


print(ativ)
