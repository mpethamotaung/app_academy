#important keywords in loops: break and continue

#continue: moves to next iteration of loop

nums = [1, 2, 3 ,4, 5]

for num in nums:
    if num == 3:
        print('We found it')
        continue #skips to the next iteraion/output
    print(num) #prints out all items in list 'nums'
