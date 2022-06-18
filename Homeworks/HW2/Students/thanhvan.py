
def is_perfect_number(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        print(f'{n} is a perfect number')
    else:
        print(f'{n} is NOT a perfect number')



def sum_factorials(n):
    f = 1
    sum = 0

    for i in range(1, n + 1):
        f = f * i
        sum += f
    print(f'result = {sum}')
