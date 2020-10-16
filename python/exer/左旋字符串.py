def reverseLeftWords(s: str, n: int) -> str:
    revers = list(s)[::-1]
    word = []
    for i in range(1, n + 1):
        word.append(revers.pop())
    result = "".join(revers[::-1]+word)

    print(revers[::-1])
    print(word)
    print(result)


reverseLeftWords("abcdefg", 3)
