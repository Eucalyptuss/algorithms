'''
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
단, 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.

1. N에서 1을 뺀다.
2. N을 k로 나눈다.

예를 들어 N이 17, K가 4라고 가정하자. 이 때 1번의 과정을 한 번 수행하면 N은 16이 된다.
이후에 2번의 과정을 두번 수행하면 N은 1이 된다.
결과적으로 이 경우 전체 과정을 실행한 횟수는 3이 된다.
이는 N을 1로 만드는 최소 횟수이다.

N과 K가 주어질 때 N이 1이 될 때 까지 1번 혹은 2번 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하시오.

입력 예시 25 5
출력 예시 2
'''

class UntilNumberReachesOne:
    def __init__(self, n, k):
        self.n = n
        self.k = k

    def check_values(self):
        return self.n, self.k

    def change_condition(self, n, k):
        self.n = n
        self.k = k

    def calculation(self):
        cnt = 0
        finish = True
        remain_n = self.n

        while True:
            if remain_n <= self.k:
                if remain_n == 1:
                    finish = False
                break

            if remain_n % self.k != 0:
                remain_n -= 1
            else:
                remain_n = remain_n / self.k
            cnt += 1

        if finish:
            return cnt +1
        else:
            return cnt + remain_n

def test():
    test1 = UntilNumberReachesOne(17, 4)
    print('check test1 values: ', test1.check_values())
    assert(test1.calculation() == 3)
    test1.change_condition(25, 5)
    print('check test1 changed values: ', test1.check_values())
    assert (test1.calculation() == 2)
    test2 = UntilNumberReachesOne(25, 5)
    print('check test2 values: ', test2.check_values())
    assert (test2.calculation() == 2)
    test2.change_condition(25, 3)
    print('check test2 changed values: ', test2.check_values())
    assert(test2.calculation() == 6)



if __name__ == '__main__':
    test()