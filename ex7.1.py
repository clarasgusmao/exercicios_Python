fname = input("Enter file name: ")
fh = open(fname)
text = fh.read()
print(text.rstrip().upper())