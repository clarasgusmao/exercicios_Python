score = input("Enter Score:")
try:
    fscore = float(score) * 100
    iscore = int(fscore)
except:
    print("Please enter a numerical value")
    quit()
if fscore < 0 or fscore > 100:
    print("Please enter a score between 0.0 and 1.0.")
    quit()
elif fscore < 60:
    print ("F")
elif fscore >= 60 and fscore < 70:
    print("D")
elif fscore >= 70 and fscore < 80:
    print("C")
elif fscore >= 80 and fscore < 90:
    print("B")
elif fscore >= 90:
    print("A")