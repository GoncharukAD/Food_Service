# Tecтовые данные без БД
positions = [
    {"id": 1, "title": "Вареники", "price": 200},
    {"id": 2, "title": "Пельмени", "price": 200},
    {"id": 3, "title": "Хинкали", "price": 300},
    {"id": 4, "title": "Салат", "price": 100},
]

orders = [
    {
        "id": 1,
        "positions_list": [
            {"id": 3, "title": "Хинкали", "price": 300, "count": 2, "amount": 600},
            {"id": 2, "title": "Пельмени", "price": 200, "count": 4, "amount": 800},
        ],
        "amount": 1400,
        "delivery": False,
    },
    {
        "id": 2,
        "positions_list": [
            {"id": 3, "title": "Хинкали", "price": 300, "count": 1, "amount": 300},
            {"id": 2, "title": "Салат", "price": 100, "count": 4, "amount": 400},
        ],
        "amount": 700,
        "delivery": True
    },
    {
        "id": 3,
        "positions_list": [
            {"id": 3, "title": "Хинкали", "price": 300, "count": 1, "amount": 300},
            {"id": 2, "title": "Пельмени", "price": 200, "count": 1, "amount": 200},
            {"id": 2, "title": "Вареники", "price": 200, "count": 2, "amount": 400},
            {"id": 2, "title": "Салат", "price": 200, "count": 4, "amount": 800}
        ],
        "amount": 1700,
        "delivery": True
    },
    {
        "id": 4,
        "positions_list": [
            {"id": 3, "title": "Салат", "price": 100, "count": 1, "amount": 100},
            {"id": 2, "title": "Пельмени", "price": 200, "count": 2, "amount": 400},
        ],
        "amount": 500,
        "delivery": False,
    }
]