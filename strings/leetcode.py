# running sum of numbers
def runningSum(nums,self):
    for i in range(1,len(nums)):
        nums[i] += nums[i-1]
    return nums
    