def sieve_flavius(min_n, max_n) -> set:
    """
    Return set with lucky numbers.
    """
    pointer = 1
    lst = list(range(1, max_n + 1, 2))
    while pointer < len(lst):
        new_lst = []
        num = lst[pointer]
        for i in range(len(lst)):
            if (i + 1) % num != 0:
                new_lst.append(lst[i])
        lst = new_lst
        pointer += 1
    ind = 0
    while lst[ind] < min_n:
        ind += 1
    return set(lst[ind:])


def ulam(min_n, max_n) -> set:
    """
    Return set with ulam numbers.
    """
    ulams = [1, 2]

    sums = [0 for i in range(2 * max_n)]

    newUlam = 2
    sumIndex = 1

    while newUlam < max_n:
        for i in ulams:
            if i < newUlam:
                sums[i + newUlam] += 1
        while sums[sumIndex] != 1:
            sumIndex += 1
        newUlam = sumIndex
        sumIndex += 1
        ulams.append(newUlam)
    ind_down = 0
    print(ulams)
    while ulams[ind_down] < min_n:
        ind_down += 1
    ind_up = -1
    while ulams[ind_down] > max_n:
        ind_up -= 1

    return set(ulams[ind_down:ind_up])


def even(min_n, max_n) -> set:
    """
    Return set with even numbers.
    """
    even_s = {x for x in range(min_n, max_n + 1) if x % 2 == 0}
    print()
    return even_s


print(even(12, 32))


# sieve_flavius_set = sieve_flavius()
# ulam_set = ulam()
# even_set = even()
