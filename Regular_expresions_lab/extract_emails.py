import re

text = input()
pattern = r"((?<=\s)([a-z0-9]+[\.\-_]*[a-z0-9]*)@(([a-z\-]+)(\.([a-z]+))+))\b"

matches = re.findall(pattern, text)
for match in matches:
    print(match[0])

# Examples of valid emails: info@softuni-bulgaria.org, kiki@hotmail.co.uk, no-reply@github.com,
# s.peterson@mail.uu.net, info-bg@software-university.software.academy

# Examples of invalid emails: --123@gmail.com, …@mail.bg, .info@info.info, _steve@yahoo.cn,
# mike@helloworld, mike@.unknown.soft., s.johnson@invalid-
