def prime_checker(number):
    is_prime = True
    for nums in range(2, number):
        if number % nums == 0:
            is_prime = False
    if is_prime == True:    
        print("This is a prime number.")
    else:
        print("This is not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)


