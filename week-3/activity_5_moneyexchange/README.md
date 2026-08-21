# Money Exchange System with Database

## Project Overview
The Money Exchange System allows an exchange business to manage customer profiles, supported currencies, real-time exchange rates, and financial exchange transactions.

## ER Diagram
![Entity Relationship Diagram](images/er_diagram.png)

## Table Breakdown & Justification
This project contains **4 core tables**:

1. **`customer`**: Stores customer demographic and contact data.
   * *Justification*: Essential for tracking transaction history per user and meeting KYC (Know Your Customer) financial requirements.
2. **`currency`**: Stores supported currency metadata (code, name, symbol).
   * *Justification*: Prevents data duplication across transactions and centralizes supported currency types.
3. **`exchange_rates`**: Holds currency pair rate values and effective timestamps.
   * *Justification*: Keeps a historical log of dynamic market exchange rates so currency valuations can update over time without affecting past transactions.
4. **`exchange_transaction`**: Records every financial transaction between two currencies.
   * *Justification*: Links customers and currencies together to preserve audit trails, precise amounts exchanged, applied exchange rates, and transaction dates.

## OOP Architecture
The project applies Object-Oriented Design principles:
* **Classes**: `Customer`, `Currency`, and `ExchangeTransaction`.
* **Encapsulation & Business Logic**: The `ExchangeTransaction` class manages exchange logic directly through its `calculate_exchange()` method before committing records to the database.

## How to Run
1. Execute `schema.sql` on your database server (e.g., MySQL / SQLite).
2. Run `main.py` (or index script) to launch the program.