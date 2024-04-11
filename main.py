from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    # YOUR ANSWER
    temp = []
    for i in range (len(nums)):
        for j in range (len(nums)):
            if j > i :
                if(nums[i] + nums[j]) == target:
                    temp.append(i)
                    temp.append(j)
                    break
            else:
                continue
            
    return temp

tmp = eval(input())
t = int(input())
ret = twoSum(tmp,t)
print(ret)