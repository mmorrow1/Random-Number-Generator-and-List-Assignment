#Matt Morrow spcID2412353 COURSE: COP1000
#Statement 1: create random numbers between 1 and 25
#Statement 2: sort the numbers
#Statement 3: display in values
#Statement 4: display values in order
#Statement 5: Determine odds/evens and display


import random

def main():

    nums = []

    for value in range(10):
        nums.append(random.randint(1,25))
        numbers = sorted(nums)
        
    for x in range(1):
        
        print(*nums)
        print(*numbers)

        start = numbers[:4]
        print(start)
        finish = numbers[-5:]
        print(finish)

        odd_even(numbers)
        
def odd_even(numbers):
    
    even_count = 0
    
    odd_count = 0
    
    for val in numbers:
        if val % 2 == 0:
            even_count += 1
        if val % 2 != 0:
            odd_count += 1

    print("List had" + ' ' + str(even_count) + ' ' + "evens and" + ' ' + str(odd_count) + ' ' + "odds")
    
    print("The 6th element in sorted nums is" + ' ' + str(numbers[5]))


    

    
        
main()


    
