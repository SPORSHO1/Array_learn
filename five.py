from numpy import*

arr1 = array ([
              [1,2,3,6,3,9],
              [4,5,6,7,5,3]
            ])

arr2 = arr1.flatten()
arr3 = arr2.reshape(2,2,3)

print(arr3)