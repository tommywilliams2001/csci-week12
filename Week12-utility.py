#   YOUR GITHUB REPO
#   Tommy Williams
#  ​CSCI 102 – Section E
#   Week 12 - Part A

def PrintOutput(string):
    print('OUTPUT', string)

def LoadFile(file):
    with open(file, 'r') as text:
        list = []
        lines = text.readlines()
        for line in lines:
            list.append(line.rstrip('\n'))
    return list

print(LoadFile('./text.txt'))