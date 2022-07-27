# 다익스트라 최단 경로 알고리즘에서 우선순위 큐 기능 구현 시 사용되는 힙 이용 위해 heapq라이브러리 사용
# 힙 정렬을 이러한 heapq로 구현하는 예제
import heapq

# 내림차순 힙 정렬
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)