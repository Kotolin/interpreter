import AppClass_sm


alphabet = set("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
#ex_alphabet = set("_.qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
usernames = {}

def get_stats(name, username):
    if name in username:
        usernames[name] += 1
    else:
        usernames[name] = 1

class AppClass:
    def __init__(self):
        self._fsm = AppClass_sm.AppClass_sm(self)
        self._is_acceptable = False
        self.counter = 0
        self.username = ''
        self.current_string = ''

    def Counter(self):
        self.counter += 1

    def ResetCounter(self):
        self.counter = 0

    def Acceptable(self):
        self._is_acceptable = True

    def Unacceptable(self):
        self._is_acceptable = False

    def Save_name(self):
        self.username = self.current_string[7:7 + self.counter]

    def check(self, string):
        self.current_string = string
        self._fsm.enterStartState()
        for c in string:
            self._fsm.symb(c, self.counter)
        return self._is_acceptable, self.username

try:
    with open("data.txt") as f:
        for string in f:
            checker = AppClass()
            print('--')
            print(string.rstrip('\n'))
            flag, f_name = checker.check(string)
            get_stats(f_name, usernames)
            print(str(flag) + " " + f_name)
except IOError as e:
    print("No file found")

print("--")
print(usernames)
