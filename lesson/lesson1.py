# full_name =input("Nhap ho va ten: ")
# print('ho va ten: ',full_name)
 



# num = int(input("nhap so bat ky: "))
# if num % 2 == 0:
#     print(f"so {num} la so chan ")
# else: print(f"so {num} la so le")



# a = int(input("nhap chieu cao ban a: "))
# b = int(input("nhap chieu cao ban b: "))
# c = int(input("nhap chieu cao ban c: "))

# if a > b and a > c:
#     print("ban a la nguoi cao nhat")
# elif b > a and b > c:
#     print("ban b la nguoi cao nhat")
# else: 
#     print("ban c la người cao nhat")



# def ucln(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# # Ví dụ sử dụng:
# num1 = int(input("Nhập số thứ nhất: "))
# num2 = int(input("Nhập số thứ hai: "))

# print(f"Ước chung lớn nhất của {num1} và {num2} là: {ucln(num1, num2)}")



# a = ["con cho ","con meo","con heo","con ga"]
# for i in a:
#     print(i)
# tong = 0

# n = [1,2,3,4,5]
# for i in n:
#     tong +=i
# print(tong)


# n = [1,2,4,2,1,4,5]
# n = list(set(n))
# print(n)

def is_symmetric(lst):
    # So sánh danh sách với phiên bản đảo ngược của nó
    return lst == lst[::-1]

# Ví dụ sử dụng:
lst1 = [1, 2, 3, 2, 1]
lst2 = [1, 2, 3, 4, 5]

print(f"Danh sách {lst1} có đối xứng không? {is_symmetric(lst1)}")
print(f"Danh sách {lst2} có đối xứng không? {is_symmetric(lst2)}")



