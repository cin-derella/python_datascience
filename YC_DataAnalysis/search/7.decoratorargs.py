def show(arg):

    def _show(func): # build in function , invoked by calling showdata()
        def __show():
            print('up',arg)
            func()
            print('down',arg)
        return __show
    return _show

@show('gogogo ')  # pass gogogo to show(arg)
def showdata(): # pass to _show()
    print('show data')

showdata()