class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        #if the lists are not overlapping they can be added and the median can be calculated
        if nums1 == []:
            half = int(len(nums2) / 2) 
            if len(nums2) % 2 == 0:
                return (nums2[half - 1] + nums2[half]) / 2
            else:
                return nums2[half]
        
        if nums2 == []:
            half = int(len(nums1) / 2) 
            if len(nums1) % 2 == 0:
                return (nums1[half - 1] + nums1[half]) / 2
            else:
                return nums1[half]
                
        if nums1[-1] <= nums2[0]:
            nums = nums1 + nums2
            half = int(len(nums) / 2) 
            if len(nums) % 2 == 0:
                return (nums[half - 1] + nums[half]) / 2
            else:
                return nums[half]
            
        elif nums2[-1] <= nums1[0]:
            nums = nums2 + nums1
            half = int(len(nums) / 2) 
            if len(nums) % 2 == 0:
                return (nums[half - 1] + nums[half]) / 2
            else:
                return nums[half]
            
        #if the lists are overlapping
        else:
            #check which list is the shorter one of if they are equal
            if len(nums1) <= len(nums2):
                A = nums1 # A is shorter
                B = nums2 
            else:
                A = nums2
                B = nums1

            lA = len(A) #length of smaller list
            lB = len(B) #length of bigger list
            lAB = lA + lB #length of combined list

            #starting point is the position of the first element of the smaller list
            start = 0  
            #end point is the length of the smaller list 
            end = lA
            #define median
            median = None

            while start <= end:
                #number of elements on left side after splitting the smaller list
                partition_A = (start + end) // 2 
                #number of elements on left side after splitting the bigger list 
                partition_B = ((lAB + 1) // 2 - partition_A) 
                
                #define the max of left parts and mins of right parts
                if partition_A == 0:
                    max_leftA = float('-inf') 
                else:
                    max_leftA = A[partition_A-1] 
                if partition_B == 0:
                    max_leftB = float('-inf')
                else:
                    max_leftB = B[partition_B-1]
                if partition_A == lA:
                    min_rightA = float('inf')
                else:
                    min_rightA = A[partition_A]
                if partition_B == lB:
                    min_rightB = float('inf')
                else:
                    min_rightB = B[partition_B]

                #check current condition to see if median can be calculated
                #if max_leftA is smaller or equal to min_rightB and max_leftB 
                #is smaller or equal to min_rightA then if the total length
                #is even the median has to be between the bigger number of the
                #left parts and the smaller number of the right parts if the
                #total length is odd the median is the bigger number of the 
                #left parts
                if (max_leftA <= min_rightB) and (max_leftB <= min_rightA):
                    if lAB % 2 == 0:
                        median = float((max(max_leftA,max_leftB) + min(min_rightA,min_rightB)) / 2)
                        break
                    else:
                        median = float(max(max_leftA,max_leftB))
                        break
                        
                #if the first condition is not satisfied and max_leftA is 
                #bigger than min_rightB, the partition is too far on the 
                #right side and has to move one step to the left for the 
                #next loop
                elif max_leftA > min_rightB:
                    end = partition_A-1
                    
                #if its smaller it has to move to the right side
                else:
                    start = partition_A+1
                    
            return median



