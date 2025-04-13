#first def
def faktorial(n):
    value = float(1)
    for i in range(1, n+1):
        value = value * i
    return value
#second def
def powr(x,y):
    return x**y
#third
def sin_1(degree):
    if(degree == 0):
        print("The sin of degree(0)= 0")
    elif(degree == 90):
        print("The sin of degree(90)=1")
    elif(degree == 180):
        print("The sin of degree(180)=0")
    elif(degree == 270): 
        print("The sin of degree (270)=-1")
    elif(degree == 360):
        print("The sin of degree (360)= 0")
    else:
        x = degree
        x = x * 3.14/180
        value = x
        sign = -1
        n = 200 # precision
        i = 3
        while i < n:
            value = value + (powr(x, i)/faktorial(i) * sign)
            i = i + 2
            sign = sign * -1
        return value

def cos_1(degree):
    if(degree == 0):
        print("The cos of degree(0)= 1")
    elif(degree == 90):
        print("The cos of degree(90)=0")
    elif(degree == 180):
        print("The cos of degree(180)=-1")
    elif(degree == 270): 
        print("The cos of degree (270)=0")
    elif(degree == 360):
        print("The cos of degree (360)= 1")
    else:
        x=degree
        "The calculation of pi * degree?"
        "I have browsed on the internet.."
        x = x * 3.14/180
        value = 1
        sign = -1
        n = 200 # precision
        i = 2
        while i < n:
            value = value + (powr(x, i)/faktorial(i) * sign)
            i = i + 2
            sign = sign * -1

        return value

cos_1(0)