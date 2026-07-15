class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # alpha="qwertyuiopsdfghjklzxcvbnm"
        # for ch in alpha:
        #     if ch not in sentence:
        #         return False
        #     else:
        #         return True
        seen = [False] * 26

        for ch in sentence:
            seen[ord(ch) - ord('a')] = True

        return all(seen)