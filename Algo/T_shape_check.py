"""
The first line contains the number of test cases T. Each test cases has five lines containing two non-negative integers x and y separated by a single space. Points in the same test case are all distinct.

Constraints

1 ≤ T ≤ 500
0 ≤ x ≤ 106
0 ≤ y ≤ 106
Output Format

For each test-case, output Yes if they form T-shaped or No if they don't form T-shaped in a new line.

Sample Input 0

1
7 5
8 5
6 5
7 6
7 7
Sample Output 0

Yes
Explanation 0

The given coordinate points form a close T-shape, hence the output is YES

"""



def groupby_occurence(item,indx):
	#[(1,2),(2,2),(1,3)], 1 --> [2:2,3:1]
	d={}
	for i in item:
		if i[indx] in d:
			
			d[i[indx]]+=1
		else:
			
			d[i[indx]]=1
	return d

def three_times_cord(item):
	key=0
	for i in item.items():
		if i[1]==3:
			key=i[0]
	return key 
def straight_line_validation(d,key):
	cnt=2
	for i in d.items():
		if i[0]- key in [1,2]:
			cnt+=1
		elif key - i[0] in [1,2]:
			cnt-=1
	if cnt in [0,4]:
		print("Both the points arestraightline")
		return True
	else:
		print("Both the Points are either side")
		return False
def T_line_validation(d,key):
	cnt=0
	for i in d.items():
		if i[0] - key == 1:
			cnt+=1
		elif key - i[0] == 1:
                        cnt-=1
	if cnt == 0 :
                print("Both the points are sides of T ")
                return True
        else:
                print("Both the Points not abve and below")
                return False


def chec_T(c):
	res=False
	#Y Axis : make a group of points based on count 
	d=groupby_occurence(c,1)
	#Find the common point between both lines 
	key=three_times_cord(d)
	#find the Line points on straight line i
	print(key,d)
	if key:
		res=straight_line_validation(d,key)
	
	#X Axis : make a group of points based on count 
	d=groupby_occurence(c,0)
	#Find the common point between both lines 
	key=three_times_cord(d)
	#find the Line points on straight line 
	print(key,d)
	if key:
		res=T_line_validation(d,key)
	
	#handle when the T is oriented in X direction 

	if not res:
		#Y Axis : make a group of points based on count 
		d=groupby_occurence(c,0)
		#Find the common point between both lines 
		key=three_times_cord(d)
		#find the Line points on straight line 
		if key:
			res=straight_line_validation(d,key)
		
		#Y Axis : make a group of points based on count 
		d=groupby_occurence(c,1)
		#Find the common point between both lines 
		
		key=three_times_cord(d)
		#find the Line points on straight line 
		if key:
			res=T_line_validation(d,key)

	return res


if __name__=="__main__":
	c=[(7,5),(8,5),(6,5),(7,6),(7,7)]
	#c=[(0,1),(1,1),(2,1),(2,2),(2,0)]
	#c=[(0,2),(0,1),(0,0),(1,1),(2,2)]
	#c=[(0,2),(0,1),(0,0),(1,1),(2,2)]

	
	print(chec_T(c))


