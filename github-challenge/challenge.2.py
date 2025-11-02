def rev(b):
    temp=[]
    for i in b:
        temp.insert(0,i)
    # print(f"Reversed list{temp}")
    print(f" Original list : {b}\n Reversed list : {temp}")



b=[1,2,3,4,5]
rev(b)