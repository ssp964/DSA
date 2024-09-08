def lcm(x: int, y: int):
    greater = max(x, y)

    while True:
        if greater % x == 0 and greater % y == 0:
            return f"The LCM of {x} and {y} is {greater}"
        greater += 1



if __name__ == '__main__':
    ip_no1 = int(input("Enter the first number: "))
    ip_no2 = int(input("Enter the second number: "))

    print(lcm(ip_no1, ip_no2))