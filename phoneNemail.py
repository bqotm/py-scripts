#! python3

import re, pyperclip


phoneRegex=re.compile(r'''
(
((\d\d\d) | (\(\d\d\d\)))?
(\s|-)
\d\d\d
-\d\d\d\d
(((ext(\.)?\s)|x)
 (\d{2,5}))?
)
''', re.VERBOSE)

emailRegex=re.compile(r'''
 [a-zA-Z0-9_.+]+@[a-zA-Z0-9_.+]+
 ''', re.VERBOSE)

text=pyperclip.paste()

extractedPhone=phoneRegex.findall(text)
extractedEmail=emailRegex.findall(text)


allPhoneNumbers=[]

for num in extractedPhone :
     allPhoneNumbers.append(num[0])

results='\n'.join(allPhoneNumbers)+'\nemails :\n'+'\n'.join(extractedEmail)

pyperclip.copy(results)

