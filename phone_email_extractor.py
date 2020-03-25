import pyperclip
import re

# User guide
print("Email and Phone Number Finder\n")
print("Copy the text of the document to get emails and phone numbers from.")
print("The phone-numbers are in kenyan format.")

# Press enter to begin
input("Press enter once you have copied text to be searched.\n")
# pasting copied string from a source that will be used by the two regex
emails_phones = str(pyperclip.paste())

# kenyan phone numbers patterns
phone_pattern = re.compile(r'''(
            \+?
            \d+
            -?
            7
            \d+
            -?
            \d+
            -?
            \d+
)''',re.VERBOSE)

# email addresses regex
email_pattern = re.compile(r'''(
        [a-zA-Z0-9-.+/]+
        @
        [a-zA-Z+-]+
        \.[a-zA-Z]{2,4}
)''',re.VERBOSE)


# passing the copied string to the two regex
matching_numbers = phone_pattern.findall(emails_phones)
matching_email = email_pattern.findall(emails_phones)

# list that will hold the matching results
matches = list()

# appending the results to one list
for email in matching_email:
    matches.append(email)
for num in matching_numbers:
    matches.append(num)

# Checking if we got any matches or none
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard")
    print('\n'.join(matches))
else:
    print("No emails or phone numbers found!!!".upper())

print("\nThank you.This program is by Benny Hinn")
