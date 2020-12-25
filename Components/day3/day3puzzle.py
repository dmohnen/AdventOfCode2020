def replicate(value, replicationfactor):
    return value.strip('\n') * replicationfactor


def buildlist():
    listofrecords = list()
    recordlist = open('../../resources/map.txt')
    lengthofrecord = len(recordlist.readline()) - 1
    recordlist.close()
    recordlist = open('../../resources/map.txt')
    filesegment = (lengthofrecord // 7)
    linenumber = 0
    list1 = list()
    for x in recordlist:
        print(x)
        linenumber += 1
        replication = linenumber // filesegment
        list1.append(replicate(x, replication + 1))
    return list1


def treecounter(list1, xslope, yslope):
    x_pos = int(0)
    y_pos = int(0)
    treecount = 0
    nontreecount = 0
    listlength = len(list1)

    while y_pos < listlength:
        stringtocheck = list1[int(y_pos)]
        treeposition = stringtocheck[x_pos:x_pos + 1]
        if treeposition == '#':
            treecount += 1
        else:
            nontreecount += 1
        x_pos += xslope
        y_pos += yslope
    return treecount


def main():
    mainlist = buildlist()
    ans1_1 = treecounter(mainlist, 1, 1)
    print(ans1_1)
    ans3_1 = treecounter(mainlist, 3, 1)
    print(ans3_1)
    ans5_1 = treecounter(mainlist, 5, 1)
    print(ans5_1)
    ans7_1 = treecounter(mainlist, 7, 1)
    print(ans7_1)
    ans1_2 = treecounter(mainlist, 1, 2)
    print(ans1_2)
    print(ans1_1*ans1_2*ans3_1*ans5_1*ans7_1)


if __name__ == "__main__":
    main()
