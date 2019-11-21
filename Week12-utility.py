#   https://github.com/tommywilliams2001/csci-week12.git
#   Tommy Williams
#  ​CSCI 102 – Section E
#   Week 12 - Part B

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

def Union(list1, list2):
    list3 = list1 + list2
    list4 = list(dict.fromkeys(list3))
    return list4

def Intersection(list1, list2):
    list = []
    for name in list1:
        if name in list2:
            list.append(name)
    return list

def Notin(list1, list2):
    list = []
    for name in list1:
        if name not in list2:
            list.append(name)
    return list

