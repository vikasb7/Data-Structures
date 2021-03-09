'''
Vikas Bhat
Restored a Shuffled String
Time Complexity o(N)
'''



class Practice:

    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        lis = ["a"] * len(indices)

        for i in range(len(s)):
            lis[indices[i]] = s[i]

        ans = ""
        for i in lis:
            ans += i

        return ans


if __name__=="__main__":
    vik=Practice()
    s = "asvik"
    indices = [3, 4, 0, 1, 2]
    print(vik.restoreString(s,indices))





