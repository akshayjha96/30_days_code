# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

phone_records = {}

for item in range(n):
    name_num = input().split()
    phone_records[name_num[0]] = name_num[1]

for i in range(n):
    try:
        name = input()    
        if name in phone_records.keys():
            print(f"{name}={phone_records[name]}")
        else:
            print("Not found")
    except:
        quit() 
