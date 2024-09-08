def fact(n):
    result = 1

    for i in range(2, n+1):
        result *= i

    return f"The factorial of {n} is: {result}"

if __name__ == '__main__':
    ip_no = int(input("Enter the number: "))
    print(fact(ip_no))