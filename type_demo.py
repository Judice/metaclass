# coding=utf-8
# 使用type函数创建Hello类
def fn(self, name='World'):     #不可缺少self
    print ('Hello %s' % name)

Hello = type('Hello',(object,),dict(hello=fn))
h = Hello()
print h.hello()
print type(Hello)
print type(h)