import heapq
from heapq import heappop, heappush
 
def Knapsack(arr,weights,no,w):
    selected_index = []
    minwt= 4 
    maxval = 0 
    for i in range(0,no):
        for j in range(0,i):
            #print(i,j)
            if weights[i] + weights[j]  <= w and arr[i] + arr[j]> maxval:
                    minwt = weights[i] + weights[j]
                    maxval = arr[i] + arr[j]
                    print("For i and j ", i ,j,maxval,minwt)

    print(minwt,maxval)

    for n in range(0, len(selected_index)):
        selected_index[n]

            
def Knapsack1(arr,wt,w):
    min_val = 0 
    max_cal = float('inf')


    for i in range(len(arr)):
        for j in range(i+1):
        
            if j < len(arr)-1:
                #print(arr[i],arr[j], wt[i] + wt[j])

                if arr[i] + arr[j] > min_val and  wt[i] + wt[j] <= w :
                    min_val=  arr[i] + arr[j]
                    print(arr[i],arr[j],min_val, wt[i] + wt[j])


        



if __name__ == '__main__':
 
    arr = [10, 20, 30, 40]
    weight = [1,2,3,4]
    w= 9
    Knapsack1(arr,weight,w)
    