class complex():
    def __init__(self,real,image):
        self.real=real
        self.image=image
def qiuhe(a,b):
    r=a.real+b.real
    i=a.image+b.image
    return complex(r,i)
def xiangjian(a,b):
    r=a.real-b.real
    i=a.image-b.image
    return complex(r,i)
def xiangcheng(a,b):
    r=a.real*b.real-a.image*b.image
    i=a.real*b.image+a.image*b.real
    return complex(r,i)
def panduan(a):
    f=1
    if a.real==0 and a.image!=0:
        print(f'纯虚数:{a.image}i')
    elif a.image==0:
        print(f'实数:{a.real}')
        f=0
    else:
        print(f'普通虚数:{a.real}+{a.image}i')
    return(f)
def qiumo(a):
    r=(a.real**2+a.image**2)**0.5
    return(r)
def shuchu(a,b):
    panduan(a)
    panduan(b)
    print(f'第一个模：{qiumo(a)}')
    print(f'第二个模：{qiumo(b)}')
    w=qiuhe(a,b)
    print(f'求和为：{w.real}+{w.image}i')
    w=xiangjian(a,b)
    print(f'相减为：{w.real}+{w.image}i')
    w=xiangcheng(a,b)
    print(f'相乘为：{w.real}+{w.image}i')
def main():
    print('请输入两个虚数:')
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    x=complex(a,b)
    y=complex(c,d)
    shuchu(x,y)
if __name__=="__main__":
    main()




    
