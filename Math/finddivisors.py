def findDivisors(num: int):
    find_divisors = set() # define an empty set

    st_no = 1 #set start number as 1
    while st_no * st_no <= num:
        if num % st_no == 0:
            find_divisors.add(st_no) # adding the divisble number (st_no)
            find_divisors.add(num // st_no) # adding the divisbile number by dividing the st_no
        st_no += 1
    return sorted(find_divisors)

if __name__ == '__main__':
    ip_no = int(input("Enter the number: "))
    result = findDivisors(ip_no)
    print(f"The factors of {ip_no} are: {result}")