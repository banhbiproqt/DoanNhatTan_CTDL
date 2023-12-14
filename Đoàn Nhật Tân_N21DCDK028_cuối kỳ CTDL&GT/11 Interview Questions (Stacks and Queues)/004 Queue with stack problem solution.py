class Queue:

    def __init__(self): #Phương thức __init__ khởi tạo hai ngăn xếp trống: enqueue_stack và dequeue_stack.
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, data):# Phương thức enqueue chèn dữ liệu vào ngăn xếp enqueue_stack.
        self.enqueue_stack.append(data) #thêm một phần tử vào cuối hàng đợi.

    def dequeue(self):# Phương thức dequeue loại bỏ và trả giá trị đầu tiên ở hàng đợi.
        if len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0:#Kiểm tra xem cả hai ngăn xếp đều trống hay không
            raise Exception("Stacks are empty...")#  nếu trống thì thông báo đang trống

        if len(self.dequeue_stack)==0:#Nếu dequeue_stack trống

            while len(self.enqueue_stack) != 0: # lặp qua enqueue_stack và chuyển tất cả các phần tử của enqueue_stack  sang dequeue_stack theo thứ tự ngược lại (thứ tự FIFO).
                self.dequeue_stack.append(self.enqueue_stack.pop())

        return self.dequeue_stack.pop()# trả về phần tử từ đầu ngăn xếp dequeue_stack.

queue = Queue()

queue.enqueue(10) #thêm 10 vào enqueue_stack
queue.enqueue(20)#thêm 20 vào enqueue_stack
queue.enqueue(30)#thêm 30 vào enqueue_stack

print(queue.dequeue()) # loại bỏ giá trị đầu tiên và in ra nó

queue.enqueue(40)#thêm 40 vào enqueue_stack

print(queue.dequeue())# loại bỏ giá trị đầu tiên và in ra nó
print(queue.dequeue())# loại bỏ giá trị đầu tiên và in ra nó
print(queue.dequeue())# loại bỏ giá trị đầu tiên và in ra nó