""" 삽입 정렬(Insertion Sort) : 특정한 데이터를 적절한 위치에 '삽입'한다는 의미에서 삽입 정렬이라함.
(첫 번째 데이터는 정렬되어 있다고 판단 -> 삽입 정렬은 '두 번째 데이터'부터 시작.)
시간복잡도 : O(N^2) -> 최선의 경우(리스트가 거의 정렬되어 있는 상태) 일 때 -> O(N)
"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법(step에 -1이 들어가면 start~end+1까지 1씩 감소)
        if array[j] < array[j - 1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)