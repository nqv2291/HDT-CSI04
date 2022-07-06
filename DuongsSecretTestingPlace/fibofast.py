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

sample = 359579325206583560961765665172189099052367214309267232255589801
i = 1
current = fibo(1)
while sample > current:
    current = fibo(i)
    i+=1
    
print(1 if current == sample else 0)
print(fibo(300))
real_time = time.time() - start_time
print(real_time)