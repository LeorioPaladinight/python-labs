e = int(input())
phi = int(input())
prine = e
prinphi = phi
repeat = 0
bufrotd = e % phi
bufiotd = e // phi
zero = 0
brotd = e % phi
print(e, phi, )
ad = 0
ab = [0, 0, 0, 0]
g = 1
while brotd != 0:
    rotd = e % phi
    if zero == e // phi:
        break
    iotd = e // phi
    ab[ad] = iotd
    ad += 1
    print(e, phi, rotd, iotd)
    e = phi
    phi = rotd
    repeat += 1  # <------------ И ТУТА
    brotd = rotd
ad = 2
print(repeat, "Repeats")
x = 0
y = 1
buffp = 1
buffe = prine
buffphi = prinphi
print("xxxxxxxxxx")
repeat -= 1
x = [0, 0, 0, 0]
y = [1, 0, 0, 0]
while repeat >= 0:  # <-------- ВОТ ТУТА
    while buffp <= repeat:
        buffrotd = buffe % buffphi
        buffiotd = buffe // buffphi
        if buffp == 1:
            buffp += 1
            continue
        if buffrotd == zero:
            break
        buffe = buffphi
        buffphi = buffrotd
        if zero == buffe // buffphi:
            break
        buffp += 1
    x[g] = y[g-1]
    y[g] = x[g-1] - y[g-1] * ab[ad]
    if ad == 0:
        ad = 1
    ad -= 1
    g += 1
    if buffe == 0 or buffphi == 0:
        break
    repeat -= 1  # <----------ТУТА
    print(x, "\n", y, "\n")
    # e - It's A
    # phi - It's B
    # rotd - It's A mod B
    # iotd - It's A / B
