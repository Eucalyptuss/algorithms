'''
체스판 8 X 8 좌표 평면이 있으며, 특정 위치에서 말은 L자 형태로만 이동할 수 있으며, 체스판 밖으로는 나갈 수 없다.
말은 특정 위치에서 다음과 같은 2가지 경우로 이동할 수 있다.

1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
2. 수직으로 두 칸 이동한 뒤에 수평으로 한칸 이동하기

행의 위치는 1부터 8까지 표현하며,
열의 위치는 a부터 h로 표현한다.

특정 위치의 값을 입력할 때, 말이 움직일 수 있는 모든 경우의 수를 계산하는 프로그램을 작성하라.
'''

class NumberOfCases():
    def __init__(self, position):
        self.position = position

    def check_value(self):
        return self.position

    def change_value(self, position):
        self.position = position

    def case_calculation(self):
        col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        row = [1, 2, 3, 4, 5, 6, 7, 8]

        col_pos = col.index(str(self.position[0]).lower()) + 1
        row_pos = row.index(int(self.position[1])) + 1

        case = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        result = 0

        for idx in case:
            next_col = col_pos + idx[0]
            next_row = row_pos + idx[1]

            if next_col >= 1 and next_col <= 8 and next_row >= 1 and next_row <= 8:
                result += 1

        return result

def test():
    test1 = NumberOfCases('a1')
    print(test1.check_value())
    assert(test1.case_calculation() == 2)
    test1.change_value('c2')
    print(test1.check_value())
    assert(test1.case_calculation() == 6)
    test1.change_value('B2')
    print(test1.check_value())
    assert(test1.case_calculation() == 4)
    test1.change_value('g7')
    print(test1.check_value())
    assert(test1.case_calculation() == 4)
    test2 = NumberOfCases('F7')
    print(test2.check_value())
    assert (test2.case_calculation() == 6)

if __name__ == '__main__':
    test()