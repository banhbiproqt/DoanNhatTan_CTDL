# kiểm tra có phần tử trùng trong mảng không
def find_duplicates(nums): # hàm kiểm tra có phần tử trùng không
    for num in nums :# duyệt qua các phần tử trong mảng
        if nums[abs(num)]>=0: # nếu phần tử tại abs(num)>0
            nums[abs(num)]= -  nums[abs(num)]# thì đảo nó lại thành số âm , để đánh dấu phần tử này đã được xét tới
        else:
            print("repetition found :%s" %str(abs(num))) # nếu điều kiện sai , tức là phần tử này đã được xét đến, nên sẽ in ra phần tử đó là phần tử trùng lặp

n=[1,2,3,4,5,6,6,7,7]
find_duplicates(n)# in ra phần tử trùng lặp