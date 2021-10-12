

#要求 ： 通过面向对象实现一个简易版的学生管理系统，要求功能中有增、删、改、查功能 ，
# 具体数据可以定义在一个字典中 ，若增加，将数据插入字典 ，若删除 ，将数据从字典中删除，依次类推

class Student_system():
    def __init__(self,name,sex,age,id):
        self.name = name
        self.sex = sex
        self.age = age
        self.id = id
    def add_info(self):

        dct = {'name':self.name,'sex':self.sex,'age':self.age,'id':self.id}
        return dct





