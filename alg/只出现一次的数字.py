#-*-coding：utf8-*-
"""
author:xiaofan
date:2019
"""

#给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#说明：
#你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

#输入: [4,1,2,1,2]
#输出: 4

def singleNumber(nums):
    count = 0
    for index_i in range(0,len(nums)):
        for index_j in range(0,len(nums)):
            count += 1
            if index_i==index_j:
                count = 0
                continue
            if nums[index_i]==nums[index_j]:
                count = 0
                break
            if(count==(len(nums)-1)):
                return index_i

if __name__ =="__main__":
    #nums = [4,1,2,1,2]
    nums =  [2,2,1]
    index = singleNumber(nums)
    print(nums[index])
