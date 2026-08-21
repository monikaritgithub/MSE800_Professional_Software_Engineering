-- Enable foreign key constraints in SQLite to ensure relationships between tables are strictly enforced
PRAGMA foreign_keys = ON;

-- ==========================================================
-- 1. CUSTOMER TABLE
-- Stores profile details for every customer doing a currency exchange.
-- ==========================================================
CREATE TABLE IF NOT EXISTS customer (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique identifier for each customer (Auto-increments: 1, 2, 3...)
    first_name TEXT NOT NULL,                     -- Customer's first name (Cannot be empty)
    last_name TEXT NOT NULL,                      -- Customer's last name (Cannot be empty)
    phone_number TEXT,                            -- Customer's contact phone number
    email TEXT UNIQUE NOT NULL                    -- Customer's email address (Must be unique across all records)
);

-- ==========================================================
-- 2. CURRENCY TABLE
-- Stores details about supported global currencies (e.g., USD, EUR, NZD).
-- ==========================================================
CREATE TABLE IF NOT EXISTS currency (
    currency_id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique identifier for each currency record
    currency_code TEXT UNIQUE NOT NULL,           -- 3-character ISO currency code (e.g., 'USD', 'NZD')
    currency_name TEXT NOT NULL,                  -- Full name of the currency (e.g., 'US Dollar')
    symbol TEXT NOT NULL                          -- Currency symbol (e.g., '$', '€', 'NZ$')
);

-- ==========================================================
-- 3. EXCHANGE RATES TABLE
-- Stores live or historical exchange rate values for currency pairs.
-- ==========================================================
CREATE TABLE IF NOT EXISTS exchange_rates (
    rate_id INTEGER PRIMARY KEY AUTOINCREMENT,     -- Unique identifier for each exchange rate entry
    pair_id TEXT NOT NULL,                        -- Currency pair identifier (e.g., 'USD/NZD')
    rate_value REAL NOT NULL,                     -- The actual conversion multiplier/rate value (e.g., 1.65)
    effective_date TEXT NOT NULL                  -- Timestamp when this exchange rate became effective
);

-- ==========================================================
-- 4. EXCHANGE TRANSACTION TABLE
-- Records every currency conversion performed by a customer.
-- ==========================================================
CREATE TABLE IF NOT EXISTS exchange_transaction (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,      -- Unique receipt/transaction ID
    customer_id INTEGER NOT NULL,                          -- Foreign key linking to customer table
    from_currency_id INTEGER NOT NULL,                     -- Foreign key linking to source currency table
    to_currency_id INTEGER NOT NULL,                       -- Foreign key linking to target currency table
    amount_from REAL NOT NULL,                             -- Amount of money given by the customer
    amount_to REAL NOT NULL,                               -- Final calculated amount given back to customer
    applied_exchange_rate REAL NOT NULL,                   -- Exchange rate used at the moment of exchange
    service_fee REAL DEFAULT 0.00,                         -- Service fee charged for processing
    transaction_date TEXT DEFAULT CURRENT_TIMESTAMP,       -- Date and time when transaction happened
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
    FOREIGN KEY (from_currency_id) REFERENCES currency(currency_id),
    FOREIGN KEY (to_currency_id) REFERENCES currency(currency_id)
);

-- ==========================================================
-- SEED DATA
-- Populate initial records so the system has dummy data ready to test immediately.
-- ==========================================================
INSERT OR IGNORE INTO currency (currency_id, currency_code, currency_name, symbol) VALUES 
(1, 'USD', 'US Dollar', '$'),
(2, 'EUR', 'Euro', '€'),
(3, 'NZD', 'New Zealand Dollar', 'NZ$');

INSERT OR IGNORE INTO exchange_rates (rate_id, pair_id, rate_value, effective_date) VALUES 
(1, 'USD/NZD', 1.65, datetime('now')),
(2, 'EUR/USD', 1.08, datetime('now')),
(3, 'NZD/USD', 0.61, datetime('now'));

INSERT OR IGNORE INTO customer (customer_id, first_name, last_name, phone_number, email) VALUES 
(1, 'Jane', 'Doe', '0211234567', 'jane.doe@example.com');