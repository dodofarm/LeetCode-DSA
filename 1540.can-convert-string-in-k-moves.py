# @leet start
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False

        char_set = set()
        step_set = set()

        for i, (char_s, char_t) in enumerate(zip(s, t)):
            if char_s != char_t:
                # print("s not equal t")
                ord_s = ord(char_s) - ord("a") + 1
                ord_t = ord(char_t) - ord("a") + 1

                difference = abs(ord_t - ord_s)

                if ord_s > ord_t:
                    difference = abs(26 - (ord_s - ord_t))

                # print(char_s, char_t, difference)

                for step in range(difference, k + 1, 26):
                    # print("i", i, "step:", step)
                    if i not in char_set and step not in step_set:
                        # print("i not in char_set and step not in step_set")
                        char_set.add(i)
                        step_set.add(step)
                        break

                if i not in char_set:
                    # print("returning false")
                    return False

        # print(char_set)
        return True


# @leet end
