a = 0;
b = 1;
c = 1;
sum = 0;
result = 0;

while(sum <4000000):
    sum = a+b;
    a=b;
    b=sum;
    if c%2==0:
        result+=sum;
    c+=1;

print(result)
