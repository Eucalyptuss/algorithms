'''

온라인 채점시스템에는 초등학생, 중고등학생, 대학생, 대학원생,
일반인, 군인, 프로그래머, 탑코더 등 아주 많은 사람들이 들어와 문제를 풀고 있는데,

실시간 채점 정보는 메뉴의 채점기록(Judge Status)을 통해 살펴볼 수 있다.

자! 여기서...잠깐..
같은 날 동시에 가입한 3명의 사람들이 온라인 채점시스템에 들어와 문제를 푸는 날짜가
매우 규칙적이라고 할 때, 다시 모두 함께 문제를 풀게 되는 그날은 언제일까?

예를 들어 3명이 같은 날 가입/등업하고, 각각 3일마다, 7일마다, 9일마다
한 번씩 들어온다면, 처음 가입하고 63일 만에 다시 3명이 함께 문제를 풀게 된다.

입력
같은 날 동시에 가입한 인원 3명이 규칙적으로 방문하는,
방문 주기가 공백을 두고 입력된다. (단, 입력값은 100이하의 자연수이다.)

출력
3명이 다시 모두 함께 방문해 문제를 풀어보는 날(동시 가입/등업 후 며칠 후?)을 출력한다.

입력 예시
3 7 9

출력 예시
63
'''
import math
from functools import reduce


class JudgeStatus():
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def check_value(self):
        return self.p1, self.p2, self.p3

    def change_value(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def lcm(self, a, b):
        return math.lcm(a, b)

    def lcm_multiple(self):
        return reduce(self.lcm, [self.p1, self.p2, self.p3])

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm_manual(self, a, b):
        return abs(a * b) // self.gcd(a, b)

    def lcm_multiple_manual(self):
        return reduce(self.lcm_manual, [self.p1, self.p2, self.p3])


def test():
    test1_1 = JudgeStatus(3, 7, 9)
    print("test1_1 check values: ", test1_1.check_value())
    assert(test1_1.lcm_multiple() == 63)
    test2_1 = JudgeStatus(5, 7, 9)
    print("test2_1 check values: ", test2_1.check_value())
    assert (test2_1.lcm_multiple_manual() == 63)

if __name__ == '__main__':
    test()