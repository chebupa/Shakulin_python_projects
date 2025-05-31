
import re

def find_emails(lines: [str]) -> [str]:
    emails = []
    email_pattern = re.compile(r'^[\w]+@[\w.-]+\.[a-zA-Z]{2,}$')
    for line in lines:
        matches = email_pattern.findall(line)
        emails.extend(matches)
    return emails

with open("input.txt", 'r', encoding="utf-8") as file:
    lines = file.readlines()
    emails = find_emails(lines)
    for email in emails:
        print(email)