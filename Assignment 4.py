def computepay(h,r):
    if h <= 40:
        pay = h * r
    else:
        pay = (40 * r) + ((h - 40) * (1.5 * r))
    return pay
hrs = input("Enter Hours:")
h = float(hrs)
rph = input("Enter Rate")
r = float(rph)
p = computepay(h,r)
print(p)
