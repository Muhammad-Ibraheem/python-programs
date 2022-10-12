a = "asd9-o1werkj-gh8i-boor-uttmn"
b = a.replace("-", " ")
print(b)

char = "ye"
newstr = ""
for i in range(len(b)):
    if b[i] == 'a' or b[i] == 'e' or b[i] == 'i' or b[i] == 'o' or b[i] == 'u':
        newstr = newstr + char
    else:
        newstr = newstr + b[i]

print(newstr)

oldstring = 'asd9-o1werkj-gh8i-boor-uttmn'
newstring = oldstring[0]
for char in oldstring[1:]:
    if char != newstring[-1]:
        newstring += char
print(newstring)
