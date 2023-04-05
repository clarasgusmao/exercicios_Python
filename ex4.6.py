def computepay(h, r):
    if (float(h) > 40):
        extravalue = (float(h) - 40) * (1.5 * float(rate))
        value = 40 * float(rate)
    else:
        value = float(h) * float(rate)
    try:
        pay = value + extravalue
    except:
        pay = value
    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
p = computepay(hrs,rate)
print("Pay", p)