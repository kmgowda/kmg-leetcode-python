// https://leetcode.com/problems/unique-email-addresses

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        st=set()
        for mail in emails:
            local, domain = mail.split('@')
            i = local.find('+')
            if i < 0:
                local = local.replace('.','')
            else:
                local = local[0:i].replace('.','')
            st.add(local+'@'+domain)
        return len(st)    
            