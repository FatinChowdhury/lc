class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # make a new array for output
        # loop through input array
        # if temperatures[i+1] - temperatures[i] > 0 then return 1
        # then append it to array
        # else i+=1 then return updated position minus start
        # append that updated position - start to array
        # nope this approach is not it
        res= [0] * len(temperatures)
        stack=[]

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i-stackInd)
            stack.append([t,i])
        return res
