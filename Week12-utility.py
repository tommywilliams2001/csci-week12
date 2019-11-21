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

def UpdateString(string1, string2, index):
    list = []
    for char in string1:
        list.append(char)
    list[index] = string2
    string = ''.join(list)
    print('OUTPUT', string)

def FindWordCount(list, string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    word_count = 0
    for line in list:
        for word in line.split():
            no_punct = ''
            for char in word:
                if char not in punctuations:
                    no_punct = no_punct + char
            if no_punct == string:
                word_count += 1
    return word_count

def ScoreFinder(players, scores, name):
    index = 'x'
    for i, item in enumerate(players):
        print(players[i])
        if item.lower() == name.lower():
            index = i
    if index == 'x':
        print('OUTPUT player not found')
    else:
        print('OUTPUT {} got a score of {}'.format(name, scores[index]))

