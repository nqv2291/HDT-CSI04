import sys
sys.setrecursionlimit(100000000)
import time
start_time = time.time()

fibo_memo = {
    0:1,
    1:1
}

def fibo(n):
    if n in fibo_memo:
        return fibo_memo[n]
    else:
        fibo_memo[n] = fibo(n-1) + fibo(n-2)
        return fibo_memo[n]

# def fibo(n):
#     if n < 2:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)

for i in range(11):
    print(i,":",fibo(i))
real_time = time.time() - start_time
print(real_time)