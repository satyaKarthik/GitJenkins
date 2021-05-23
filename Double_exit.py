def double(array):
    n=len(array)
    array.sort()
    print(array)
    for i in range(n-1,-1,-1):
        for j in range(0,n):
            if array[i]==2*array[j]:
                print("True")
                break


array=[-2,0,10,-19,4,6,-8]

double(array)

#     for i in range(n):
#         ele=array[i]
#         j=n
#         while(j>0):
#             if (ele==2*array[j-1]):
#                 j=j-1
#                 print(True)
#                 break
#             else:
#                 j=j-1
#
#
# array=[10,2,5,3]
# double(array)