baho=int(input("Oquvchining bahosini kiriting = "))
if baho>100 and baho<0:
    print("Baho 0 dan 100 gacha bolgan son oraligida bolishi shart!")
elif baho<60:
    print("Sizda F natija mavjud")
elif baho>59 and baho<70:
    print("Sizda D natija mavjud")
elif baho>69 and baho<80:
    print("Sizda c natija mavjud")
elif baho>79 and baho<89:
    print("Sizda B natija mavjud")
elif baho>89 and baho<=100:
    print("Sizda A natija mavjud")