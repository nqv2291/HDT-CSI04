def xepgach(n):
    if n < 3:
        return 0
    
    prime_arr = [True] * (n)
    prime_arr[0] = False
    prime_arr[1] = False
    
    listsnt = [] #Chua cac so nguyen to
    for i in range(2,n):
        if prime_arr[i]:
            listsnt.append(i)
            
            for j in range(2,(int((n-1)//i)+1)):
                prime_arr[i*j] = False
    
    for i in range(len(listsnt)-1):
        if listsnt[i]*listsnt[i+1]<=n:
            result = listsnt[i],listsnt[i+1]
    
    return n - result[0]*result[1] 

n= int(input())  
t = []          
for i in range(n):
    t.append(int(input()))

for i in t:
    print(xepgach(i))    