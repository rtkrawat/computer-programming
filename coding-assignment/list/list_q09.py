# Given an array arr, you need to reverse a subarray of that array. The range of this subarray is given by indices L and R (1-based indexing).
def reverseSubArray(self,arr,l,r):
		p=arr[:l-1]
		q=arr[r:]
		k=arr[l-1:r]
		k.reverse()
		return p+k+q
