import json
# here we import the data from the json file ,first we open the file read the content and then loads the content using json method.
with open("question.json", "r") as file:
    content = file.read()
data = json.loads(content)

# now we need to use the data to print its contents
for questions in data:
    co_count =0
    print(questions["questions"])
    for index , alternative in enumerate(questions["alternatives"]):
        print(index + 1,"-" ,alternative)

    user_choice = int(input("enter your answer : "))
    questions["user_choice"] = user_choice
    if questions["user_choice"] == questions["ans"]:
        #print("correct answer")
        co_count += 1
    #else:
        #print("wrong answer")
for i,j in enumerate(data):
    print(f"{i+1} - your answer is: {j['user_choice']} ,correct answer is : {j['ans']} ")

print(f"score : {co_count}")
# Yes, %A extracts the current day and %a extracts the abbreviation of the current day (i.e., Wed).