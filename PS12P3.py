def loadarrays(lname3, score):
    with open("myfile.txt", "r") as f:
        for i in range(0, 5):
            lname = f.readline().strip()
            if lname:  
                lname3.append(lname)
            else:
                break  
            scr = f.readline().strip()
            if scr:  
                score.append(int(float(scr)))  
            else:
                break  

def darrays(lname3, score):
    for i in range(len(lname3)):
        print(lname3[i], "has a score of", score[i])

lname3 = []
score = []
loadarrays(lname3, score)
darrays(lname3, score)
def find_highest_lowest(lname3, score):
    high_index = score.index(max(score))
    low_index = score.index(min(score))
    print("            ")
    print(lname3[high_index], "has the highest score of", score[high_index])
    print(lname3[low_index], "has the lowest score of", score[low_index])
find_highest_lowest(lname3, score)

