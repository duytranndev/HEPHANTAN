# import math
# # CAU 1
# a = int(input("Nhap so nguyen to A: "))
# b = int(input("Nhap so nguyen to B: "))

# if a>b:
#     print("A max")
# else:
#     print("B max")

# #CAU 2
# canh_a = int(input("Nhap canh A: "))
# canh_b = int(input("Nhap canh B: "))
# canh_c = int(input("Nhap canh C: "))

# chuvi = canh_a+canh_b+canh_c
# print("Chu vi: "+str(chuvi))
# p = chuvi*1/2

# dien_tich = math.sqrt(p*(p-canh_a)*(p-canh_b)*(p-canh_c))

# print("Dien tich: " +str(dien_tich))

# #CAU 3

# if canh_a !=0 and canh_b !=0 and canh_c != 0:
#     if canh_a+canh_b>canh_c or canh_a+canh_c>canh_b or canh_b+canh_c>canh_a:
#         print("Day la 1 tam giac")
# else:
#     print("day khong phai la 1 tam giac")



#Cau 4
isOK = True
while isOK:
    canh_a = float(input("nhap a "))    
    canh_b = float(input("nhap b "))
    canh_c = float(input("nhap c "))

    if canh_a !=0 and canh_b !=0 and canh_c != 0:
        if canh_a+canh_b>canh_c and canh_a+canh_c>canh_b and canh_b+canh_c>canh_a:
            print("day la 1 tam giac")
            break
    else:
        isOK = True  
    if isOK: 
        print("day khong la 1 tam giac, moi nhap lai") 

#
    
    
