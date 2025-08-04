def square_filter(start,end):
    squares = []
    even_squares = []
    odd_squares = []

    for num in range(start,end + 1):
        square = num * num
        squares.append(square)
        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)

    print("All squares:",squares)
    print("Even squares:",even_squares)
    print("Odd squares:",odd_squares)

square_filter(1,5)