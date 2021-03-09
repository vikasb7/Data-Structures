class Practice:
    def tournamentWinner(self,competitions, results):
        # Write your code here.

        d = {}

        for i in range(len(competitions)):
            if (results[i] == 0):
                if(competitions[i][1] not in d):
                    d[competitions[i][1]]=1
                else:
                    d[competitions[i][1]] = d[competitions[i][1]]+1

            else:
                if(competitions[i][0] not in d):
                    d[competitions[i][0]]=1
                else:
                    d[competitions[i][0]] = d[competitions[i][0]]+1

        ans= max(d, key=d.get)

        return ans

if __name__=="__main__":
    vik=Practice()
    comp=[
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
]
    winner=[0, 0, 1]
    print(vik.tournamentWinner(comp,winner))