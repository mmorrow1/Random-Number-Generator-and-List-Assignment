import random

def main():

    if __name__ == "__main__":
        nums = []
    for val in range(10):
        nums.append(random.randint(1,25))
        print(*nums)
        nums = sorted(nums)
        print(*nums)
        start = nums[:4]
        print(start)
        finish = nums[-5:]
        print(finish)
def odd_even(nums):
    even_count = 0
    odd_count = 0
    for val in nums:
        if val % 2 == 0:
            even_count+=1
    else:
        odd_count+=1
        print("List had" + ' ' + str(even_count) + ' ' + "evens and" + ' ' + str(odd_count) + ' ' + "odds")
        odd_even(nums)
        print("The 6th element in sorted nums is" + ' ' + str(nums[6]))
main()
