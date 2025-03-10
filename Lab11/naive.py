class Naive:
    def __init__(self):
        pass

    @staticmethod
    def intersection(list1,list2):
        sum=0
        for i in list1:
            for j in list2:
                if i==j:
                    sum=sum+1
        return sum

    def run(self,corpus,c:float):
        ans=set()
        for i in range(len(corpus)-1):
            for j in range(i+1,len(corpus)):
                inter=self.intersection(corpus[i],corpus[j]) 
                union=len(corpus[i])+len(corpus[j])-inter 
                if inter>=c*union:
                    ans.add((i,j))
        return ans

