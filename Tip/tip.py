def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    d_fl = d.strip("$")
    return d_fl

def percent_to_float(p):
    p_fl = p.strip("%")
    return float(p_fl) / 100


main()
