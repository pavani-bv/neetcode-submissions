class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split('+')[0]
            local = local.replace(".","")
            new_emails = local + "@" + domain
            unique_emails.add(new_emails)
        return len(unique_emails)

                