class Solution:
    def searchInsert(self,nums,target):
        si=0
        li=len(nums)-1
        while si<=li:
            mid=(si+li)//2
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                si=mid+1
            else:
                li=mid-1
        return si
s=Solution()
print(s.searchInsert([1,3,5,6],2))