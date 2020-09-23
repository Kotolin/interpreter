import re


reg = "(?i:mailto:([a-z0-9]+)@[a-z0-9]+\.[a-z]+\?subject=[a-z0-9]{0,64})"
in_file = open("input.txt", "r")
out_file = open("output.txt", "w")
user_data = {}
for line in in_file.readlines():
    user = re.search(reg, line)
    if user and (user not in user_data):
        user = user.group(1)
        user_data[user] = 1
    else:
        user = user.group(1)
        user_data[user] += 1
for tup in user_data.items():
    out_file.write(tup[0] + ": " + str(tup[1]) + "\n")
