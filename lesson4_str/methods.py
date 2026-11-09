city = "Minsk"

len(city)

print(city.capitalize())
print(city.lower())
print(city.upper())

phone_number = " +3753361476320"
phone_number = phone_number.strip()

print(phone_number.startswith("+375"))
print(phone_number.endswith("30"))

phone_number = phone_number.replace("+375", "+911-")
print(phone_number)

print(phone_number.count("3"))
