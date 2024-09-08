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


def collect_prime_factors(num: int):
    get_prime_no = find_prime(num)
    prime_factors = []

    for i in get_prime_no:
        while num%i == 0:
            prime_factors.append(i)
            num //= i

    return prime_factors
    

if __name__ == '__main__':
    ip_no = int(input("Enter the number to get prime factors: "))
    print(f"The prime factors of {ip_no} is: {collect_prime_factors(ip_no)}")