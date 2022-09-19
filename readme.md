Запуск:

`docker-compose up --build -d`

На `localhost (127.0.0.1:80)` будет поднят сервис.


Основные эндпоинты API
- GET /item/{id} - получение html страницы `Item`
- GET /buy/{id} - получение session_id

`Dockerfile, docker-compose.yml, requirenments.txt, entrypoint.sh` - прописаны

`env variables` - указывать в `docker-compose.yml`

На `localhost/admin` модели `Item, Order, Discount, TaxRate`

- GET /order/{id} - получение html страницы `Order`
- GET /buy/order/{id} - получение `session_id`

Также можно привязать к `Order` модели `Discount, TaxRate` 

Тестирование двух дополнительных валют 
- GET /buy-eur/{id}
- GET /buy-jpy/{id}

Не получилось реализовать: 
 - "Stripe Payment Intent" не получилось реализовать
- "2 Stripe Keypair"
 - "Запуск приложения на удаленном сервере, доступном для тестирования"

Дополнительно: 
- Создание `TaxRate, Price, Product, Coupon` происходит при каждом запросе за 
`session_id`
- `Item.currency` - подразумевает перевод цены 
между валютами (интеграцию с внешним сервисом), поэтому просто выставлены две 
валюты `eur, jpy, usd` со стандартной `usd` и без перевода цены.
- Для получения доступа к админке и тестированию запустить 
`docker-compose exec backend python manage.py setup`
  (`admin`/`adminpass` для входа в админ панель)