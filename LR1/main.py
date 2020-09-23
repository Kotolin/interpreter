import re


reg = "(?i:mailto: [a-z0-9]+@[a-z0-9]+\.[a-z]+(\?subject=[a-z0-9]{1,64}))"
reg_user = "(?i:: [a-z0-9]+@)"
in_file = open("input.txt", "r")
out_file = open("output.txt", "w")
user_data = {}
data = in_file.read()
val_list = re.findall(reg, data)
for line in val_list:
    user = re.findall(reg_user, line)
    user = user[0][2:-1].lower()
    if user[0] not in user_data:
        user_data[user] = 1
    else:
        user_data[user] += 1
for tup in user_data.items():
    out_file.write(tup[0] + ": " + str(tup[1]) + "\n")
