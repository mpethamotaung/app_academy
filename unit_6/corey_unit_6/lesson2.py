#important keywords in loops: break and continue
#break: exits the loop
#continue: moves to next iteration of loop

nums = [1, 2, 3 ,4, 5]

for num in nums:
    if num == 3:
        print('We found it')
        break # breaks out when condition is met
    print(num) #prints out all items in list 'nums'

