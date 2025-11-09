sonlar=[1,2,3,4,5,6,7,8,9]
toq=[]
juft=[]
for son in sonlar:
    if son%2==0:
        juft.append(son)
    else:
        toq.append(son)
print("Juft sonlar: ",juft)
print("toq sonlar: ",toq)