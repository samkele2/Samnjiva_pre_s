
def main():
    word = input("camelCase: ")
    snake_str = ""
    for c in word:
        if c.isupper():
            snake_str += "_" + c.lower()
        else:
            snake_str += c
    print("snake_case:", snake_str)



main()




