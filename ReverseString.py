str1= "The Sky is Blue"

ans=""
lis=str1.split()
l=len(lis)-1

for i,j in enumerate(reversed(lis)):
    ans+=j
    if(i!=l):
        ans+=" "


print(ans)