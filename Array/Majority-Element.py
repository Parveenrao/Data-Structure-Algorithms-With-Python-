# Find the element that appears more than ⌊n/2⌋ times. in array 

from typing import List

# Bruter force Approach -> Hashmap / dict   Iterate through the array and store its count , and then return the no who has count more then n/2


class Solution:
    def majority(self , nums:List[int]) -> int:  
        
        n = len(nums)            
        
        freq = {}
        
        for x in nums:
            
            freq[x] = freq.get(x , 0) + 1
            
        for num , count in freq.items():          # Time Complexity O(n)  -> Iterate through the array 
            
            if count > n /2:                      # Space complexity because we take extra space O(n) 
                return num    
            

# Optimal Approach  --> Boyer- Moore - Voting Algorithm 
  
"""  keep two variables candidate and count 
       if count == 0  -> pick new candidate 
       if same number appers --> count += 1
       if different number  -> count -= 1"""
       
       
class Solution:
    def majority(self, nums:List[int]) -> int:         
        
        count = 0 
        candidate = None
        
        for num in nums:
            
            if count == 0:
                candidate = num 
                
            if num == candidate:
                count += 1
            
            else:
                count -= 1
        
        return candidate

if __name__ == "__main__":
    sol = Solution()
    print(sol.majority([2,2,1,1,1,2,2]))  # 2                           
            
            
            
            
