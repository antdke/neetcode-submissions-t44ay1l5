class Solution:

    def encode(self, strs: List[str]) -> str:

        # traverse string
        # for each string
            # encode the string length + separator
            # concatenate into a result string
        # return the result string

        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        print(res)
        return res


    def decode(self, s: str) -> List[str]:

        # think of an accordian
        # set two pointers
        # head/tail
        # head/tail start at 0
        # move tail until find "#"
        # then grab head:tail and convert to int
        # use that to slip head/tail after "#"
        # grab that string and add to result list

        res = []
        head = 0

        while head < len(s) - 1:
            tail = head
            while s[tail] != "#":
                tail += 1
            length = int(s[head:tail])
            print(length)
            head = tail + 1
            print(head)
            tail = head + length
            print(tail)
            print(s[head:tail])
            res.append(s[head:tail])
            head = tail

        return res