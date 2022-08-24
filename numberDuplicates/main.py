def reader(file):
    with open(file) as file:
        read = file.readlines()
        new_list = [int(num) for num in read]
        return new_list

file1 = reader("./nums1.py")
file2 = reader("./nums2.py")

result = [num for num in file1 if num in file2]

print(result)