'''
큰 수의 법칙은 일반적으로 통계 분야에서 다루어 지는 내용이지만 동빈이는 본인만의 방식으로 다르게 사용하고 있다.
동빈이의 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속적으로 K번을 초과하여 더해질 수 없는 것이 이법칙의 특징이다.

ex) [2, 3, 5, 4, 6], M = 8, K = 3 일 때 특정한 인덱스의 수가 연속해서 세번까지만 더해질 수 있으므로
    가장 큰 수의 결과는 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5인 46이 된다.

단, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다.

ex) [3, 4, 3, 4, 3], M = 7, K = 2 일 때,
    4 + 4 + 4 + 4 + 4 + 4 + 4가 가능하고 결과는 28이 된다.

ex1) [2, 3, 5, 4, 6], M = 8, K = 3, result = 46
ex2) [3, 4, 3, 4, 3], M = 7, K = 2, result = 28
ex3) [2, 4, 5, 4, 6], M = 8, K = 3, result = 46
'''

class LawOfBigNumber:
    def __init__(self, arr, m, k):
        self.arr = arr
        self.m = m
        self.k = k

    def check_values(self):
        return self.arr, self.m, self.k

    def add_arr(self, val):
        self.arr.append(val)

    def remove_arr(self, val):
        self.arr.remove(val)

    def calculation(self):
        first_number, second_number = sorted(self.arr, reverse=True)[0], sorted(self.arr, reverse=True)[1]
        result = first_number * (self.m - (self.m // self.k)) + second_number * (self.m // self.k)
        # print((self.m - (self.m // self.k), (self.m % self.k)))
        return result


def test():
    test1 = LawOfBigNumber([2, 3, 5, 4, 6], 8, 3)
    print('test1 values: ', test1.check_values())
    assert(test1.calculation() == 46)
    test1.add_arr(7)
    print('test1 values: ', test1.check_values())
    assert(test1.calculation() == 54)
    test1.remove_arr(7)
    print('test1 values: ', test1.check_values())
    assert (test1.calculation() == 46)
    test2 = LawOfBigNumber([3, 4, 3, 4, 3], 7, 2)
    print('test2 values: ', test2.check_values())
    assert(test2.calculation() == 28)
    test3 = LawOfBigNumber([2, 4, 5, 4, 6, 7], 8, 3)
    print('test3 values: ', test3.check_values())
    assert(test3.calculation() == 54)


if __name__ == '__main__':
    test()