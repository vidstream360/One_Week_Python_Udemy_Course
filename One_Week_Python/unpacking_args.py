def average(*args):
    total = 0
    for arg in args:
        total += arg
    print(total/len(args)) # or return total/len(args)

average(1,2,3,4,5)

average(10,1)

#if you pass a function like this a list, it is unhappy. it wants individual arguments 

nums = [7,4,9,2,11,2,3,4]

#average(nums) #<- this breaks if uncommented

#unpack the list into individual arguemnts. use star * to unpack

average(*nums)