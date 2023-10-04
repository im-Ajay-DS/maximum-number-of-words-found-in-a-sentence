class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans=[]
        for i in sentences:
            count=0
            for j in i:
                if j ==' ':
                    count=count+1
            ans.append(count+1)
        return(max(ans))
