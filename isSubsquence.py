'''
Vikas Bhat
Validate Sequences (Strings)
Time Complexity o(N)
'''



class Practice:

    def isValidSubsequence(self,str1, str2):
        # Write your code here.
        i=0
        j=0

        while i<len(str1) and j<len(str2):
            if str1[i]==str2[j]:
                j+=1
            i+=1

        return j==len(str2)




if __name__=="__main__":
    vik=Practice()
    s = "abc"
    t = "ahbgdc"
    print(vik.isValidSubsequence(t,s))





