def reverse(nums): # hàm reverse đảo ngược mảng nums
    start_index =0 # start index  ở phần tử đầu
    end_index=len(nums)-1 # end index là phần tử cuối

    while end_index>start_index: # vòng lặp chừng nào end index còn lớn hơn start index
        nums[start_index],  nums[end_index]=nums[end_index],  nums[start_index] # hoán đổi vị trí phần tử đầu và phần tử cuối
        start_index=start_index+1 # di chuyển start và end lại gần nhau về phía giữa array
        end_index=end_index-1

if __name__ == '__main__':# kiểm tra chương trình độc lập không( không phải module import vào file khác)
    n=[1,2,3,4,5,6,7] # tạo một mảng
    reverse(n) # đảo ngược mảng
    print(n)# in ra mảng đã đảo ngược
