# dict
employee = {
    "name" : "HuongBTL" ,
    "age" : 26,
    "position" : "QA"
}
## Lấy tất cả giá trị
print(employee.values())

## Lấy tất cả key
print(employee.keys())

## Lấy giá trị cụ thể (nếu không có sẽ trả về null)
print(employee.get("name"))