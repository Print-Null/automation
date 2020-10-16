class Solution:
    def myPow(slef, x: float, n: int) -> float:
        if x == 0 and n != 0:
            return 0
        elif x == 0 and n == 0:
            print("0的0次方没有意义")
        elif x != 0 and n == 0:
            return 1
        elif x != 0 and n > 0:
            listx = []
            for i in range(1, n + 1):
                listx.append(x)

            pow = 1
            for i in listx:
                pow = pow * i
            return pow
        elif x != 0 and n < 0:
            listx = []
            for i in range(1, -n + 1):
                listx.append(1 / x)

            pow = 1
            for i in listx:
                pow = pow * i
            return pow


solution = Solution()
print(solution.myPow(2.1, 3))


def num(J: str, S: str):
    count = 0
    for i in J:
        for j in S:
            if i == j:
                count += 1
    return count


print(num("baA", "abcbefg"))



