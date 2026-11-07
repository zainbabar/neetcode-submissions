class Solution:

    def encode(self, strs: List[str]) -> str:
        # outupt string has the length of the str
        # and then a comma
        # decoding starts reading the length until we hit a comma then we know 
        # we have the full length
        # throw away the comma and read the next length characters
        output = ""
        for s in strs:
            output += str(len(s)) + ","
            output += s
        return output

    def decode(self, s: str) -> List[str]:
        length = ""
        int_length = 0
        body = False
        output = []
        current = ""
        for i in range(len(s)):
            # not reading body text and havent hit delimiter yet
            if not body and (s[i]) != ",":
                length += s[i]
            # hit length delimiter, ignore the comma and wanna read the next length chars
            elif not body and s[i] == ",":
                int_length = int(length)
                if int_length == 0:
                    output.append("")
                    length = ""
                    continue
                body = True
                length = ""
                continue
            # at the body text now, keep reading into the curretn
            elif body:
                current += s[i]
                int_length -= 1
                if int_length <= 0:
                    body = False
                    output.append(current)
                    current = ""

        return output


            
