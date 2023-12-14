# hàm anagram (đảo chữ )
def anagrams(str1, str2): # hàm kiểm tra có phải 2 chuỗi  trên là anagram không
    # Sắp xếp các ký tự trong chuỗi
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # Kiểm tra xem chuỗi đã sắp xếp có giống nhau không
    return sorted_str1 == sorted_str2

# Nhập hai chuỗi từ người dùng
str1 = input("Nhập chuỗi thứ nhất: ")
str2 = input("Nhập chuỗi thứ hai: ")

# Kiểm tra xem chúng có phải là anagram không
if anagrams(str1, str2):
    print(f'"{str1}" và "{str2}" là anagram.')
else:
    print(f'"{str1}" và "{str2}" không phải là anagram.')