def counts(a: str):
    dic = dict()
    for i in a:
        if i not in dic.keys():
            num = + 1
            dic[i] = num
        else:
            dic[i] = dic[i] + 1
    return dic


def comp(a, b):
    if counts(a) == counts(b):
        return True
    else:
        return False


print(comp("abacd", "aabcd"))
