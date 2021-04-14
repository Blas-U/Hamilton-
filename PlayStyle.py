with open ("Satisfied.txt") as f:
    s = f.readlines()

print (s[0])

for i in range (0,60):
    print (s[i].strip())
