def fun(k):
    if k>155:
        return
    print(k)
    fun(k+2)
    print(k)
k=150
fun(k)
'''
output:
150
152
154
154
152
150

'''
