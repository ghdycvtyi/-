def f(n,l,x):
    r=l[0]
    d=1
    for i in range(n):
        d*=x
        r+=l[i+1]*d
    return r
def main():
    n=int(input())
    l=list(map(float,input().split()))
    x=float(input())
    r=f(n,l,x)
    print(f"{r:.2f}")
if __name__=="__main__":
    main()
