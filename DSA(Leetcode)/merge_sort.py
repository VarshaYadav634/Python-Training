# mergesort
 
def merge(l,si,mid,li):
    left=l[si:mid+1]
    right=l[mid+1:li+1]
    i=0
    j=0
    k=si
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            l[k]=left[i]
            i+=1
        else:
            l[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        l[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        l[k]=right[j]
        j+=1
        k+=1
def mergesort(l,si,li):
    if si<li:
        mid=(si+li)//2
        mergesort(l,si,mid)
        mergesort(l,mid+1,li)
        merge(l,si,mid,li)
l=[7,2,1,3,4,6,5]
mergesort(l,0,len(l)-1)
print(l)
 
 