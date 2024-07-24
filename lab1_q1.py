v='aeiou'
c='bcdfghjklmnpqrstvwxyz'
s=input()
count=0
count1=0
for x in s:
    if x in v:
        count+=1
    if x in c:
        count1+=1
print('No. of vowels',count)
print('No. of consonents',count1)