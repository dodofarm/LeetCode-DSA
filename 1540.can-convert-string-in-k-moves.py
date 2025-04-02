# @leet start
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        char_set = set()
        step_set = set()
        s_list = list(s)
        t_list = list(t)

        for i in range(0, len(s)):
            ord_s = ord(s_list.pop(0)) - ord("a") + 1
            ord_t = ord(t_list.pop(0)) - ord("a") + 1
            if s[i] != t[i]:
                print("s not equal t")
                difference = abs(ord_t - ord_s)
                # if difference > 13:
                #     difference = 26 + ord(t[i]) - ord(s[i])

                # if difference > 13 and ord(s[i]) < ord(t[i]):
                #     difference = 26 - ord(t[i]) + ord(s[i])
                if ord_s > ord_t:
                    # difference = 26 + ord(t[i]) - ord(s[i])
                    # difference = abs(26 - ((ord(t[i]) - ord('a')+1) - (ord(s[i]) - ord('a')+1)))
                    difference = abs(26 - (ord_s - ord_t))
                print(s[i], t[i], difference)
                # k -= count

                for step in range(difference, k + 1, 26):
                    print("i", i, "step:", step)
                    if i not in char_set and step not in step_set:
                        print("i not in char_set and step not in step_set")
                        char_set.add(i)
                        step_set.add(step)
                        break

                if i not in char_set:
                    print("returning false")
                    return False

        if len(t_list) > 0:
            return False

        print(char_set)
        return True


# @leet end
