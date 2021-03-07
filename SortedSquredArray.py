'''
Vikas Bhat
Sorted Squred Array
Time Complexity o(N)
'''



class Practice:

    def sortedSquaredArray(self,lis):
        # Write your code here.

        for i in range(len(lis)):
            lis[i]*=lis[i]

        return sorted(lis)





if __name__=="__main__":
    vik=Practice()
    print(vik.sortedSquaredArray([1, 2, 3, 5, 6, 8, 9]))





