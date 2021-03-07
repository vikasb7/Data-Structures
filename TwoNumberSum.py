'''
Vikas Bhat
Two Sum
Time Complexity o(N)
'''


class Practice:

    def twoSum(self,lis,target):
        i=0
        j=len(lis)-1
        sorted(lis)
        d={}

        for x,y in enumerate(lis):
            d[y]=x

        while i<=j:

            curr=lis[i]+lis[j]
            if curr==target:

                return [d[lis[i]],d[lis[j]]]
            elif curr < target:
                i+=1
            else:
                j-=1


        return 0


if __name__=="__main__":
    vik=Practice()
    print(vik.twoSum([3, 5, -4, 8, 11, 1, -1, 6],10))





