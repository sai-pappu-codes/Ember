-- Seed data for Ember (safe to run multiple times)
INSERT INTO public.customers (customer_name, email, phone_number, newsletter_signup)
VALUES
  ('Test Customer', 'test@example.com', '555-1234', TRUE)
ON CONFLICT (email) DO NOTHING;

-- Use existing or newly created customer id
WITH c AS (
  SELECT customer_id FROM public.customers WHERE email = 'test@example.com'
)
INSERT INTO public.reservations (customer_id, time_slot, table_number, number_of_guests, status, special_requests)
SELECT c.customer_id, NOW() + INTERVAL '1 day' + TIME '18:00', 5, 2, 'confirmed', 'Anniversary dinner'
FROM c
ON CONFLICT DO NOTHING;

