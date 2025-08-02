def main():
    word = input("Input:  ")
    twttr = ""
    for c in word:
        if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
            continue
        else:
            twttr += c
    print(twttr)



main()
