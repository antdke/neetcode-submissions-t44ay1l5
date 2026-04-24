class Solution:

    def encode(self, strs: List[str]) -> str:
        
        # traverse list of strings
        # encode length
        # add a seperator
        # append to a single string

        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s

        return encoded_string

    def decode(self, s: str) -> List[str]:
        
        # create empty list
        # traverse string
        # add integer version of char until you hit "#"
        # once at "#", then have two pointers
        # grab substring from one element over from "#" until the integer value stored
        # add that substring to the result list

        res = []
        head = 0
        while head < len(s):
            tail = head
            while s[tail] != "#":
                tail += 1
            print(s[head:tail])
            length = int(s[head:tail])
            head = tail + 1
            tail = head + length
            res.append(s[head:tail])
            head = tail

        return res

            
            


