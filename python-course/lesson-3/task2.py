from utils import get_input_no_empty


user_keys = {
    'first_name': 'имя', 'last_name': 'фамилию',
    'birth_year': 'год рождения', 'city': 'город проживания',
    'email': 'email', 'phone': 'телефон',
}


def get_user(**user) -> str:
    return (
        f"\nИмя: {user['first_name']}, Фамилия: {user['last_name']}, Год рождения: {user['birth_year']}, "
        f"Город проживания: {user['city']}, Email: {user['email']}, Телефон: {user['phone']}"
    )


user_obj = {}
for key, label in user_keys.items():
    value = get_input_no_empty(label)
    user_obj[key] = value

print(get_user(**user_obj))
