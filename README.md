Запустить: 
```bash
docker compose up -d --build
```

Остановить:
```bash
docker compose stop
```

Уничтожить:
```bash
docker-compose down -v
```

Применение миграций:
```bash
 docker compose exec web python manage.py migrate --noinput
```

Добавление фикстур
```bash
docker compose exec web python manage.py loaddata category ingredient measurement quantity recipe
```

Создание суперпользователя
```bash
docker compose exec web python manage.py createsuperuser
```

Проект доступен по адресу _http://127.0.0.1:8000_

В проекте риализовано: фильтры по категориям рецептов, а также по ингредиентам через отдельные кнопки слева вверху, а также поле для поиска рецепта по названию.
Также, после нажатия на рецепт реализована отдельная страница с подробным описанием рецепта.