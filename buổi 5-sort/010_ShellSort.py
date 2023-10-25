def shellsort(A): # hàm sắp xếp shellsort
    n = len(A) # n là độ dài A
    gap = n // 2 # Khởi tạo khoảng cách ban đầu giữa các phần tử là n/2
    while gap > 0: # Bắt đầu vòng lặp chính, kiểm tra nếu khoảng cách còn lớn hơn 0.
        i = gap # Bắt đầu xét từ phần tử ở vị trí `gap.
        while i < n: # Bắt đầu vòng lặp bên trong để xem xét các phần tử trong danh sách.
            temp = A[i] # Lưu giá trị của phần tử hiện tại vào biến tạm thời.
            j = i - gap # Xác định phần tử trước khoảng `gap`.
            while j >= 0 and A[j] > temp: # Bắt đầu vòng lặp để so sánh và hoán đổi các phần tử.
                A[j + gap] = A[j] # Dịch chuyển phần tử sang phải để tạo khoảng trống cho `temp`.
                j = j - gap # Xem xét phần tử trước đó.
            A[j + gap] = temp # Gán giá trị temp vào vị trí đúng trong danh sách.
            i = i + 1 # duyệt phần tử tiếp theo.
        gap = gap // 2 # Giảm khoảng cách `gap` đi một nửa.
A = [3, 5, 8, 9, 6, 2] # Khởi tạo danh sách A.
print('Original Array:', A) # In danh sách ban đầu.
shellsort(A) # Gọi hàm
print('Sorted Array:', A) # In danh sách sau khi sắp xếp.
