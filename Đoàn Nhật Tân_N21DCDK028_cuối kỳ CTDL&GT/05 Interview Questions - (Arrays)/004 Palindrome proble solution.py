def palindrome(s): # hàm kiểm tra palindrome
    n=len(s) # gán n là chiều dài của của chuỗi s
    st=""# gán chuỗi st là rỗng, dùng để lưu trữ chuỗi đảo ngược của s
    for i in range(n): # duyệt qua chuỗi s
        st=st+s[n-i-1]   # st để lưu trữ chuỗi đảo ngược của s
    return st==s # trả về true nếu là chuỗi đảo ngược = chuỗi ban đầu và false nếu không bằng


a_input=input("nhap mot chuoi : ") # nhập chuỗi
if palindrome(a_input):# kiểm tra và in ra kết quả true thì in ra là palindrome,  false thì in ra không phải là palindrome
    print("là palindrome")
else:
    print("không phải là palindrome ")
