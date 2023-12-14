print("Hello word from Pycharm and Python !")

array = [10, 3, 7, 5,46]   # tạo một biến array chứa các phần tử
print(array[0]) # in ra phần tử đầu tiên
print(array[0:2]) # in ra các phần tử được cắt từ phần tử đầu tới kế phần tử thứ 2

max = array[0] # gán max là phần tử đầu tiên

for num in array: # duyệt qua array để tìm phần tử lớn nhất trong array
    if num>max:
        max=num # nếu phần tử duyệt qua lớn hơn max thì gán nó cho max

print(max)# in ra giá trị max trong array