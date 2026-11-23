class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        s = s.lower()
        while left < right:
            if (s[left].isalnum() and s[right].isalnum()) and s[left] == s[right]:
                left += 1
                right -= 1
            elif (not s[left].isalnum()):
                left += 1
            elif (not s[right].isalnum()):
                right -= 1
            else:
                return False
        return True
                


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))


''' 
Самая большая сложность здесь — обработать "грязную" строку и сделать из нее то, что просят в примере
Для этого беру встроенный питоновский метод isalnum(), который проверяет, является ли символ
алфонумерическим (???), как и просят в задаче
ну и просто пишу всвозможные варианты событий и двигаю указателями

можно было решать через ord(), если не хотим встроенных методов
'''