class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        overlapping_items = []
        overlapping = False
        for i in intervals:
            print(i)
            print(i[0],new_interval[0],new_interval[1],i[1])
            if i[1] > new_interval[0] and new_interval[1] > i[0]:
                overlapping = True
                overlapping_items.append(i)


        if  overlapping :
            print("overlapping",overlapping_items)
            i= min(overlapping_items[0][0],new_interval[0])
            j= max(overlapping_items[len(overlapping_items)-1][1],new_interval[1])
            print(i,j)
            t=[i,j]


        for i in intervals:
            if i[1] > new_interval[0] and new_interval[1] > i[0] :
                new_interval.pop(i)
              
 
    

if __name__=="__main__":
        L=Solution()
        L.insert([[1,3],[4,5],[6,9]],[2,5])
        