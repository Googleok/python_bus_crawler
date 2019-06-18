'''
문제5.
선택정렬(제자리 정렬 알고리즘)을 적용하는 코드를 완성하세요.
문제에 주어진 배열 [ 5, 9, 3, 8, 60, 20, 1 ] 를 크기 순서대로 정렬하여
다음과 같은 출력이 되도록 완성하는 문제입니다.
'''
# --- 1 : 그냥 정렬

l = [5, 9, 3, 8, 60, 20, 1]

# l.sort(reverse=True)
# print(l)
for j in range(0, len(l)-1):
    for i in range(0, len(l)-1):
        if l[i] < l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
            print(i, l)

l = [5, 9, 3, 8, 60, 20, 1]

tmp = 0
for i in l:
    tmp = l[i]
    print(l)
