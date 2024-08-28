'''
말이 맵 안에 움직일 수 있으며, 맵은 1 X 1 크기의 정사각형으로 이루어진 N X M 크기의 직사각형으로, 각각의 칸은 육지 또는 바다이다.
말은 동서남북 중 한 곳을 바라본다.

맵의 각 칸은(A, B)로 나타낼 수 있고, A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수이다.

말은 상하좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 갈 수 없다.
말의 움직임을 설정하기 위해 정해놓은 메뉴얼은 아래와 같다.

1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.)
2. 말의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다.
   왼쪽방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
   단, 이 때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

메뉴얼에 따라 말을 움직인 뒤에, 말이 방문한 칸의 수를 출력하는 프로그램을 만드시오

입력 예시
4 4 # 4 x 4 맵 생성
1 1 0 # (1, 1)위치에서 0(북쪽) 방향을 보고 서 있는 말
1 1 1 1 # 첫 줄은 모두 바다
1 0 0 1 # 둘째 줄은 바다/육지/육지/바다
1 1 0 1 # 셋째 줄은 바다/바다/육지/바다
1 1 1 1 # 넷째 줄은 모두 바다

출력 예시
3
'''

class MoveMap():
    def __init__(self, map_row, map_col, initial_position, map_2d):
        self.map_row = map_row
        self.map_col = map_col
        self.initial_position = initial_position
        self.map_2d = map_2d

    def check_value(self):
        return self.map_row, self.map_col, self.initial_position, self.map_2d

    def change_value(self, map_row, map_col, initial_position, map_2d):
        self.map_row = map_row
        self.map_col = map_col
        self.initial_position = initial_position
        self.map_2d = map_2d

    def start(self):
        position = self.initial_position[0:2]
        direction = self.initial_position[2]
        position_history = [[0] * self.map_col for _ in range(self.map_row)]
        self.map_2d[position[0]][position[1]] = 1

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        def turn_left(direction):
            direction -= 1
            if direction == -1:
                direction = 3
            return direction

        cnt = 1
        turn_time = 0

        while True:
            direction = turn_left(direction)
            nx = position[0] + dx[direction]
            ny = position[1] + dy[direction]

            if position_history[nx][ny] ==  0 and self.map_2d[nx][ny] == 0:
                position_history[nx][ny] = 1
                position = [nx, ny]
                cnt += 1
                turn_time = 0
                continue
            else:
                turn_time += 1

            if turn_time == 4:
                nx = position[0] - dx[direction]
                ny = position[1] - dy[direction]

                if self.map_2d[nx][ny] == 0:
                    position = [nx, ny]
                else:
                    break
                turn_time = 0

        return cnt


def test():
    test1 = MoveMap(4, 4, [1, 1, 0], [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]])
    print(test1.check_value())
    assert(test1.start() == 3)
    test1.change_value(4, 4, [1, 1, 3], [[1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]])
    print(test1.check_value())
    assert(test1.start() == 4)


if __name__ == '__main__':
    test()