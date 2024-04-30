s=input()
part =input()
while part in s:
    s=s.replace(part,'')
print(s)