def asc_desc(list,order):
    if(order=="asc"):
        list.sort()
        print(list)
    elif(order=="desc"):
        list.sort(reverse = True )
        print(list)
    elif(order=="none"):
        print(list)
    else:
        print("please enter valid order")


asc_desc([1,7,3,8,4,2],"asc")