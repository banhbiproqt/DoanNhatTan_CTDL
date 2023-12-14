def reverse_integer(n):# hàm đảo ngược số nguyên

    reversed_integer=0 #  biến reversed để lưu trữ số sau khi đã đảo ngược
    remainder =0 # biến để lưu trữ số dư

    while n>0: # vòng lặp nếu n còn lớn hơn 0
        remainder=n%10 #  số dư của biến lúc đầu chia cho 10
        reversed_integer =reversed_integer*10+remainder # biến đã đảo ngược bằng chính nó nhân 10 + với số dư
        n=n//10# chia số lúc đầu cho 10
    return reversed_integer # trả về giá trị đảo ngược

print(reverse_integer(1234567800)) # in ra biến đảo ngược