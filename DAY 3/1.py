# List comprehensive
# Find the square of the numbers if the sum is odd otherwise cube,if sum is even.
#Output should be in nested list as input.
#Output => [[1, 8, 9, 64], [25, 216, 49, 512], [81, 1000, 121, 1728], [169, 2744, 225, 4096]]

ls=[]
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print([[j**3 if j%2==0 else j**2 for j in i] for i in mat ])






