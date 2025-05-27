'''1. Giải phương trình bậc 1
Đề: Viết chương trình giải phương trình bậc nhất dạng: ax + b = 0.
Người dùng nhập a, b. In nghiệm hoặc thông báo vô nghiệm.
a = int(input("mời nhập giá trị a:"))
b = int(input("mời nhập giá trị b:"))
if a == 0:
 if b == 0:
  print("phương trình có vô số nghiệm")
 else:
  print("phương trình vô nghiệm")
else:
 x = -b / a
 print("nghiệm của phương trình là",x) '''

'''2. In dãy số chia hết cho 3 từ 1 đến 100
Đề: Sử dụng for và if để in ra tất cả số chia hết cho 3 trong khoảng từ 1 đến 100.

for x in range(1,100):
 if x % 3 == 0:
  print(x)

#List Comprehension để tạo một danh sách các số chia hết 
numbers = [number for number in range(1,100) if number % 3 == 0]
print(numbers)'''

'''3. Tính tổng các số lẻ từ 1 đến n
Đề: Người dùng nhập n. In ra tổng tất cả số lẻ từ 1 đến n.
tong_le = 0
n = int(input("mời nhập số nguyên:"))
while not n >=1:
  n = int(input("bạn phải nhập số nguyên dương:"))
for i in range(1, n+1):
  if i % 2 != 0:
   tong_le += i
print(f"tổng của các số lẻ từ 1 tới {n} là {tong_le}")'''

'''4.Kiểm tra số nguyên tố
Đề: Người dùng nhập n. Kiểm tra và in xem n có phải là số nguyên tố không.

n = int(input("mời nhập giá trị n: "))
for i in range(2, n):
    if n % i == 0:
        print(" {0} không phải là số nguyên tố".format(n))
        break
else:
        print("{0} là số nguyên tố".format(n))'''

'''5. Đếm số dương, âm, bằng 0 trong list
Đề: Cho list nums = [3, -2, 0, 7, -5, 0, 1]. Đếm và in ra số lượng phần tử:
Dương
Âm
Bằng 0
sl_0 = 0
sl_am = 0
sl_duong = 0
list_nums = [3, -2, 0, 7, -5, 0, 1]
for i in list_nums:
    if i > 0:
        sl_duong += 1
    elif i < 0:
        sl_am += 1
    else: 
        sl_0 += 1
print(f"Có {sl_duong} số dương")   
print(f"Có {sl_am} số âm")    
print(f"Có {sl_0} số 0")''' 
    
'''Phân loại học lực
Đề: Người dùng nhập điểm (0–10). Dựa vào điểm, in ra xếp loại:
= 9: Xuất sắc
= 8: Giỏi
= 6.5: Khá
= 5: Trung bình
< 5: Yếu
score = int(input("Mời nhập số điểm:"))
if score >= 9:
 hoc_luc = "Xuất sắc"
elif score >= 8:
 hoc_luc = "Giỏi"
elif score >= 6.5:
 hoc_luc = "Khá"
elif score >= 5:
 hoc_luc = "Trung bình"
else:
 hoc_luc = "Kém"
print("Học lực là:", hoc_luc)'''

# In tam giác số
#Khoi lenh co the phat sinh loi
'''try:
   #Nhap gia tri tu ban phim
   #Ep kieu du lieu sang so nguyen
   n = int(input())
  
   #Su dung cau truc re nhanh xu ly truong hop n nam ngoai (1:9)
   if n<1 or n>9:
       print("Vui long nhap gia tri tu 1 den 9!")
   else:   
       #Su dung vong 2 vong for long nhau de thuc hien yeu cau bai toan
       for hang in range(1, n+1):
           for cot in range(1, hang+1):
               #Tham so end=' ' de cac so trong hang cach nhau 1 khoang trong
               print(cot, end=' ')
           #Xong 1 hang thi xuong dong
           print()
#Khoi lenh duoc thuc thi khi loi xay ra
except:
   print("Dinh dang dau vao khong hop le!")'''

'''n = int(input("Vui lòng nhập số nguyên:"))
for hang in range(1, n+1):
    for cot in range(1, hang+1):
        print(cot, end=' ')
    print()'''

numbers = [10, 8, 3, 20, 15, 20]
def find_second_largest(numbers):
    # Kiểm tra danh sách có ít nhất hai phần tử
    if len(numbers) < 2:
        return None
    
    # Tìm số lớn nhất trong danh sách
    max_number = float('-inf')
    for number in numbers:
        if number > max_number:
            max_number = number
    
    # Xóa số lớn nhất khỏi danh sách
    numbers.remove(max_number)
    
    # Tìm số lớn nhất thứ hai trong danh sách đã xóa
    second_max_number = float('-inf')
    for number in numbers:
        if number > second_max_number:
            second_max_number = number
    
    # Trả về số lớn nhất thứ hai
    return second_max_number