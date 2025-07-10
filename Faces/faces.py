mrt = input()
def convert(mrt):
    return mrt.replace(":)", "\U0001F642").replace(":(", ("\U0001F641"))


print(convert(mrt))
