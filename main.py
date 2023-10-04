from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
  # YOUR ANSWER
  

  
  for first in range(0, len(nums)):
    for second in range(first+1, len(nums)):
      sum = nums[first] + nums[second]
      if sum == target:
        print("[", first, ",", second, "]")
        break
  
  return