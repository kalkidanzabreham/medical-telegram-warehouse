SELECT DISTINCT
    message_date AS full_date,
    EXTRACT(DOW FROM message_date) AS day_of_week,
    EXTRACT(WEEK FROM message_date) AS week_of_year,
    EXTRACT(MONTH FROM message_date) AS month,
    EXTRACT(YEAR FROM message_date) AS year
FROM {{ ref('stg_telegram_messages') }}
