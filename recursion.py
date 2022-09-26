def factorial(x: int) -> int:
    if x == 1:
        return 1
    else:
        return(x * factorial(x-1))

print(factorial(3))
print(factorial(6))  

my_list =[1,2,3,4,5,6,7,8,9,10,11,12,35,31]

new_list = list(filter(lambda x: x%2 == 0, my_list))


def factorial(n):
    fact = 1

    while n>0:
        fact = fact * n

def reverse_string(s: str) -> str:
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
print(reverse_string("Hello"))

def reverse_str(s: str) ->str:
    return s[::-1]

print(reverse_str("Hello"))