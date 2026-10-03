class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # This character now has enough copies in the window.
            if c in countT and window[c] == countT[c]:
                have += 1

            # Shrink the window while it still contains everything.
            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Remove the leftmost character.
                leftChar = s[l]
                window[leftChar] -= 1

                # The window becomes invalid if a required count drops.
                if leftChar in countT and window[leftChar] < countT[leftChar]:
                    have -= 1

                l += 1

        l, r = res
        return s[l:r + 1] if resLen != float("infinity") else ""