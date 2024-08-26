#Loops - For, While
#Python does not have a do while loop

"""
for var_name in range(start,stop,step)

range will print(start, stop -1)
step default val =1
start default val =0
Same outputs:
range(0,10,1)
range(0,10)
range(10)

var_name=0
while condition:
  code
  var_name increment

pass - pass statement is a null operation; nothing happens when it is executed.It is used as a placeholder for future code where
Python syntax requires a statement, but you have nothing to write.

continue - continue statement is used within a loop to skip the current iteration and move on to the next one. It effectively
jumps back to the loop's start, bypassing the remaining code block for that particular iteration

"""
print(tuple(range(1,10)))

#InterviewTip:
for i in range(10,-3,-2):
    print(i,end=" ")

for j in range(10):
    if j%2 == 0:
        continue
        pass
    else:
        print(j)



