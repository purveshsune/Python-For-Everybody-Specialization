hrs = input("Enter Hours:")
h = float(hrs)
rph = input("Enter Rate per Hour:")
rh = float(rph)
if(h <= 40):
    pay=h * rh
else:
    pay = (40 * rh) + ((h-40) * (rh * 1.5))
print(pay)
