'''
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.

예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각이다.
- 00시 00분 03초
- 00시 13분 30초

반면에 다음은 3이 하나도 푸함되어 있지 않으므로 세면 안 되는 시각이다.
- 00시 02분 55초
- 01시 27분 45초
'''

class Clock():
    def __init__(self, n):
        self.n = n

    def check_value(self):
        return self.n

    def change_value(self, n):
        self.n = n

    def count_num_three(self):
        result = 0
        for hh in range(self.n + 1):
            for mm in range(60):
                for ss in range(60):
                    if '3' in str(hh) + str(mm) + str(ss):
                        result += 1
        return result

    def count_num_three_2(self):
        result = 0
        for hh in range(self.n + 1):
            if '3' in str(hh):
                result += 3600
            else:
                result += 1575
                # Min [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53] -> 15*60 = 900
                # Sec [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53] -> 45*15 = 675 -> 900 + 675 = 1575
        return result
def test():
    test1 = Clock(5)
    print(test1.check_value())
    assert(test1.count_num_three() == 11475)
    assert(test1.count_num_three_2() == 11475)
    test1.change_value(1)
    print(test1.check_value())
    assert (test1.count_num_three() == 1575*2)
    assert (test1.count_num_three_2() == 1575*2)

if __name__ == '__main__':
    test()