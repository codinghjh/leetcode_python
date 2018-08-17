class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        string_x = str(x)
        negative = False
        result = 0
        for s in string_x[::-1]:
            if s == '-':
                negative = True
                continue
            elif s == '+':
                continue
            else:
                result = result * 10 + int(s, 10)
        if negative:
            result = -result
        if result < - pow(2, 31) or result > pow(2, 31) - 1:
            return 0
        return result


a = Solution()
print(a.reverse(123))
