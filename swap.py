
def swap_list(mylist):
    if not mylist:
        return mylist
    else:
        mid = (len(mylist) - 1) / 2
        temp = mylist[int(mid)]
        mylist[int(mid)] = mylist[-1]
        mylist[-1] = temp
        return mylist

