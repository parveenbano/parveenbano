question_list = [["How many continents are there?"],
["What is the capital of India?"],
["NG mei kaun se course padhaya jaata hai?"]]

options_list = [
["Four", "Nine", "Seven", "Eight"],
["Chandigarh", "Bhopal", "Chennai", "Delhi"],
["Software Engineering", "Counseling", "Tourism", "Agriculture"]]


# har ek question ke liye, uski solution key (yeh index nahi hai)
# solution_list = [3, 4, 1]

solution_list = [3, 4, 1]
life_line =[1,3],[2,4],[1,2]
money =[2000,4000,8000]
i=0
sum=0
count=0
while i<len(question_list):
    print(i+1,question_list[i])
    j=0
    while j<len(options_list):
        print(j+1,options_list[i][j])
        j=j+1
    if count<1:
        print("oho_do you want life line")
        s= str(input("enter the number"))
        if s==("yes"):
           count+=1
           print("life line[i]")
        else:
            print("you already used life line")
            n=int(input("enter the answer"))
            if n==solution_list[i]:
              sum=sum+money
              print("your answer is correct",sum)
            else:
                print("your answer is wrong game is over",sum)
                break
            i=i+1









