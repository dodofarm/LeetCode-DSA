# @leet start
class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        zeroes, ones = 0, 0
        for i in students:
            if i == 1:
                ones += 1
            else:
                zeroes += 1

        for i in sandwiches:
            if i == 1:
                ones -= 1
                if ones == -1:
                    return zeroes
            else:
                zeroes -= 1
                if zeroes == -1:
                    return ones

        return 0


# @leet end
