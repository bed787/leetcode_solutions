nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

def intersection(nums1, nums2):
    hm = {}
    result = []
    for num in nums1:
        if num not in hm:
            hm[num] = 1
        else:
            hm[num] += 1
    for num in nums2:
        if (num in hm) and (hm[num] != 0):
            result.append(num)
            hm[num] -= 1
    return result

print(intersection(nums1, nums2))


'''

Немного костыльно, но вроде работает. Создана мапа, создан список рез.
Проходимся по первой строке, каждое число добавляем в мапу "найденное число: колво повторов".

Потом проходимся по второй строке. Берем число, если оно есть
в мапе (и значение не равно нулю) - добавляем в рез и убавляем значние этого
числа в мапе. То есть как бы ставим второй массив на счетчик - 
оттуда мы никак не сможем вытащить больше элементов чем есть в первом массиве.

O(n + k) - n, k - размеры массивов nums1, nums2

'''