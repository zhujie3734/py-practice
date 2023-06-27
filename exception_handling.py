""""
try:
    year = int(input('input year:'))
except ValueError:
    print('请输入数字')


try:
    print(1/0)
except ZeroDivisionError as e:
    print('0不能做除数 %s' %e)



try:
    print(1/'a')
except Exception as e:
    print('%s' %e)

"""
#自定义错误
try:
    raise NameError('helloError')
except NameError:
    print('my custom error')