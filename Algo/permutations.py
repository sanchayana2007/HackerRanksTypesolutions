def permute(elements):
	
	if len(elements) <=1:
		yield elements
	else:
		for perm in permute(elements[1:]):
			for i in range(len(elements)):
				# nb elements[0:1] works in both string and list contexts
				yield perm[:i] + elements[0:1] + perm[i:]
		


if __name__=="__main__":
	a=['A','B','C']
	
	for i in permute(a):
		print(i)
	
		
	
	
	#
