class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict={}
        count={}
        for i in nums:
            if i not in nums_dict:
                nums_dict[i]=1
            else:
                nums_dict[i]+=1
        

        for value in nums_dict.values():
            if value>1:
                return True
        return False        