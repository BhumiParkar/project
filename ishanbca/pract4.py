def display(list1):
    threshold = int(input("Enter the threshold value: "))

    print("Elements less than the threshold are:")
    for x in list1:
        if x < threshold:
            print(x)
n = int(input("Enter the number of elements: "))

list1 = []
for i in range(n):
    element = int(input("Enter element: "))
    list1.append(element)
display(list1)