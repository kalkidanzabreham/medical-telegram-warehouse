SELECT
    message_id,
    channel_name,
    message_date::date AS message_date,
    message_text,
    LENGTH(message_text) AS message_length,
    has_media AS has_image,
    views AS view_count,
    forwards AS forward_count
FROM raw.telegram_messages
WHERE message_text IS NOT NULL
