digit_names = ["zero","one","two","three","four","five","six","seven","eight","nine"]
def main(input):
    lines = input.splitlines()
    total1 = 0
    total2 = 0
    for line in lines:

        digits =[char for char in line if char.isnumeric()]
        if digits:
            total1 += int(digits[0]+digits[-1])
        digits = [char for char in translate(line) if char.isnumeric()]
        total2 += int(digits[0]+digits[-1])
        print(total2,total2)
        total3 =total1+total2
    print(total3)
def translate(line):
    for num,name in enumerate(digit_names):
        line.replace(name,f"{name}{num}{name}")
    return line

with open("text.txt","r") as file:

    for line in file:
        main(line)

