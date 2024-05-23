def fibonacci(limit):
    print(0, 1, end=" ")
    previous = 0
    next = 1
    result = 0

    for i in range(limit - 2):
        result = previous + next
        print(result, end=" ")
        previous = next
        next = result


limit = int(input("Enter the limit of number count: "))

fibonacci(limit)