import datetime as dt

# ---------------------------
# Main function & entry point
# ---------------------------

def run():
    print("-" * 40)
    my_time = dt.datetime.now()
    print("Local time: ", my_time)

    utc_time = dt.datetime.utcnow()
    print("UTC time: ", utc_time)

    # Date manipulation (no time)
    print("-" * 40)
    today = dt.date.today()
    print(today)
    print(f"Year: {today.year}")
    print(f"Month: {today.month}")
    print(f"Day: {today.day}")

    # Date formatting
    print("-" * 40)

    my_date = dt.datetime.now()
    mx_time = my_date.strftime("%d/%m/%Y")
    us_time = my_date.strftime("%m/%d/%Y")


if __name__ == '__main__':
    run()