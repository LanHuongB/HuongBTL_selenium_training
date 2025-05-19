
#int
a = 10
b = 5
## chia (trả về float))
'''print(a/b)
##nhân
print(a*b)
##Trừ
print(a-b)
## cộng
print(a+b)
## chia lấy phần nguyên
print(5//3)
## chia lấy phần dư (%)
print(10%3)
## Luỹ thừa
print(2**3)
#string
str1 = "Hello"
str2 = "Minasan"
## Nối chuỗi
print(str1+" "+str2)
## Lặp chuỗi
print(str1*4)
## Cắt chuỗi
print(str1[0:3])
## Viết hoa toàn bộ
print("Hello".upper())
## Viết thường toàn bộ
print("HEllo".lower())
## Viết hoa chữ cái đầu
print("hello minasan".capitalize())
## Viết hoa từng chữ cái đầu
print("hello minasan".title())
## Xoá khoảng trắng đầu cuối
print(" hello  minasan ".strip())
## Thay thế chuỗi con
print("hello minasan".replace("minasan", "everyone"))
## Kiểm tra chuỗi con
print("Huong" in "Bui Thi Lan Huong")
## Tìm kiếm index()
print("lan huong".index("a"))
print("lan huong".index("h"))
print("lan huong".index("m"))
## Tìm kiếm find()
print("lan huong".find("a"))
print("lan huong".find("y"))
my_list = ["a","b","c"]
print(my_list[1])
'''
students = [
     {"name": "An", "scores": [8.0, 7.5, 9]}, 
     {"name": "Bình", "scores": [6, 5.5, 7.0]}, 
     {"name": "Cường", "scores": [9, 9.5, 10]}
       ]
''' in ra tên và điểm trung bình của từng sinh viên theo định dạng
An - Average: 8.17'''

#Lấy ra thông tin từng học sinh
hs_0 = (students[0])
hs_1 = (students[1])
hs_2 = (students[2])
#Lấy tên từng học sinh
name_hs_0 = hs_0["name"]
name_hs_1 = hs_1["name"]
name_hs_2 = hs_2["name"]
#Tính điểm trung bình từng học sinh (Làm tròn tới số thập phân thứ 2)
'''avg_hs_0 =sum(hs_0["scores"]) / len(hs_0["scores"]) => tính điểm trung bình
#avg_hs_0_fl = round(avg_hs_0, 2) => Làm tròn tới số thập phân thứ 2'''
avg_hs_0 = round(sum(hs_0["scores"]) / len(hs_0["scores"]), 2)
avg_hs_1 = round(sum(hs_0["scores"]) / len(hs_1["scores"]), 2)
avg_hs_2 = round(sum(hs_2["scores"]) / len(hs_2["scores"]), 2)
#in ra kết quả
print(name_hs_0,"- Average:", avg_hs_0)
print(name_hs_1,"- Average:", avg_hs_1)
print(name_hs_2,"- Average:", avg_hs_2)
