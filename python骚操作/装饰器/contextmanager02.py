from contextlib import contextmanager

class DataBase():
    def query(self):
        print('写入操作')
    @contextmanager
    def open(self):
        try:
            yield self.commit()
        except Exception as e:
            self.rollback()
            raise e

    def commit(self):
        print("commit")
    def rollback(self):
        print("rollback")

db = DataBase()
with db.open():
    db.query()

'''
执行流程
①with语句调用open函数=>
②执行try异常判断=>
③执行with语句中的写入操作=>
④执行数据库的提交操作=>
⑤如果出现异常执行数据库回滚操作
'''