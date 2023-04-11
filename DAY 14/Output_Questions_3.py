def fun(x):
    if x>9:
        fun(x/9)
        print(x-1)
        fun(x/3)
    else:
        print(x-2)
fun(27)
