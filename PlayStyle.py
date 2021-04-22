with open ("Satisfied.txt") as f:
    s = f.readlines()

print (s)

totalwords = 0

for i in s:
    n = len(i.strip().split())
    print (n)
    totalwords = totalwords + n
    print (totalwords)
    print (len(s))
nlines = len(s)
aveWords = totalwords / nlines
print ('averageWords', aveWords)
lc=[]
for i in s:
    lc.append(i.lower())
    lc[-1]=lc[-1].replace(',','')
    lc[-1]=lc[-1].replace('(','')
    lc[-1]=lc[-1].replace(')','')
    print(lc[-1])
    





##for i in range (len(s)):
##    print (s[i].strip())
##
##nlines = len(s)
##
##print (f'the number of lines is {nlines}')
##line = s[].split()
##print (line)
