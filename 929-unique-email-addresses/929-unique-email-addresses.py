class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        import re
        for i in range(len(emails)):
            localName, domainName = re.split("@", emails[i])
            localName = localName.replace('.', '')
            localName = re.sub("\+[a-z]*", "", localName)
            
            emails[i] = localName + "@" + domainName
        
        return(len(list(set(emails))))
        