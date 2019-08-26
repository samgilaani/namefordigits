numbers = []
numbers.append(["+"])
numbers.append(["#"])
numbers.append(["A","B","C"])
numbers.append(["D","E","F"])
numbers.append(["G","H","I"])
numbers.append(["J","K","L"])
numbers.append(["M","N","O"])
numbers.append(["P","Q","R","S"])
numbers.append(["T","U","V"])
numbers.append(["W","X","Y","Z"])

def chasb(ListA,ListB):
    ListC = []
    for i in ListA:
        for j in ListB:
            ListC.append(i+j)
    return ListC


def bechasb(ListN):
    ListN = [5,7,8,3]
    ListX = [""]

    for i in ListN:
        ListX = chasb(ListX,numbers[i])

    return(ListX)


inp = list(input("Input the number : "))
newList = []

for i in inp:
    newList.append(int(i))

result = bechasb(newList)

for i in result:
    print(i)
