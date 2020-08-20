def sum_of_nums(nums):
    global sum
    nums = list(nums.split())
    for count, i in enumerate(nums):
        try:
            i = int(i)
        except ValueError:
            if "Q" in i or "q" in i:
                nums[count] = "Q"
                pass
            else:
                nums[count] = 0
    for i in nums:
        if i == "Q":
            print(sum)
            print('Работа программы завершена!')
            return sum
        sum += int(i)
    print(sum)
    sum_of_nums(input())

sum = 0
sum_of_nums(input())
