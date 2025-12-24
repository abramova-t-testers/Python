from smartphone import Smartphone

catalog = [
    Smartphone('Apple', 'iPhone 16 Pro Max', '+79807265924'),
    Smartphone('Apple', 'iPhone 15', '+79614832911'),
    Smartphone('Apple', 'iPhone XS', '+79223156274'),
    Smartphone('Samsung', 'Galaxy A26', '+79812634855'),
    Smartphone('Samsung', 'Galaxy S25', '+79112562278')
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
