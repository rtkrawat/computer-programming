# You are given an array arr[], and you have to re-construct an array arr[].
#The values in arr[] are obtained by doing Xor of consecutive elements in the array.
def game_with_number (arr,  n) : 
    k=[]
    for i in range(len(arr)):
        if i==len(arr)-1:
            k+=[arr[i]]
        else:
            k+=[arr[i]^arr[i+1]]
    return k
