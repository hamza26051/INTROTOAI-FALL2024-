def show_info(**details):
    info = "Information:\n"
    for key, value in details.items():
        info += f"- {key}: {value}\n"
    return info

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

info = show_info(name=name, age=age, city=city)
print(info)