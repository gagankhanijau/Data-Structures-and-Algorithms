
#mirror tree

def isMirrorUtil(l,r):
	if not l and not r:
		return True
	if not r:
		return False
	if not l :
		return False
	return l.val==r.val and isMirrorUtil(l.l,r.r) and isMirrorUtil(l.r,r.l)

def isMirror(root):
	if not root:
		return True
	return isMirrorUtil(root.left, root.right)


#---------------------------------------------------------------------------------------
#min depth of bin tree


def minDepth(root):
	if not root:
		if not root.left and not root.right:   
			return 1
		if not root.left:
			return 1+minDepth(root.right)
		if not root.right:
			return 1+minDepth(root.left)
		return 1+min(minDepth(root.left), minDepth(root.right))
	return 0

########################################################################################
#column wise traversal



def colTraversal(root):
	queue=[root]
	cols_qu=[0]
	cols=dict()
	min_col, max_col=sys.maxint, -1*sys.maxint 
	while queue:
		temp= queue.pop(0)
		temp_col= cols_qu.pop(0)
		if min_col>temp_col:
			min_col= temp_col
		if max_col<temp_col:
			max_col= temp_col
		cols[temp_col] = cols.get(temp_col,[]).append(temp.val)

		if temp.left:
			queue.append(temp.left)
			cols_qu.append(temp_col-1)
		if temp.right:
			queue.append(temp.right)
			cols_qu.append(temp_col+1)

	for i in range(min_col,max_col+1):
		print cols[i]



########################################################3 sum
def twoSum(arr,num):
	res=[]
	hashmap=dict()
	for i in arr:
		hashmap[i]=1
	for i in arr:
		if hashmap.get(num-i,0) :
			res.append((i,num-i))
	return res
def threeSum(arr,num):
	res=[]
	hashmap=dict()
	for i in arr:
		hashmap[i]=hashmap.get(i,0)+1
	for i in arr:
		hashmap[i]=hashmap.get(i,0)-1
		for j in arr:
			hashmap[j]=hashmap.get(j,0)-1
			if hashmap.get(num-i-j,0) :
				res.append([i,j,num-i-j])
			hashmap[j]=hashmap.get(j,0)+1
		hashmap[i]=hashmap.get(i,0)+1
	return res

# res=threeSum([5, 6, -2, 4, 3, 5, 1, 9, 0, -5, 2, 1], 7)
# for i in res:
# 	print i 



###############################################################################


def dom_parser(input_str):
	output=''
	tabs= -1
	is_tag=False
	tag=''
	for i in input_str:
		if i =='<':
			is_tag=True
			tabs+=1
		elif i=='>' and is_tag:
			print ''.join(['\t' for x in range(tabs)])+tag
			tag=''
			is_tag=False
		elif i=='/' and is_tag:
			tabs-=2
			is_tag=False
		elif is_tag:
			tag+=i
		else:
			continue			

input_str= '<html>dfsf<p>dfdsf</p></html'
input_str1= '<a><b></b>osfidgj<p><p></p></p></a>'
dom_parser(input_str)
print "\n"
dom_parser(input_str1)





















