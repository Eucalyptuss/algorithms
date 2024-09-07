'''
Graph의 방식

1. 인접 행렬 방식(위치와 거리)
2. 인접 리스트 방식(위치와 거리, 위치만)
3. 딕셔너리
'''


# 인접 행렬

INF = 999999999999999

graph_array = [
    [0, INF, 5, INF, 9],
    [INF, INF, INF, INF, INF],
    [5, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF],
    [9, INF, INF, INF, INF]
]

# 인접 리스트

graph_list = [
    [(2, 5), (4, 9)],
    [],
    [(0, 5)],
    [],
    [(0, 9)]
]

graph_list_2 = [[] for _ in range(5)]

graph_list_2[0].append((2, 5))
graph_list_2[0].append((4, 9))
graph_list_2[2].append((0, 5))
graph_list_2[4].append((0, 9))

graph_list_3 = [[] for _ in range(5)]

graph_list_3[0].append(2)
graph_list_3[0].append(4)
graph_list_3[2].append(0)
graph_list_3[4].append(0)

graph_dictionary = {
    0: [2, 4],
    1: [],
    2: [0],
    3: [],
    4: [0]
}



print(graph_array)
print()
print(graph_list)
print()
print(graph_list_2)
print()
print(graph_list_3)
print()
print(graph_dictionary)