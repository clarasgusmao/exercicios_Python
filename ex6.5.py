text = "X-DSPAM-Confidence:    0.8475"
zeropos = text.find('0')
number = text[zeropos:]
fnumber = float(number)
print(number)