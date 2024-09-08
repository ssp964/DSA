#Using Sieve of Eratosthenes


def find_prime(num: int):
    '''
    Return the list of prime numbers
    '''
    st_no = 2
    prime_list = [True for i in range(num+1)]

    while st_no * st_no <= num:
        if prime_list[st_no]: #Checks if the value is True or not (True = prime, False = not prime)
            for i in range(st_no * st_no, num + 1, st_no):
                prime_list[i] = False # change the state to false for the multiples of st_no foe each iterations
        st_no += 1
    
    collect_prime = [p for p in range(2, num+1) if prime_list[p]] # collects the prime numbers having state as False in a list

    return collect_prime


def check_prime(num: int):
    if num < 2:
        return False
    
    get_prime = find_prime(num) # gets all the prime numbers

    return num in get_prime # returns true if the number exists in the list


if __name__ == '__main__':
    ip_no = int(input("Enter the number: "))
    ip_list = input(f"Yes: Need prime numbers from 0 to {ip_no}\nNo: Check {ip_no} is a prime number\nType Yes or No\n").lower()

    if ip_list == 'yes':
        result = find_prime(ip_no)
        print(f"The list of prime numbers form 0 to {ip_no} is:\n{result}")

    if ip_list == 'no':
        if check_prime(ip_no):
            print(f"{ip_no} is a prime number")
        else:
            print(f"{ip_no} is not a prime number")