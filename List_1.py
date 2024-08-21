'''
정보 선생님은 수업을 시작하기 전에 이상한 출석을 부른다.

학생들의 얼굴과 이름을 빨리 익히기 위해 번호를 무작위(랜덤)으로 부르는데,
영일이는 선생님이 부른 번호들을 기억하고 있다가 거꾸로 불러보는 것을 해보고 싶어졌다.

출석 번호를 n번 무작위로 불렀을 때, 부른 번호를 거꾸로 출력해 보자.

입력
번호를 부른 횟수(n, 1 ~ 10000)가 첫 줄에 입력된다.
n개의 랜덤 번호(k, 1 ~ 23)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력된다.

출력
출석을 부른 번호 순서를 바꾸어 공백을 두고 출력한다.

입력 예시
10
10 4 2 3 6 6 7 9 8 5

출력 예시
5 8 9 7 6 6 3 2 4 10
'''

class ReverseList():
    def __init__(self, n, list_data):
        self.n = n
        self.list_data = list_data

    def check_value(self):
        return self.n, self.list_data

    def change_data(self, n, list_data):
        self.n = n
        self.list_data = list_data

    def reverse_list(self):
        result = []

        for idx in range(self.n):
            result.append(self.list_data[self.n - idx - 1])
        return result

def test():
    test1 = ReverseList(10, [10, 4, 2, 3, 6, 6, 7, 9, 8, 5])
    print(test1.check_value())
    assert(test1.reverse_list() == [5, 8, 9, 7, 6, 6, 3, 2, 4, 10])
    test1.change_data(3, [5, 4, 3])
    print(test1.check_value())
    assert(test1.reverse_list() == [3, 4, 5])

if __name__ == '__main__':
    test()