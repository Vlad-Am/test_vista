# MyWishlist

## Описание
MyWishlist - это пример проекта на Django, с реализованной crud моделью wishlist

## Установка и запуск

### 1. Клонирование репозитория
Склонируйте репозиторий на ваш локальный компьютер:

> git clone https://github.com/yourusername/myproject.git
> cd wishlist

### 2. Создание виртуального окружения
Создайте и активируйте виртуальное окружение для изоляции зависимостей:
> python -m venv venv
> source venv/bin/activate  # Для Windows: venv\Scripts\activate

### 3. Установка зависимостей
Установите все необходимые зависимости из файла requirements.txt:
> pip install -r wishlist/requirements.txt

#### 3.1 Установка переменных виртуального окружения
> Переименуйте файл .env.sample в .env и определите переменные

### 4. Применение миграций
Создайте и примените миграции для инициализации базы данных:

> python manage.py makemigrations
> python manage.py migrate

### 5. Создание суперпользователя
Создайте суперпользователя для доступа к административному интерфейсу,
доступного по адресу http://127.0.0.1:8000/admin/:

> python manage.py createsuperuser

### 6. Запуск сервера разработки
Запустите сервер разработки Django:

> python manage.py runserver
> 
### 7. Документация
> Документация доступна по адресу http://127.0.0.1:8000/swager/ или  http://127.0.0.1:8000/redoc/