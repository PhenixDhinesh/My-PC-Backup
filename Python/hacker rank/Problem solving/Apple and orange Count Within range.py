ho=list(map(int,input().split()))
ao=list(map(int,input().split()))
nf=list(map(int,input().split()))
ac=list(map(int,input().split()))
oc=list(map(int,input().split()))
l=[0,0]
for i in ac:
    if((ao[0]+i)>=ho[0] and (ao[0]+i)<=ho[1]):
        l[0]+=1
for i in oc:
    if((ao[1]+i)>=ho[0] and (ao[1]+i)<=ho[1]):
        l[1]+=1
x=[print(x) for x in l if True]