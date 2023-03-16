a="I like Python"
b="Java is very popular language"

arr={i for i in a}
arr.remove(' ')

brr={i for i in b}
brr.remove(' ')
st=""
for i in brr:
    if i in arr:
        st=st+i
print(st)

