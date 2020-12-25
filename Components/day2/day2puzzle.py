import pandas as pd


def splitcolumn1(values):
    return [int(x) for x in values.split("-")]

def chartoevaluate(stringtoevaluate):
    return stringtoevaluate[0:1]

def countofcharsinpassword(chartocount, password):
    return password.count(chartocount)


def passwordpolicy2(password, char2find, pos1, pos2):
    if pos1-1 <= len(password) and pos2-1 <= len(password):

        if char2find == password[pos1-1] and char2find == password[pos2-1]:
            return False

        if char2find == password[pos1-1] and char2find != password[pos2-1]:
            return True

        if char2find != password[pos1-1] and char2find == password[pos2-1]:
            return True

        if char2find != password[pos1-1] and char2find != password[pos2-1]:
            return False


def checkpasswordpolicy():
    df = pd.read_table("../../resources/passwords.txt", index_col=0, header=None)
    passwordcounted = 0
    passwordpol2 = 0
    for row in df.iterrows():
        array1 = row[0].split(sep=' ')
        minmax = splitcolumn1(array1[0])
        chartocheck = chartoevaluate(array1[1])
        password = array1[2]
        countofchar = countofcharsinpassword(chartocheck, password)
        if (passwordpolicy2(password, chartocheck, minmax[0], minmax[1])):
            passwordpol2 += 1
        if (countofchar >= minmax[0]) and (countofchar <= minmax[1]):
            passwordcounted += 1
        print(passwordcounted)

    print(passwordpol2)


if __name__ == "__main__":
    checkpasswordpolicy()
