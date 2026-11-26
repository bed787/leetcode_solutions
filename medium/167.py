class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            inter_target = numbers[left] + numbers[right]
            if inter_target < target:
                left += 1
            elif inter_target > target:
                right -= 1
            else:
                return [left + 1, right + 1]

print(Solution().twoSum([2,7,11,15], 9))

'''

Задача чуть ли не проще, чем обычный twoSum. Просто ставим указатели влево и вправо. Складываем числа, стоящие
на этих указателях. Если это число больше таргета - двигаем правый указатель влево, если это число меньше таргета -
двигаем левый указатель вправо. Иначе возвращаем индексы указателей (к каждому индексу + 1, т.к. в условии просят)

'''