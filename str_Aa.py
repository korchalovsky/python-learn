S1 = "HeLlO WoRdD! 123"
S2 = ""

for i in S1:
    if ord('Z') >= ord(i):
        if ord(i) <= ord('A'):
            S2 += i
        else:
            S2 += chr(ord(i) + 32)
    else:
        S2 += i

print(S2)
