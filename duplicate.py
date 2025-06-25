def dup(s):
    k = set(s)
    if len(s) == len(k):
        return False
    return True
s = input()
print(dup(s))