def fibbo(n):
    global f
    if (n == 0 or n == 1):
        return n
    elif(f[n] != -1):
        return f[n]
    f[n] = fibbo(n-1)+fibbo(n-2)
    return f[n]


n = int(input("Enter the value: "))
global f
f = [-1]*(n+1)
f[0] = 0
f[1] = 1
print("Fibonacci Sequence:  ", end="")
fibbo(n)
for i in f:
    print(i, end=" ")
print()
