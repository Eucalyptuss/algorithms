'''
정보 선생님은 수업을 시작하기 전에 이상한 출석을 부른다.

선생님은 출석부를 보고 번호를 부르는데,
학생들의 얼굴과 이름을 빨리 익히기 위해 번호를 무작위(랜덤)으로 부른다.

그리고 얼굴과 이름이 잘 기억되지 않는 학생들은 번호를 여러 번 불러
이름과 얼굴을 빨리 익히려고 하는 것이다.

출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.

입력
첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.

출력
1번부터 번호가 불린 횟수를 순서대로 공백으로 구분하여 한 줄로 출력한다.

입력 예시
10
1 3 2 2 5 6 7 4 5 9

출력 예시
1 2 1 1 2 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
'''

class Sort():
    def __init__(self, count, list_data):
        self.count = count
        self.list_data = list_data

    def check_value(self):
        return self.count, self.list_data

    def change_value(self, count, list_data):
        self.count = count
        self.list_data = list_data

    def sort_data(self):
        result = [0] * 23

        for idx in self.list_data:
            result[idx-1] += 1

        return result

def test():
    test1 = Sort(10, [1, 3, 2, 2, 5, 6, 7, 4, 5, 9])
    print('test1 check value: ', test1.check_value())
    result = [1, 2, 1, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert(test1.sort_data() == [1, 2, 1, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    assert(all([a == b for a, b in zip(test1.sort_data(), result)]))

if __name__ == '__main__':
    test()