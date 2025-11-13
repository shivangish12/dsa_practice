class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        area=0
        while(left<right):
            set_area=min(height[left],height[right])*(right-left)
            if(area<set_area):
                area=set_area
            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
        return area

