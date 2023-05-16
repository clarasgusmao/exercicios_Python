# Find who has sent the most e-mails and how many there were in an mbox file

fname = input("Enter file name: ")
fhandle = open(fname)
wordsinline = list()
sender = list()

# Creating a list of senders
for line in fhandle:
    line = line.rstrip()
    if line.startswith('From '):
        wordsinline = line.split()
        sender.append(wordsinline[1])

# Create histogram
histogram = {}
for key in sender:
    histogram[key] = histogram.get(key,0) + 1

# Find the most common sender and how many e-mails they sent
bigsender = None
bigvalue = None
for sender,value in histogram.items():
    if bigvalue is None or value > bigvalue:
        bigvalue = value
        bigsender = sender

print(bigsender,bigvalue)
