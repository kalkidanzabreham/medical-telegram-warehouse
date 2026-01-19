SELECT
    m.message_id,
    c.channel_key,
    d.full_date,
    m.message_text,
    m.message_length,
    m.view_count,
    m.forward_count,
    m.has_image
FROM {{ ref('stg_telegram_messages') }} m
JOIN {{ ref('dim_channels') }} c
  ON m.channel_name = c.channel_name
JOIN {{ ref('dim_dates') }} d
  ON m.message_date = d.full_date
