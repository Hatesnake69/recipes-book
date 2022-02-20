Запустить: 
```bash
docker compose up -d --build
docker compose exec web python manage.py migrate --noinput
```

Остановить:
```bash
docker compose stop
```

Уничтожить:
```bash
docker-compose down -v
```
