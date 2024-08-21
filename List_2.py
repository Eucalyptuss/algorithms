'''
정보 선생님은 오늘도 이상한 출석을 부른다.

영일이는 오늘도 다른 생각을 해보았다.
출석 번호를 다 부르지는 않은 것 같은데... 가장 빠른 번호가 뭐였지?

출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.

단,
첫 번째 번호와 마지막 번호가 몇 번인지는 아무도 모른다.
음수(-) 번호, 0번 번호도 있을 수 있다.


입력
번호를 부른 횟수(n, 1 ~ 10000)가 첫 줄에 입력된다.
n개의 랜덤 번호(k)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력된다.

출력
출석을 부른 번호 중에 가장 빠른 번호를 출력한다.

입력 예시
10
10 4 2 3 6 6 7 9 8 5

출력 예시
2
'''

class FindMinList():
    def __init__(self, n, list_data):
        self.n = n
        self.list_data = list_data

    def check_value(self):
        if self.n != len(self.list_data):
            print('data length is not correct!')
        else:
            print('data length is okay')
        return(self.n, self.list_data)

    def change_data(self, n, list_data):
        self.n = n
        self.list_data = list_data

    def find_min_value(self):
        return(min(self.list_data))

def test():
    test1 = FindMinList(10, [10, 4, 2, 3, 6, 6, 7, 9, 8, 5])
    print(test1.check_value())
    assert(test1.find_min_value() == 2)
    test1.change_data(5, [5, 23, 3, 2, -1])
    print(test1.check_value())
    assert(test1.find_min_value() == -1)

if __name__ == '__main__':
    test()