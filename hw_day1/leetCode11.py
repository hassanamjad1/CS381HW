'''
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
'''

height = [1,8,6,2,5,4,8,3,7]


def maxArea(height):
  leftMax = height[0]
  rightMax = height[0]
  start = 0
  end = len(height)-1
  mid = len(height) // 2
  while end > mid:
    if rightMax < height[end]:
      rightMax = height[end]
    end = end-1
  while start < mid:
    if leftMax < height[start]:
      leftMax = height[start]
    end = end-1

  if rightMax > leftMax:
    return leftMax
  else:
    return rightMax

print(maxArea(height))
  
    



  
