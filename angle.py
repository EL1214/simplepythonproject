import math 
x1 = float(input("Enter x1: ")) 
x2 = float(input("Enter x2: ")) 
y1 = float(input("Enter y1: ")) 
y2 = float(input("Enter y2: "))

a = float(x2-x1) 
b = float(y2-y1) 
if a <= 0 or b <= 0 : 
    print("The value is not defined.")
else: 
    if b > a : 
        t = a/b 
    else: 
        t = b/a
    sum = 0.0
    i = 1
    sign = 1
    summand = 1.0
    t_squared = t*t
    while summand <= -0.000001 or summand >= 0.000001:
        summand = sign * 1/i * t
        sum = sum + summand
        sign = -sign
        i = i + 2
        t = t*t_squared
        
    if b > a :
        final_sum = math.pi / 2 - sum
        if final_sum > math.pi / 4 and final_sum <= math.pi / 2 :
            angle_in_degree = math.degrees(final_sum)
            print("The angle is:", angle_in_degree) 
        else :
            print("The angle is out of range for Case 2")  
    else :
        final_sum = sum
        if final_sum >= 0 and final_sum <= math.pi / 4 :
            angle_in_degree = math.degrees(final_sum)
            print("The angle is:", angle_in_degree)
        else :
            print("The angle is out of range for Case 1")
