class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n==1:
            return 1
        left,right=1,n
        while(left<right):
            mid=(left+right)//2
            if isBadVersion(mid):
                right=mid
            if not isBadVersion(mid):
                left=mid+1
        return left
            