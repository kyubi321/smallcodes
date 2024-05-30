import re
dic = { "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}



def convert_spelled(input1, dicti):
    #sortedkeys = sorted(dicti.keys(),key=len,reverse=True)
    for word in sorted(dicti.keys(),key=lambda x: input1.find(x)):
        input1 = input1.replace(word,str(dicti[word]))
    return input1

def calliberate(input):

    print(input)
    new_string = convert_spelled(input,dic)
    print(new_string)

    string = re.findall(r'\d+',new_string)
    print(string)

    if string:
        int1 = string[0][0]
        int2 = string[-1][-1]

        sum1 = int1 + int2
        print(sum1)

        total.append(int(sum1))



with open("text.txt","r") as file:
    lines = file.readlines()
    total = []
    for line in lines:
        calliberate(line)

print(sum(total))
