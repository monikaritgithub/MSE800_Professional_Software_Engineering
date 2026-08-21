import os
import sqlite3
from models import ExchangeTransaction

class DatabaseHandler:
    """Handles SQLite database interactions and CRUD operations."""
    def __init__(self, db_file: str = "exchange_system.db"):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_file = os.path.join(base_dir, db_file)

    def get_connection(self):
        """Creates connection and enforces Foreign Key constraints."""
        conn = sqlite3.connect(self.db_file)
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn

    def initialize_database(self):
        """Creates tables and populates default records if empty."""
        schema = """
        PRAGMA foreign_keys = ON;

        CREATE TABLE IF NOT EXISTS customer (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone_number TEXT,
            email TEXT UNIQUE NOT NULL
        );

        CREATE TABLE IF NOT EXISTS currency (
            currency_id INTEGER PRIMARY KEY AUTOINCREMENT,
            currency_code TEXT UNIQUE NOT NULL,
            currency_name TEXT NOT NULL,
            symbol TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS exchange_transaction (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            from_currency_id INTEGER NOT NULL,
            to_currency_id INTEGER NOT NULL,
            amount_from REAL NOT NULL,
            amount_to REAL NOT NULL,
            applied_exchange_rate REAL NOT NULL,
            service_fee REAL DEFAULT 0.00,
            transaction_date TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
            FOREIGN KEY (from_currency_id) REFERENCES currency(currency_id),
            FOREIGN KEY (to_currency_id) REFERENCES currency(currency_id)
        );
        """
        with self.get_connection() as conn:
            conn.executescript(schema)
            cursor = conn.cursor()

            # Seed default currencies if empty
            cursor.execute("SELECT COUNT(*) FROM currency")
            if cursor.fetchone()[0] == 0:
                cursor.executemany(
                    "INSERT INTO currency (currency_id, currency_code, currency_name, symbol) VALUES (?, ?, ?, ?)",
                    [
                        (1, 'USD', 'US Dollar', '$'),
                        (2, 'EUR', 'Euro', '€'),
                        (3, 'NZD', 'New Zealand Dollar', 'NZ$')
                    ]
                )

            # Seed default customer if empty
            cursor.execute("SELECT COUNT(*) FROM customer")
            if cursor.fetchone()[0] == 0:
                cursor.execute(
                    "INSERT INTO customer (customer_id, first_name, last_name, phone_number, email) VALUES (?, ?, ?, ?, ?)",
                    (1, 'Jane', 'Doe', '0211234567', 'jane.doe@example.com')
                )

            conn.commit()

    def save_transaction(self, tx: ExchangeTransaction) -> int:
        query = """
        INSERT INTO exchange_transaction 
        (customer_id, from_currency_id, to_currency_id, amount_from, amount_to, applied_exchange_rate, service_fee)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        params = (
            tx.customer_id,
            tx.from_currency_id,
            tx.to_currency_id,
            tx.amount_from,
            tx.amount_to,
            tx.applied_exchange_rate,
            tx.service_fee
        )
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.lastrowid

    def get_all_transactions(self):
        query = """
        SELECT 
            t.transaction_id,
            COALESCE(c.first_name || ' ' || c.last_name, 'Unknown Customer') AS customer_name,
            COALESCE(fc.currency_code, 'N/A') AS from_code,
            COALESCE(tc.currency_code, 'N/A') AS to_code,
            t.amount_from,
            t.amount_to,
            t.applied_exchange_rate,
            t.service_fee,
            t.transaction_date
        FROM exchange_transaction t
        LEFT JOIN customer c ON t.customer_id = c.customer_id
        LEFT JOIN currency fc ON t.from_currency_id = fc.currency_id
        LEFT JOIN currency tc ON t.to_currency_id = tc.currency_id
        ORDER BY t.transaction_id DESC
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            return cursor.fetchall()

    def get_all_currencies(self):
        query = "SELECT currency_id, currency_code, currency_name, symbol FROM currency"
        with self.get_connection() as conn:
            cursor = conn.cursor()
            return cursor.fetchall()

    def get_all_customers(self):
        query = "SELECT customer_id, first_name, last_name, phone_number, email FROM customer"
        with self.get_connection() as conn:
            cursor = conn.cursor()
            return cursor.fetchall()

    def add_customer(self, first_name: str, last_name: str, phone: str, email: str) -> int:
        query = "INSERT INTO customer (first_name, last_name, phone_number, email) VALUES (?, ?, ?, ?)"
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (first_name, last_name, phone, email))
            conn.commit()
            return cursor.lastrowid