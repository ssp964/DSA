def isPal(n:int):
    result = 0
    temp = n

    while temp!= 0:
        id = temp % 10
        result = result * 10 + id
        temp //= 10

    return f"{n} is a palindrome!" if result == n else f"{n} is not a palindrome"


ip_no = int(input("Enter the number to check: "))
result = isPal(ip_no)
print(result)    