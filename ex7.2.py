fname = input("Enter file name: ")
fh = open(fname)
counter = 0
soma = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        zeropos = line.find('0')
        number = line[zeropos:]
        fnumber = float(number)
        soma = soma + fnumber
        counter = counter + 1
print("Average spam confidence:", soma/counter) 