import random
import string

def generate_password(length, use_uppercase, use_digits, use_special_chars):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_yes_no_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['так', 'ні']:
            return response == 'так'
        else:
            print("Будь ласка, введіть 'Так' або 'Ні'.")

def get_integer_input(prompt):
    while True:
        response = input(prompt).strip()
        if response.isdigit():
            return int(response)
        else:
            print("Будь ласка, введіть ціле число.")

def main():
    length = get_integer_input("Введіть довжину паролю: ")
    use_uppercase = get_yes_no_input("Використовувати великі літери? (Так/Ні): ")
    use_digits = get_yes_no_input("Використовувати цифри? (Так/Ні): ")
    use_special_chars = get_yes_no_input("Використовувати спеціальні знаки? (Так/Ні): ")

    password = generate_password(length, use_uppercase, use_digits, use_special_chars)

    print("Згенерований пароль:", password)

    save_to_file = get_yes_no_input("Зберегти пароль у файл? (Так/Ні): ")
    if save_to_file:
        filename = input("Введіть ім'я файлу для збереження: ")
        with open(filename, 'w') as file:
            file.write(password)
        print("Пароль збережено у файлі", filename)

    output_password = get_yes_no_input("Вивести пароль? (Так/Ні): ")
    if output_password:
        print("Пароль:", password)

if __name__ == "__main__":
    main()
