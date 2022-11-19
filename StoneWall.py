def solution(H):
    last=0
    c=0
    S=[]
    for i in range(0,len(H)):
        if(H[i]>last):
            last=H[i]
            c+=1
            S.append(H[i])
        elif(H[i]<last):
            while(len(S)>0 and H[i]<S[-1]):
                S.pop()
            if(len(S)==0 or H[i]!=S[-1]):
                c+=1
                S.append(H[i])
             last=H[i]
    return c
    pass
