def calculate_weather_severity():
    total_rain = 0
    total_wind = 0
    count = 0

    while True:
        data = input("Enter rain (inches) and wind speed (mph) separated by a space, or '-1' to finish: ")

        if data.strip() == "-1.0":
            break

        try:
            rain, wind = map(float, data.split())
            total_rain += rain
            total_wind += wind
            count += 1
        except ValueError:
            print("Invalid input, please enter valid numbers.")
            continue

    if count == 0:
        print("No data was entered.")
    else:
        average_rain = total_rain / count
        average_wind = total_wind / count
        weather_severity = (average_rain * 10) + average_wind

        print(f"\nThe average rain is {average_rain:.1f} inches")
        print(f"The average wind is {average_wind:.1f} mph")
        print(f"The weather severity for these {count} readings is: {weather_severity:.1f}")


calculate_weather_severity()
