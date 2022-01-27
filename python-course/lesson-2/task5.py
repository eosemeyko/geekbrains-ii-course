from typing import List

from utils import get_input_num

ratings: List[int] = [2, 4, 6, 8]
print(ratings)
input_rating: int = get_input_num('новое число рейтинга')
add_rating: bool = False

for i, v in enumerate(ratings):
    if input_rating <= v:
        ratings.insert(i, input_rating)
        add_rating = True
        break

if not add_rating:
    ratings = ratings + [input_rating]

print(ratings)
