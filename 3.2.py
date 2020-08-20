def user_info(**kwargs):
    """Выводит всю введённую информацию одной строчкой"""
    info_dict = {**kwargs}
    for i in info_dict.keys():
        print(f"{i}: {info_dict.get(i)};", end=" ")
    print("\n")

user_info(name="Ivan", last_name="Petrovitch", year_of_birth="1810", sity="Moscow", email="IvanPetrovitch@email.email", phone_number="88005553535")
