hrs = input("Ënter Hours:")
h = float(hrs)
rate = input("Enter Rates:")
if (h > 40):
    extravalue = (h - 40) * (1.5 * float(rate))
    value = 40 * float(rate)
else:
    value = h * float(rate)
try:
    pay = value + extravalue
except:
    pay = value
print(pay)

    