def parseStringForAshtik(s):
    result=[]
    i=0
    while i < len(s):
        if ord(s[i])>47 and ord(s[i])<58:
            number = ''
            while i<len(s) and ord(s[i])>47 and ord(s[i])<58:
                number += s[i]
                i+=1
            result.append(number)
        elif s[i] >= 'a' and s[i] <= 'z':
            result.append(s[i])
            i+=1
        elif s[i] >= 'A' and s[i] <= 'Z':
            result.append(chr(ord(s[i])+32))
            i+=1
        else:
            i+=1
    return result

print(parseStringForAshtik("Hc123rf(A)t456y"))
        

