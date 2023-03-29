# Enter your code here. Read input from STDIN. Print output to 

input_ = input().strip()
#print(input_)
even =""
odd = ""
for i in range(int(input_)):
    input_string = input()
    for j in range(len(input_string)):
        if j%2 ==0:
            even += input_string[j]
        else:
            odd += input_string[j]
    #print(input_string)
    print(even+" "+odd)
    even=""
    odd = ""
