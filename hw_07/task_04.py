nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,19,22]
def nums_calc():
    sum=0
    for i in nums:
        if i % 2== 0:
         sum +=i
    print(sum)
nums_calc()