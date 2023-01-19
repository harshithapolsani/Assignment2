# nested interactive loop
#Allowing the user to select the method
method_name=["1","2"]
print("Enter the number corresponding to the method:")
user_value=int(input())
if user_value==1:
    print("Nested Interactive loop:")
    N = "Y"
    # initializing the  value to yes
    while N == 'Y':
        print("Enter the values in the list:")
        list1 = list(map(int,input().split()))
        list2 = []
        for i in list1:
            list2.append(round(i/2.2049,2))
        print(list2)
        print("if there is data Y/N?:")
        N = input()
if user_value == 2:
    print("List comprehension:")
    inches =[150,155,145,148]
    cms = []
    for x in inches:
        cms.append(round(x / 2.2049,2))
    print(cms)

