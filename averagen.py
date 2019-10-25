print('Please input 5 numbers:')
N=5
sum=0
count=0
while count < N:
    number=float(input())
    sum=sum+number
    count=count + 1
averagen=sum/N
print("相加的和是{}".format(sum))
print("平均数是{:.2f}".format(averagen))
