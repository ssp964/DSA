def find_trailing_zeros(n):
    if n < 0:  # Negative Number Edge Case
        return -1

    # Initialize result
    count = 0

    # Keep dividing n by powers of 5 and update count
    i = 5
    while n // i >= 1:
        print(f"The value of {n}//{i} is {n//i}")
        count += n // i
        i *= 5
        print(f"The value of count is: {count}")

    return count

# Driver Code
if __name__ == "__main__":
    ip_no = int(input("Enter the number: "))
    print(f"Count of trailing 0s in {ip_no}! is {find_trailing_zeros(ip_no)}")