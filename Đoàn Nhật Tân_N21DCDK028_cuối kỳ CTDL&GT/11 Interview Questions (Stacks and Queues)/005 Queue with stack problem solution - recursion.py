class Queue:
    def __init__(self):#Phương thức __init__ khởi tạo một ngăn xếp trống có tên self.stack.
         self.stack = []

    def enqueue(self, data):#Phương thức enqueue thêm phần tử data được cung cấp vào ngăn xếp. nghĩa là  thêm một phần tử vào cuối hàng đợi.
        self.stack.append(data)

    def dequeue(self): #Phương thức dequeue loại bỏ và trả về phần tử ở đầu hàng đợi.
        if len(self.stack)==1:#Nếu chỉ có một phần tử trong ngăn xếp, nó sẽ được trả về trực tiếp là phần tử đầu của hàng đợi.
            return self.stack.pop()

        item = self.stack.pop()# Nếu có nhiều phần tử trong ngăn xếp, phần tử đầu tiên được tạm thời lưu trữ trong biến item.
        dequeue_item = self.dequeue() # thực hiện đệ quy để loại bỏ tất cả các phần tử khỏi ngăn xếp cho đến khi chỉ còn phần tử đầu tiên

        self.stack.append(item)#thêm phần tử item vào ngăn xếp self.stack.  nghĩa  thêm một phần tử vào cuối hàng đợi.
        return dequeue_item# phần tử đầu (dequeue_item) được trả về.


queue = Queue()

queue.enqueue(10) #thêm 10 vào enqueue_stack
queue.enqueue(20)#thêm 20 vào enqueue_stack
queue.enqueue(30)#thêm 30 vào enqueue_stack

print(queue.dequeue()) # loại bỏ giá trị đầu tiên và in ra nó

queue.enqueue(40)#thêm 40 vào enqueue_stack

print(queue.dequeue())# loại bỏ giá trị đầu tiên và in ra nó
print(queue.dequeue())# loại bỏ giá trị đầu tiên và in ra nó
print(queue.dequeue())# loại bỏ giá trị đầu tiên và in ra nó