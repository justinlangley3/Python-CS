import base64

def appendNullChars(string, x):
    for _ in range (0, x):
        string = string + "0"
    return string

def extractStringDifferences(string1, string2):
    diff1 = ''
    diff2 = ''
    t1 = []
    t2 = []

    if (len(string1) > len(string2)):
        appendNullChars( string2, (len(string1) - len(string2)) )
    else:
        appendNullChars( string1, (len(string2) - len(string1)) )

    for it, x in enumerate(string1):
        if string1[it] != string2[it]:
            t1.extend(string1[it])
            t2.extend(string2[it])
        else:
            pass
    for x in t1:
        diff1 += x
    for x in t2:
        diff2 += x

    return (diff1, diff2)

def sxor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

s1 = ""
s2 = ""

with open("string1.txt") as f, open("string2.txt") as g:
    s1 = f.read()
    s2 = g.read()
    g.close()
    f.close()

s1, s2 = extractStringDifferences(s1, s2)
print(s1 + "\n")
print(s2 + "\n")
s3 = sxor(base64.b64decode(s1), base64.b64decode(s2))
print(s3)