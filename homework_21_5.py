# Exam#2
students = [
    {"name": "An", "scores": {"Toán": 8.0, "Lý": 7.5, "Hóa": 9}},
    {"name": "Bình", "scores": {"Toán": 6, "Lý": 5.5, "Hóa": 7.0}},
    {"name": "Cường", "scores": {"Toán": 9, "Lý": 9.5, "Hóa": 10}}
]
# 1. In ra tên và điểm trung bình của từng sinh viên theo định dạng
'''An - Average: 8.17
Bình - Average: 6.17
Cường - Average: 9.5'''

# 2. Tìm sinh viên có điểm trung bình cao nhất
# 3. Tính điểm trung bình của từng môn
# 4. In xếp loại học lực cho từng sinh viên\
'''Theo thang điểm:
 Điểm trung bình	Xếp loại
 >= 9	          Xuất sắc
 >= 8	          Giỏi
 >= 6.5	        Khá
 >= 5	          Trung bình
 < 5	            Yếu

 Yêu cầu:
 - Áp dụng vòng for để rút gọn code'''

#Lấy ra thông tin từng học sinh
hs_0 = students[0]
hs_1 = students[1]
hs_2 = students[2]
#Lấy ra list điểm từng học sinh
score_hs_0 = hs_0["scores"]
score_hs_1 = hs_1["scores"]
score_hs_2 = hs_2["scores"]
#Lấy ra điểm toán từng học sinh
math_0 = score_hs_0["Toán"]
math_1 = score_hs_1["Toán"]
math_2 = score_hs_2["Toán"]
#Lấy ra điểm Lý từ học sinh
physic_0 = score_hs_0["Lý"]
physic_1 = score_hs_1["Lý"]
physic_2 = score_hs_2["Lý"]
#Lấy ra điểm Hoá từng học sinh
chem_0 = score_hs_0["Hóa"]
chem_1 = score_hs_1["Hóa"]
chem_2 = score_hs_2["Hóa"]
#List từng học sinh
list_score_0 = (math_0, physic_0,chem_0)
list_score_1 = (math_1, physic_1,chem_1)
list_score_2 = (math_2, physic_2,chem_2)
#Tính điểm trung bình từng học sinh
avg_hs_0 = round(sum(list_score_0) / len(list_score_0), 2)
avg_hs_1 = round(sum(list_score_1) / len(list_score_1), 2)
avg_hs_2 = round(sum(list_score_2) / len(list_score_2), 2)
print(hs_0["name"],"- Average:",avg_hs_0)
print(hs_1["name"],"- Average:",avg_hs_1)
print(hs_2["name"],"- Average:",avg_hs_2)

#Tính điểm trung bình từng môn học

print(aaa.value())

#Xếp loại học lực
if avg_hs_0 >= 9:
 print("Học lực của",hs_0["name"],"là: Xuất sắc")
elif avg_hs_0 >= 8:
 print("Học lực của",hs_0["name"],"là: Giỏi")
elif avg_hs_0 >=6.5:
 print("Học lực của",hs_0["name"],"là: Khá")
elif avg_hs_0 >=5:
 print("Học lực của",hs_0["name"],"là: Trung bình")
else:
 print("Học lực của",hs_0["name"],"là: Yếu")
  
print(aaa)