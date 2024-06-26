# Approach -1
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # if . then same email
        # if + then all before + gets email
        s = ""
        unique = set()
        for e in emails:
            local, domain = e.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            unique.add((local, domain))
            print(unique)
        return len(unique)


# Approach-2
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # if . then same email
        # if + then all before + gets email
        s = ""
        unique = set()
        for e in emails:
            i, local = 0, ""
            while e[i] not in ["@", "+"]:
                if e[i] != ".":
                    local += e[i]
                i += 1

            while e[i] != "@":
                i += 1
            domain = e[i + 1 :]
            unique.add((local, domain))
        return len(unique)


# Time : 72ms (12.81%) Space : 16.62 MB (73.79%)
