'''
Vikas Bhat
Search in Rotated Sorted Array
Time Complexity o(logN)
'''


class Practice:

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l = 0
        r = len(nums) - 1

        while (l <= r):

            print("l is : ", l)
            print("r is :", r)
            m = (l + r) // 2
            print("m is :iuuv", m)

            if (nums[m] == target):
                return m

            if (target >= nums[0]):
                if nums[m] >= nums[0] and target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m] >= nums[0] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1

        return -1


if __name__=="__main__":
    vik=Practice()
    print(vik.search([4,5,6,7,0,1,2],0))






