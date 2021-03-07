'''
Vikas Bhat
Validate Sequences (Lists)
Time Complexity o(N)
'''


class Practice:

    def isValidSubsequence(self,array, sequence):
        # Write your code here.
        i=0
        j=0

        while i<len(array) and j<len(sequence):

            if array[i]==sequence[j]:
                j+=1
            i+=1

        return j==len(sequence)


if __name__=="__main__":
    vik=Practice()
    print(vik.isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10],[1, 6, -1, 10]))





