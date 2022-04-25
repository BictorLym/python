
#원의 넓이 계산
def circleArea(radius):
    global PI
    PI = 3.141592
    area = PI * radius **2
    print(f'반지름이 {radius}인 원의 면적: {area}')

#원의 둘레계산
def circleCircumference(radius):
    
    length = 2* PI * radius
    print(f'반지름이 {radius}인 원의 둘레: {length}')


x = 5;    
circleArea(x)
circleCircumference(x)
