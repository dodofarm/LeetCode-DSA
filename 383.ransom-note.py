# @leet start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False

        # Could also just to note = Counter(ransomNote) which would count all occurences
        note: dict[str, int] = {}

        # Instead of generating a dict for the magazine, generate a dict for the note.
        # The reason being that if the note can be contructed
        # it cuuld be that the magazine is too long
        # and it's faster to stop before the end of the magazine.
        for i in ransomNote:
            note[i] = 1 + note.get(i, 0)

        for i in magazine:
            if i in note:
                if note[i] == 1:
                    note.pop(i)
                else:
                    note[i] -= 1
            if not note:  # ransom note is done
                return True

        return False


# @leet end

