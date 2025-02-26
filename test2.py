arr1 = input("please input data in array1 (use , ): ").split(',')
arr2 = input("please input data in array2 (use , ): ").split(',')

def result_arrays(arr1, arr2):
    unique = []
    for item in arr1 + arr2:
        if item not in unique:
            unique.append(item)
    difference = []
    for item in arr1:
        if item not in arr2:
            difference.append(item)
    for item in arr2:
        if item not in arr1:
            difference.append(item)

    return unique, difference

result1, result2 = result_arrays(arr1, arr2)
print("Array รวมข้อมูลไม่มีข้อมูลซ้ำ:", result1)
print("Array รวมข้อมูลที่ตัดข้อมูลซ้ำ:", result2)
