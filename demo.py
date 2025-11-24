for i in range(1, 11):
    square = i * i
    cube = i * i * i
    if square % 2 == 0:
        print(f"{i}: Square={square} (even), Cube={cube}")
    else:
        print(f"{i}: Square={square} (odd), Cube={cube}")
print("Done!")
