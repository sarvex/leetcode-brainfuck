class Solution:
    def reformat(self, s: str) -> str:
        a = [c for c in s if c.islower()]
        b = [c for c in s if c.isdigit()]
        if abs(len(a) - len(b)) > 1:
            return ''
        if len(a) < len(b):
            a, b = b, a
        ans = [x + y for x, y in zip(a, b)]
        if len(a) > len(b):
            ans.append(a[-1])
        return ''.join(ans)
