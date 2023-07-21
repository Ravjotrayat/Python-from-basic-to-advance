'''
Algorithm of LCS(Least common sequence)
def lcs(i,j):
    if a[i]=='\o' or b[i]=='\o':
        return 0
    elif a[i]==b[j]:
        return 1+lcs(i+1,j+1)
    else:
        return max(lcs(i+1,j),lcs(i,j+1))
Example 1:
a b c d e f g h i j
c d g i
output => 4

Example 2:
a b c d e f g h i j
e c d g i
output =>

1.) Recursive Approach
2.) Memoization
3.) Dynamic Approach(Tabulation method)

1.) Recursive Method => Since we are calling function again and again
time and space complexity is not so efficient.
Time complexity=>

2.) Memoization =>Here compared to the first approach the efficiency is
    getting better whereas in the memoization table whenever result
    for a particular is already formed we don't do that task again.
    Time complexity=> 

3.) Dynamic approacha : ( Algorithm )
Time complexity=>O(log n^2)
if a[i]==b[i]
    lcs[i,j]=1+lcs[i-1,j-1]
else
    lcs[i,j]=max(lcs(i-1,j),lcs(i,j-1))

'''

