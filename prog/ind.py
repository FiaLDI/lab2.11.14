
def search_area(type = 0):
    def triangle(a, h):
        return 1 / 2 * a * h

    def rectangle(a, b):
        return a * b
    
    if type == 0:
        return triangle
    else:
        return rectangle


def main():
    print(search_area(0)(1,2))
    print(search_area(1)(1,2))

if __name__ == "__main__":
    main()