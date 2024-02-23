def wind_chill(temperature_F, wind_speed):
    """
    Calculate wind chill based on temperature in Fahrenheit and wind speed in miles per hour.
    """
    # Check if wind speed is less than 3 mph or temperature is greater than 50F,
    # in which case wind chill is undefined
    if wind_speed < 3 or temperature_F > 50:
        return temperature_F  # Return the temperature itself in these conditions
    else:
        # Use the wind chill formula to calculate wind chill
        return 35.74 + 0.6215 * temperature_F - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature_F * (wind_speed ** 0.16)

def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    """
    # Use the conversion formula to convert Celsius to Fahrenheit
    return (celsius * 9/5) + 32

def main():
    # Get user input for temperature and unit (Fahrenheit or Celsius)
    temperature = float(input("What is the temperature? "))
    unit = input("Fahrenheit or Celsius (F/C)? ").upper()

    # Convert temperature to Fahrenheit if unit is Celsius
    if unit == 'C':
        temperature = celsius_to_fahrenheit(temperature)

    # Display the temperature before calculating wind chill
    print(f"At temperature {temperature:.1f}F:")

    # Loop through wind speeds from 5 to 60 mph, incrementing by 5
    for wind_speed in range(5, 61, 5):
        # Calculate wind chill for each wind speed
        windchill = wind_chill(temperature, wind_speed)
        # Display wind chill for the current temperature and wind speed
        print(f"At temperature {temperature:.1f}F, and wind speed {wind_speed} mph, the windchill is: {windchill:.2f}F")

if __name__ == "__main__":
    main()
