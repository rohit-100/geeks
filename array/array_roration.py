n,k = map(int,input().split())
arr =list( map(int,input().split()))
#print (arr)
#print (n)
#print (k)
#def fun(n,k,arr):
#	while k:
#		temp = arr[0]
#		for i in range(1,n):
#			arr[i-1]=arr[i]
#		arr[-1]=temp
#		k-=1
#	print (arr)
#fun(n,k,arr)

##   REVERSAL ALGO TO REVERSE A ARRAY
##   REVERSE 1 - K
##   REVERSE K+1 - N
##   REVERSE 1 - N
def reverse(arr,a,b):
	while a<b:
		temp = arr[a]
		arr[a]=arr[b]
		arr[b]=temp
		a+=1
		b-=1
def rotate(arr,n,k):
	reverse(arr,0,k-1)
	reverse(arr,k,n-1)
	reverse(arr,0,n-1)
rotate(arr,n,k)
print (arr)
