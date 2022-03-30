def Merge(arr, s,m,e):

	ne = e - m # Right length : (5 - 3) = 2   
	ns = m - s + 1 #left length : 3-0= 3 is wrong so to compensate the 0 index + 1 is added 

	#create Size of items 
	R = [0] * ne
	L = [0] * ns
	#print("arr, s,m,e", arr, s,m,e)
	#print("ns , ne ", ns , ne)

	#R is always greater tehn L by + 1
	for i in range(0,ne):
		R[i] = arr[m + i + 1]
		#ran
	for i in range(0, ns):
		L[i] = arr[i + s] 
	print("R,L",R, L )

	i = 0     # Initial index of first subarray
	j = 0     # Initial index of second subarray
	k = s     # Initial index of merged subarray

	#Set the L And R subarrays arrays with the k value fo main array 
	# Till our Subarrays are full 
	while i < ns and j < ne:
		#print("Li",L, i, "Rj", R ,j,"k", k, "ns, ne",ns , ne)
		if L[i] >= R[j]:
			arr[k] = R[j]
			j += 1
		else:
			arr[k] = L[i]
			i += 1
		k += 1
	
	#Set the left over items as they are already sorted and needs to be  stored 
	#Set 
	print("Left overs ")
	while i <  ns:
		print(L[i])
		arr[k] = L[i]
		i+=1
		k+=1
		
	#While the j < ne
	while j <  ne:
		print(R[j])
		arr[k] = R[j]
		j+=1
		k+=1
		
		   
def MergeSort(arr, s,e):
	#print(s,e)
	if s < e:
		m = s+ (e - s)//2 
		#print("middle",m)
		
		MergeSort(arr,s,m)
		MergeSort(arr,m+1,e)
		Merge(arr,s,m,e)



# Function to find a pair in an array with a given sum using hashing
if __name__=="__main__":
        
        arr = [64, 34, 25, 12, 22, 11, 90]
		
        L= MergeSort(arr,0 ,len(arr)-1)
        print(arr)
