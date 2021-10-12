#1.实现一个函数，将1~100内所有的平方数放在一个列表中，
# 如：1,4,9,16,...
def square():
    lst = []
    for x in range(1,101,1):
        y = x**2
        if y <= 100:
            lst.append(y)
        else: continue
    return(lst)

print(square())


#2.实现一个函数，通过接受用户的输入字符串，去搜索该字符串是否在固定的
# 字典中 ，字典的数据需要自己定义 。如果在将该字典的值输出
def exist(**kwargs):
    s = input("请输入一个字符串:")
    for key,value in kwargs.items():
            if s in key:
                return value
    else:
        return '抱歉没有收到对应的数据'



print(exist(a=2,b=3,ab=4,abcdf=5,asdf='aa',bcv='bb'))

def search(**kwargs):
    s = input("请输入一个字符串:")
    if s in kwargs.keys():
        return kwargs.get(s)  # get() 获取某个键的值

    else:
        return '抱歉没有收到对应的数据'

print(search(a=2,b=3,ab=4,abcdf=5,asdf='aa',bcv='bb'))


