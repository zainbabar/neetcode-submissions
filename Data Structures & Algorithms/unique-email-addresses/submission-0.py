class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # need to go through all emails 
        # and parse them into their unique form 
        # drop the ., get rid of anything after the plus sign in the local
        unique = set()
        for index, email in enumerate(emails):
            local, domain = email.split("@")
            local = "".join(local.split("."))
            # split at + so first index is everything up to the first +
            # anything else is garbage, throw it away
            split_local = local.split("+")
            local = split_local[0]
            email = "".join([local, domain])
            unique.add(email)

        return len(unique)