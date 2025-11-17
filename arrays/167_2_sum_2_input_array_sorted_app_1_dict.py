class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        visited={}
        for idx in range(len(numbers)):
            complement=target-numbers[idx]
            if complement in visited:
                return [visited[complement]+1,idx+1]
            else:
                visited[numbers[idx]]=idx
    