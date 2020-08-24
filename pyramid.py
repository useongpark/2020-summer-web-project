def drawPyramid(num):
    for i in range(1, num+1):
        print(" "*(num-i), "*"*(2*i-1))

num = int(input("Type a number: "))
drawPyramid(num)

