class Testwith():
    def __enter__(self):
        print('enter')
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print('exit')
        else:
            print('has error %s' %exc_tb)
        

with Testwith():
    print('test is running')
    raise NameError('testNameError')
