nums = list(map(int, input().split()))

hm = {}
def contains_duplicate(nums):
    for n in nums:
        if n not in hm:
            hm[n] = 1
        else:
            return False
    return True

print(contains_duplicate(nums))

'''
Не очень понял прикол задачи. Можно было бы вообще
в одну строку `if len(set(nums)) == len(nums)` и по
времени выполнения код был бы +- такой же, но раз
уж сказали мапой, я сделал мапой

Просто проход поэлементый (переделывать стркоу в числа необяз),
если элемента нет - добавляем в мапу, если есть - ломаем
функцию и возвращаем False

O(k), k - индекс первого повторенного элемента

'''