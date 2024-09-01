'''
Recursive Fuction(재귀함수)
!(factorial) 계산하기
'''

class Factorial():
    def __init__(self, n):
        self.n = n

    def check_value(self):
        return self.n

    def change_value(self, n):
        self.n = n

    def factorial_interative(self):
        result = 1
        for idx in range(1, self.n + 1):
            result *= idx
        return result

    def recursive(self, n):
        if n <= 1:
            return 1
        return n * self.recursive(n - 1)

    def factorial_recursive(self):
        return self.recursive(self.n)


def test():
    test1 = Factorial(5)
    print(test1.check_value())
    assert(test1.factorial_interative() == 120)
    assert(test1.factorial_recursive() == 120)
    test1.change_value(10)
    print(test1.check_value())
    assert(test1.factorial_interative() == 3628800)
    assert(test1.factorial_recursive() == 3628800)

if __name__ == '__main__':
    test()