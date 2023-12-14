import copy
class StacksArray:
    # Phương thức khởi tạo, tạo một đối tượng ngăn xếp với một mảng trống
    def __init__(self):
        self._data = []

    # Phương thức đặc biệt để trả về độ dài của ngăn xếp (sử dụng len(self._data))
    def __len__(self):
        return len(self._data)

    # Kiểm tra xem ngăn xếp có trống không (kiểm tra độ dài mảng)
    def isempty(self):
        return len(self._data) == 0

    # Thêm một phần tử e vào đỉnh ngăn xếp (sử dụng append để thêm vào cuối mảng)
    def push(self, e):
        self._data.append(e)

    # Lấy và trả về phần tử ở đỉnh ngăn xếp. Nếu ngăn xếp trống, in thông báo và trả về None
    def pop(self):
        if self.isempty():
            print('Stack is Empty')
            return
        return self._data.pop()

    # Trả về giá trị của phần tử ở đỉnh ngăn xếp mà không loại bỏ nó.
    # Nếu ngăn xếp trống, in thông báo và trả về None
    def top(self):
        if self.isempty():
            print('Stack is Empty')
            return
        return self._data[-1]  # trả về phần tử ở đỉnh ngăn xếp




# Tạo một đối tượng S của lớp StacksArray
S = StacksArray()

# Thêm các phần tử 5 và 3 vào ngăn xếp, in ra mảng và độ dài ngăn xếp
# Thêm phần tử 5 vào đỉnh ngăn xếp
S.push(5)

# Thêm phần tử 3 vào đỉnh ngăn xếp
S.push(3)

# In ra mảng hiện tại của ngăn xếp
print(S._data)

# In ra độ dài của ngăn xếp
print('Length:', len(S))

# Lấy phần tử từ đỉnh ngăn xếp, in ra kết quả, kiểm tra xem ngăn xếp có trống không, và lấy phần tử tiếp theo
# Lấy và in ra giá trị của phần tử ở đỉnh ngăn xếp. Nếu ngăn xếp trống, in ra thông báo "Stack is Empty" và trả về None.
print(S.pop())



# Thêm các phần tử 7, 9, 4 vào ngăn xếp, in ra mảng, lấy giá trị ở đỉnh ngăn xếp, và in ra mảng cuối cùng
# Thêm phần tử 7 vào đỉnh ngăn xếp
S.push(7)

# Thêm phần tử 9 vào đỉnh ngăn xếp
S.push(9)

# Thêm phần tử 4 vào đỉnh ngăn xếp
S.push(4)

# In ra mảng hiện tại của ngăn xếp
print(S._data)
print(S.top())
# In ra giá trị của phần tử ở đỉnh ngăn xếp mà không loại bỏ nó




