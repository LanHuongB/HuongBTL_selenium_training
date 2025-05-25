'''1. Giải phương trình bậc 1
Đề: Viết chương trình giải phương trình bậc nhất dạng: ax + b = 0.
Người dùng nhập a, b. In nghiệm hoặc thông báo vô nghiệm.'''
a = 1
b = 2
if a == 0:
 if b == 0:
  print("phương trình có vô số nghiệm")
 else:
  print("phương trình vô nghiệm")
else:
 x = -b / a
 print("nghiệm của phương trình là",x) 

'''2. In dãy số chia hết cho 3 từ 1 đến 100
Đề: Sử dụng for và if để in ra tất cả số chia hết cho 3 trong khoảng từ 1 đến 100.'''

for x in range(1,100):
 if x % 3 == 0:
  print(x)

#List Comprehension để tạo một danh sách các số chia hết 
numbers = [number for number in range(1,100) if number % 3 == 0]
print(numbers)

'''3. Tính tổng các số lẻ từ 1 đến n
Đề: Người dùng nhập n. In ra tổng tất cả số lẻ từ 1 đến n.'''
tong_le = 0
n = int(input("mời nhập số nguyên:"))
while not n >=1:
  n = int(input("bạn phải nhập số nguyên dương:"))
for i in range(1, n+1):
  if i % 2 != 0:
   tong_le += i
print(f"tổng của các số lẻ từ 1 tới {n} là {tong_le}")

 