-- EmberTable PostgreSQL schema
-- This mirrors the SQLAlchemy models in backend/app_cafe.py

-- Customers table
CREATE TABLE IF NOT EXISTS public.customers (
  customer_id SERIAL PRIMARY KEY,
  customer_name VARCHAR(100) NOT NULL,
  email VARCHAR(120) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  newsletter_signup BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW()
);

-- Reservations table
CREATE TABLE IF NOT EXISTS public.reservations (
  reservation_id SERIAL PRIMARY KEY,
  customer_id INTEGER NOT NULL REFERENCES public.customers(customer_id) ON DELETE CASCADE,
  time_slot TIMESTAMP WITHOUT TIME ZONE NOT NULL,
  table_number INTEGER NOT NULL CHECK (table_number BETWEEN 1 AND 30),
  number_of_guests INTEGER NOT NULL CHECK (number_of_guests BETWEEN 1 AND 12),
  status VARCHAR(20) NOT NULL DEFAULT 'confirmed' CHECK (status IN ('confirmed','cancelled','completed')),
  special_requests TEXT,
  created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW()
);

-- Useful indexes
CREATE INDEX IF NOT EXISTS idx_reservations_time_slot ON public.reservations(time_slot);
CREATE INDEX IF NOT EXISTS idx_reservations_table_time ON public.reservations(table_number, time_slot);
-- Prevent exact duplicate bookings for the same table at the same timestamp
CREATE UNIQUE INDEX IF NOT EXISTS ux_reservations_table_time ON public.reservations(table_number, time_slot);

-- Trigger to auto-update updated_at
CREATE OR REPLACE FUNCTION set_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DO $$ BEGIN
  IF NOT EXISTS (
    SELECT 1 FROM pg_trigger WHERE tgname = 'customers_set_updated_at'
  ) THEN
    CREATE TRIGGER customers_set_updated_at
    BEFORE UPDATE ON public.customers
    FOR EACH ROW EXECUTE FUNCTION set_updated_at();
  END IF;

  IF NOT EXISTS (
    SELECT 1 FROM pg_trigger WHERE tgname = 'reservations_set_updated_at'
  ) THEN
    CREATE TRIGGER reservations_set_updated_at
    BEFORE UPDATE ON public.reservations
    FOR EACH ROW EXECUTE FUNCTION set_updated_at();
  END IF;
END $$;

