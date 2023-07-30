

data2="0.983749       0.179548       0.000639952    -109.266        -0.179369      0.982916       -0.0412659     27.014  -0.00803822    0.0404805      0.999148       -26.7991        0      0      0     1"



data2=data2.split()
f_d=list()
for i in data2:
    f_d.append(float(i))
    

# Create a 2D array of size 4x4 initialized with 0s
array_2d = [[0 for _ in range(4)] for _ in range(4)]

# Iterate over the input list and fill the 2D array
for i in range(len(f_d)):
    row = i // 4  # Calculate the row index
    col = i % 4   # Calculate the column index
    array_2d[row][col] = f_d[i]


   

      
  
    
    
    

        