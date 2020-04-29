def fibo(n):
    if n<=1:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))
nterms=int(input("how many terms" ))
#first two terms
n=0,1
count=0
if nterms<=0:
 print("enter a positive interger")
else:
 print("Fibonacci sequence")
 for i in range(nterms):
    print(fibo(i))


