time = "18:30"

def main():
    co_time = convert(time)
    if 7 <= co_time <= 8:
        print("Breakfast Time")
    elif 12 <= co_time <= 13:
        print("Lunch Time")
    elif 18 <= co_time <= 19:
        print("Dinner Time")

def convert(time):
    hours, minutes = time.split(":")
    p_min = int(minutes) / 60
    flt_hours = float(hours)
    print(flt_hours + p_min, "hours")

if __name__ == "__main__":
    main()
