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

#1. In ra điểm trung bình
'''for x in students:
 avg = round(sum(x["scores"].values())/len(x["scores"].values()), 2)
 print(x["name"],"- Average:",avg)
'''
# 4. In xếp loại học lực cho từng sinh viên
#1. In ra điểm trung bình
'''for x in students:
 avg = round(sum(x["scores"].values())/len(x["scores"].values()), 2)
 if avg >=9:
  xep_loai = "Xuất sắc"
 elif avg >=8:
  xep_loai = "Giỏi"
 elif avg >=6.5:
  xep_loai = "Khá"
 elif avg >5:
  xep_loai = "Trung bình"
 else:
  xep_loai = "Yếu"
 print("Học lực của",x.get("name"),"la:",xep_loai)'''


for x in students:
 avg = round(sum(x["scores"].values())/len(x["scores"].values()), 2)
 if avg