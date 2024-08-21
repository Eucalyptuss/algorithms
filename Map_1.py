'''
여행가 A는 N X N크기의 정사각형 공간위에 서 있다.
이 공간은 1 X 1 크기의 정사각형으로 나누어져 있다. 가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N) 이다.
여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)이다.
우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있다.(L, R, U, D)
이 때 여향가 A가 N X N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다.

여행가 A가 최종적으로 도착할 지점의 좌표를 출력하는 프로그램을 작성하시오
'''

class Map():
    def __init__(self, n, list_direction_data):
        self.n = n
        self.list_direction_data = list_direction_data

    def check_value(self):
        return self.n, self.list_direction_data

    def change_data(self, n, list_direction_data):
        self.n = n
        self.list_direction_data = list_direction_data

    def move(self):
        coord_row, coord_col = 1, 1
        for idx in range(len(self.list_direction_data)):
            buffer_coord_col, buffer_coord_row = 1, 1
            if self.list_direction_data[idx] == 'U':
                buffer_coord_col = coord_col -1
                buffer_coord_row = coord_row
            elif self.list_direction_data[idx] == 'D':
                buffer_coord_col = coord_col + 1
                buffer_coord_row = coord_row
            elif self.list_direction_data[idx] == 'L':
                buffer_coord_row = coord_row - 1
                buffer_coord_col = coord_col
            elif self.list_direction_data[idx] == 'R':
                buffer_coord_row = coord_row + 1
                buffer_coord_col = coord_col
            else:
                print('Data is not coreect!')

            if buffer_coord_row < 1 or buffer_coord_row > self.n or buffer_coord_col < 1 or buffer_coord_col > self.n:
                continue
            else:
                coord_col = buffer_coord_col
                coord_row = buffer_coord_row

        return [coord_col, coord_row]

def test():
    test1 = Map(5, ['R', 'R', 'R', 'U', 'D', 'D'])
    print(test1.check_value())
    assert(test1.move() == [3, 4])
    test1.change_data(5, ['L', 'R', 'R', 'U', 'D'])
    print(test1.check_value())
    assert(test1.move() == [2, 3])


if __name__ == '__main__':
    test()