import math

def sieve_flavius() -> list:
    """
    Return list with lucky numbers.
    """
    n = 100
    pointer = 1
    lst = list(range(1, n+1, 2))
    while pointer < len(lst):
        new_lst = []
        num = lst[pointer]
        for i in range(len(lst)):
            if (i+1) % num != 0:
                new_lst.append(lst[i])
        lst = new_lst
        pointer += 1
    return set(lst)

def ulam() -> list:
    """
    Return list with ulam numbers.
    """
    ulams=[]
    ulams.append(1)
    ulams.append(2)

    limit=100

    sums=[0 for i in range(2*limit)]

    newUlam=2
    sumIndex=1

    while(newUlam <limit):
        for i in ulams:
            if (i<newUlam):
                sums[i+newUlam] += 1
        while(sums[sumIndex]!=1):
            sumIndex += 1
        newUlam = sumIndex
        sumIndex += 1
        ulams.append(newUlam)
    return set(ulams)

def even() -> list:
    """
    Return list with even numbers.
    """
    n = 100
    even_lst = []
    for num in range(n+1):
        if num / 2 == 0:
            even_lst.append(num)
    return set(even_lst)