class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums={}
        n=len(nums)
        buckets=[0]*(n+1)
        ret=[]
        for i in nums:
            if i not in dict_nums:
                dict_nums[i]=1
            else:
                dict_nums[i]+=1
            
        for key,value in dict_nums.items():
            if buckets[value]==0:
                buckets[value]=[key]
            else:
                buckets[value].append(key)

        for i in range(n,-1,-1):
            if buckets[i]!=0:
                ret.extend(buckets[i])
            if len(ret)==k:
                break
        return ret

        # https://www.youtube.com/watch?v=phNDYf1xzco

            

