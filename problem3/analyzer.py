# Ryan Dawkins
# October 9th, 2014
# Programming Assignment 1

# Grammer:
# A > aB  | b  | cBB
# B > aB  | bA | Bb
# C > aaA | b  | caB

# A  > aB  | b | cBB
# B  > aB  | bA | bB`
# B` > bB` | ""
# C  > aaA | b | caB
# Isn't this irrelevant since there's no way to get to C?

class Analyzer(object):

    def a(self, sub):
        if sub[0] == "b":
            return True
        elif sub[0] == "a":
            return self.b(sub[1:])
        elif sub[0] == "c":
            return self.b(sub[1:])

    def b(self, sub):
        if len(sub) == 0:
            return True
        elif sub[0] == "a":
            return self.b(sub[1:])
        elif sub[0] == "b":
            return self.a(sub[1:])
        else:
            return False

    def c(self, sub):
        if len(sub) == 0:
            return True
        elif sub[0:1] == "aa":
            return self.a(sub[2:])
        elif sub[0] == "b":
            return True
        elif sub[0:1] == "ca":
            return self.b(sub[2:])
        else:
            return False
