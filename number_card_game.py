'''
숫자 카드 게임은 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다.
단, 게임의 룰을 지키며 카드를 뽑아야 하고 룰은 다음과 같다.

    1. 숫자가 쓰인 카드들이 N * M 형태로 놓여 있다. 이 때 N은 행의 개수를 의미하고, M은 열의 개수를 의미한다.
    2. 먼제 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
    3. 그 다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
    4. 따라서 처음 카드를 골라낼 행을 선택 할 때,
       이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여
       최종적으로 가장 높은 숫자의 카드를 뽑을 수 있는 전략을 세워야 한다.

예를 들어, 3 * 3의 형태로 카드 들이 다음과 같이 놓여 있다고 가정하자
[[3, 1, 2],
[4, 1, 4],
[2, 2, 2]]

여기서 카드를 골라낼 행을 고를 때 첫 번째 혹은, 두 번째 행을 선택하는 경우, 최종적으로 뽑는 카드는 1이다.
하지만 세 번째 행을 선택하는 경우 최종적으로 뽑ㅂ는 카드는 2이다.
따라서 이 예제에서는 세번째 행을 선택하여 숫자 2가 쓰여진 카드를 뽑는 것이 정담이다.

ex>
  1. 3, 3
     3, 1, 2
     4, 1, 4
     2, 2, 2
  result = 2

  2. 2, 4
     7, 3, 1, 8
     3, 3, 3, 4
'''

class NumberCard:
    def __init__(self, row_col, arr):
        self.row_col = row_col
        self.arr = arr
        self.check_condition()

    def check_condition(self):
        if self.row_col[0] == len(self.arr) and self.row_col[1] == len(self.arr[0][:]):
            return self.row_col, self.arr
        else:
            return 'wrong array, please check it'

    def change_condition(self, row_col_data, arr_data):
        self.row_col = row_col_data
        self.arr = arr_data
        self.check_condition()

    def calculation(self):
        buffer = []
        for idx in range(self.row_col[0]):
            buffer.append(min(self.arr[idx][:]))
        return max(buffer)


def test():
    test1 = NumberCard([2, 2], [[3, 1], [4, 1]])
    print('check test1 condition: ', test1.check_condition())
    test1.change_condition([3, 3], [[3, 1, 2], [4, 1, 4], [2, 2, 2]])
    print('check test1 changed condition: ', test1.check_condition())
    assert (test1.calculation() == 2)
    test2 = NumberCard([2, 3], [[1, 2, 3], [3, 4, 5]])
    print('check test2 condition: ', test2.check_condition())
    test2.change_condition([2, 4], [[7, 3, 1, 8], [3, 3, 3, 4]])
    print('check test2 changed condition: ', test2.check_condition())
    assert (test2.calculation() == 3)

if __name__ == '__main__':
    test()