class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                    if nums[x]+nums[y] == target:
                        return [x,y]

#Finallly my first leetcode OMG ive such a long way to go, by well i got it working and i am happy with it. Did use chatgpt to help in last test since i wasnt able to figure
#out how to solve the duplicate issue. But i am happy with the result.
#Learningfrom this is that i need to learn more about python and its libraries and also need to learn more about the data structures and algorithms. And list.index uses () not []