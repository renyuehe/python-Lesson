
class Student():
    def read(self):
        pass

class Student_Hook():
  def __init__(self):
    self.read_book = None
  def reg_book(self, book):
    self.read_book = book

  def read(self):
    if self.read_book  is not None:
        self.read_book()
    else:
        pass

def book_A():
  print("read book A")

def book_B():
  print("read book B")

# 钩子函数就是回调函数,卧槽真尼玛会取名字
# 这个到底是 钩子 还是 回调 有待考证
if __name__ == "__main__":
  student = Student_Hook()
  student.reg_book(book_B)
  student.read()