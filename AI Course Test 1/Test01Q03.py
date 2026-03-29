names = ["hello_python", "my_variable_name", "python", "a_b_c_d"]

def snake_to_camel(text: str) -> str:
    string = ""
    text = text.split("_")
    for word in text:
        string += word.capitalize()
    new_name = string[0].lower() + string[1:]
    return new_name

for name in names:
    print(snake_to_camel(name))