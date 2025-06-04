# Health_idea

Веб-приложение на Flask с поддержкой webhook и использованием секретных ключей из .env.

## Запуск

1. Создайте файл `.env` в корне проекта и добавьте туда:
   ```
   SECRET_KEY=sk_test_1234567890abcdef
   API_KEY=api_test_abcdef123456
   WEBHOOK_SECRET=whsec_test_abcdef987654
   ```
2. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```
3. Запустите сервер:
   ```
   python webhook.py
   ```

## Webhook endpoint

POST `/webhook`

- В заголовке `X-Webhook-Secret` должен быть ключ из переменной `WEBHOOK_SECRET`.
- Тело запроса — JSON.

## Безопасность

Файл `.env` добавлен в `.gitignore` и не попадёт в репозиторий.
