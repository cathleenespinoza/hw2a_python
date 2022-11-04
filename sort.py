

def sort_dictionary(myDict):
    sortedByAge = sorted(myDict.items(), key= lambda v: v[1][1])
    names = []
    phoneNums = []
    for i in sortedByAge:
        names.append(i[0])
        phoneNums.append(i[1][0])
    namesPhoneNums = list(zip(names, phoneNums))
    return namesPhoneNums

