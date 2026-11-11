# 🐘 Шпаргалка: Docker + PostgreSQL + FastAPI

> Команды для пересоздания БД, работы с контейнером, PostgreSQL и запуска приложения.

---

## 🔄 1. Миграция и пересоздание БД

### 1.1 Бэкап старой БД *(если нужен)*

```bash
docker exec -t -e PGPASSWORD=admin pg-container pg_dump -U postgres postgres > backup.sql
```

### 1.2 Фиксация зависимостей

```bash
pip freeze > requirements.txt
```

### 1.3 Пересоздание контейнера

```bash
docker rm -f pg-container

docker run -d --name pg-container \
  -e POSTGRES_PASSWORD=admin \
  -p 5432:5432 \
  -v pg_data:/var/lib/postgresql/data \
  postgres
```

### 1.4 Проверка готовности

```bash
docker ps
docker logs pg-container
```

### 1.5 Запуск приложения *(в отдельном терминале)*

```bash
uvicorn main:app --port 8080 --reload
```

---

## 🐳 2. Docker

| Задача | Команда |
|---|---|
| Оболочка внутри контейнера | `docker exec -it pg-container bash` |
| SQL-запрос одной строкой | `docker exec -it -e PGPASSWORD=admin pg-container psql -U postgres -c "SELECT * FROM users LIMIT 5;"` |
| Использование ресурсов | `docker stats pg-container` |
| Проброшенные порты | `docker port pg-container` |
| Инспекция (IP, volumes, env) | `docker inspect pg-container` |
| Остановить всё | `docker stop $(docker ps -q)` |
| Очистка неиспользуемого | `docker system prune -af` |

---

## 🐘 3. PostgreSQL

| Задача | Команда |
|---|---|
| Список баз | `docker exec -it -e PGPASSWORD=admin pg-container psql -U postgres -c "\l"` |
| Список таблиц | `docker exec -it -e PGPASSWORD=admin pg-container psql -U postgres -d mydb -c "\dt"` |
| Размер баз | `docker exec -it -e PGPASSWORD=admin pg-container psql -U postgres -c "\l+"` |
| Активные подключения | `docker exec -it -e PGPASSWORD=admin pg-container psql -U postgres -c "SELECT * FROM pg_stat_activity;"` |

---

## ⚡ 4. Python / FastAPI

### 4.1 Проверка сборки без ошибок

```bash
python -c "from main import app; print('OK')"
```

### 4.2 Запуск с логами в файл

```bash
uvicorn main:app --port 8080 --reload --log-level debug 2>&1 | tee app.log
```

### 4.3 Проверка, свободен ли порт 8080

```bash
lsof -i :8080
```

---

## ⚠️ Важные замечания

> [!WARNING]
> **`docker rm -f pg-container`** удаляет контейнер, но данные остаются в volume `pg_data`. Для полностью чистой БД выполните `docker volume rm pg_data`.

> [!CAUTION]
> **`docker system prune -af`** удаляет все неиспользуемые контейнеры, образы, сети и кэш. Используйте осторожно.

> [!NOTE]
> **`docker stop $(docker ps -q)`** останавливает *все* запущенные контейнеры, а не только `pg-container`.