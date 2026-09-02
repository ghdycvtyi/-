import sys
import sys
def find_biggest(num):
    l=len(num)
    start_l=0
    end_l=0
    r=-float('inf')
    d=0
    l1=0
    for i in range(l):
        if d>=0:
            d+=num[i]
        else:
            d=num[i]
            l1=i
        if d>r:
            r=d
            start_l=l1
            end_l=i
    if r<=0:
        return(0,-1,-1)
    else:
        return(r,start_l,end_l)
def main():
    nums=list(map(int,sys.stdin.read().split()))
    p=0
    res=[]
    while p<len(nums):
        n=nums[p]
        p+=1
        num=nums[p:p+n]
        p+=n
        r,sl,el=find_biggest(num)
        res.append(f"{r} {sl} {el}")
    print(''.join(res))
if __name__=='__main__':
    main()
