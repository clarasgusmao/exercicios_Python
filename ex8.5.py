fname = input("Enter file name: ")
fhandle = open(fname)
count = 0
lst = list()
for line in fhandle:
    line = line.rstrip()
    if line.startswith('From'):
        if not line.startswith('From:'):
            lst = line.split()
            print(lst[1])
            count = count + 1
print("There were", count, "lines in the file with From as the first word")

#if len(fname) < 1:
#    fname = "mbox-short.txt"

#fh = open(fname)
#count = 0

#print("There were", count, "lines in the file with From as the first word")