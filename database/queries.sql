-- Handy queries for demo and troubleshooting

-- 1) Upcoming reservations in the next 7 days
SELECT r.reservation_id, r.time_slot, r.table_number, r.number_of_guests,
       c.customer_name, c.email
FROM public.reservations r
JOIN public.customers c ON c.customer_id = r.customer_id
WHERE r.time_slot BETWEEN NOW() AND NOW() + INTERVAL '7 days'
ORDER BY r.time_slot;

-- 2) Find reservations for a specific email
-- Replace the email in the WHERE clause
SELECT r.*
FROM public.reservations r
JOIN public.customers c ON c.customer_id = r.customer_id
WHERE c.email = 'test@example.com'
ORDER BY r.time_slot DESC;

-- 3) Availability check for a given time (approximate)
-- Replace timestamp below
WITH occupied AS (
  SELECT table_number
  FROM public.reservations
  WHERE time_slot BETWEEN TIMESTAMP '2025-09-07 17:00:00' AND TIMESTAMP '2025-09-07 19:00:00'
    AND status = 'confirmed'
)
SELECT generate_series AS table_number
FROM generate_series(1,30)
WHERE generate_series NOT IN (SELECT table_number FROM occupied)
ORDER BY table_number;

