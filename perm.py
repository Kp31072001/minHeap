import sys


def main():
	print("main code", sys.argv[1])
	x = [i+1 for i in xrange(int(sys.argv[1]))]
	getPerm(x,1,int(sys.argv[1])) #This will gen all perms starting from 2 to n

	


def swap(arry,i,j):
	tmp = arry[i]
	arry[i] = arry[j]
	arry[j] = tmp


def getPerm(arry,start,end):
	
	if(start == end):
		print(arry , checkMinHeap(arry,0,len(arry)))
		return 
	
	getPerm(arry,start+1,end)
	
	for i in xrange(start+1,end):
		if(arry[start] == arry[i]):
			continue
		swap(arry,start,i)
		getPerm(arry,start+1,end)
		swap(arry,start,i)


def checkMinHeap(arry,i,n):
	if (2*i+2 > n):
		return True


	left = (arry[i] <= arry[2*i +1]) and checkMinHeap(arry, 2*i + 1 , n)
	right = (2*i + 2 == n) or (arry[i] <= arry[2*i + 2] and checkMinHeap(arry, 2*i + 2,n))

	return left and right
	

if __name__ == "__main__":
	main()
