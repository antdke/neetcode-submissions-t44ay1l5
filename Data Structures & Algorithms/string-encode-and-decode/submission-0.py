class Solution:

    def encode(self, strs: List[str]) -> str:
        
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s
        
        return result

    def decode(self, s: str) -> List[str]:

        result = []
        front = 0

        while front < len(s):
            back = front
            while s[back] != "#":
                back += 1
            length = int(s[front:back])
            front = back + 1
            back = front + length
            result.append(s[front:back])
            front = back

        return result

