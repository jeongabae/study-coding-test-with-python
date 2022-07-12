#파이썬 정렬 라이브리는 항상 최악의 경우에도 시간 복잡도 O(NlogN)보장.

# sorted() 이용 : 리스트, 집합 자료형이나 딕셔너리 자료형을 입력받아 리스트형태로 정렬된 결과가 반환됨.
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)

# sort() 이용 : 정렬된 결과가 반환되지않고 내부 원소가 바로 정렬됨.
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

array.sort()
print(array)

# sorted()나 sort() 이용 시 key 매개변수를 이용해 정렬하는 방법
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting) #data[1] 즉 두번쨰 원소를 기준으로 정렬.
print(result)

# 람다 표현식 이용 정렬
array = [('바나나', 2), ('사과', 5), ('당근', 3)]
print(sorted(array,key=lambda x:x[1]))
#위의 식 대신 함수 정의해서 아래처럼 쓸수도..!
def my_key(x):
    return x[1]
print(sorted(array,key=my_key))