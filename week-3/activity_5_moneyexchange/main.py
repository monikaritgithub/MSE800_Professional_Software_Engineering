import sqlite3
import sys
from database import DatabaseHandler
from models import ExchangeTransaction

def display_menu():
    print("\n==================================================")
    print("      MONEY EXCHANGE SYSTEM - MAIN MENU           ")
    print("==================================================")
    print("1. Perform a Currency Exchange Transaction")
    print("2. View All Transaction Logs")
    print("3. View Supported Currencies")
    print("4. View All Registered Customers")
    print("5. Register New Customer")
    print("6. Exit System")
    print("==================================================")


def main():
    db = DatabaseHandler()
    
    try:
        db.initialize_database()
        print("\n[SUCCESS] Connected to database and initialized tables.")
    except Exception as e:
        print(f"\n[FATAL ERROR] Could not initialize database: {e}")
        sys.exit(1)

    while True:
        display_menu()
        choice = input("Enter option (1-6): ").strip()

        # OPTION 1: Execute Exchange
        if choice == '1':
            print("\n--- 1. NEW CURRENCY EXCHANGE ---")
            try:
                cust_id = int(input("Enter Customer ID (e.g., 1): "))
                from_curr_id = int(input("Enter Source Currency ID (1=USD, 2=EUR, 3=NZD): "))
                to_curr_id = int(input("Enter Target Currency ID (1=USD, 2=EUR, 3=NZD): "))
                amount = float(input("Enter Amount to Exchange: "))
                rate = float(input("Enter Exchange Rate (e.g., 1.65): "))
                fee = float(input("Enter Service Fee (e.g., 5.00): "))

                new_tx = ExchangeTransaction(
                    customer_id=cust_id,
                    from_currency_id=from_curr_id,
                    to_currency_id=to_curr_id,
                    amount_from=amount,
                    applied_exchange_rate=rate,
                    service_fee=fee
                )

                saved_id = db.save_transaction(new_tx)

                print("\n--------------------------------------------------")
                print(f"[SUCCESS] Transaction logged successfully!")
                print(f"Receipt ID       : #{saved_id}")
                print(f"Amount Exchanged : ${new_tx.amount_from:.2f}")
                print(f"Total Received   : ${new_tx.amount_to:.2f}")
                print("--------------------------------------------------")

            except ValueError:
                print("\n[ERROR] Invalid numerical input! Please enter numbers only.")
            except sqlite3.IntegrityError:
                print("\n[ERROR] Transaction failed: Provided Customer ID or Currency ID does not exist.")
            except Exception as e:
                print(f"\n[ERROR] Transaction failed: {e}")

        # OPTION 2: View Transactions
        elif choice == '2':
            print("\n--- 2. TRANSACTION HISTORY LOGS ---")
            records = db.get_all_transactions()
            if not records:
                print("No transactions found in database.")
            else:
                for row in records:
                    tx_id, cust_name, from_c, to_c, amt_from, amt_to, rate, fee, date = row
                    print(f"Receipt #{tx_id} | Customer: {cust_name} | ${amt_from:.2f} {from_c} -> ${amt_to:.2f} {to_c} | Rate: {rate} | Fee: ${fee:.2f} | Date: {date}")

        # OPTION 3: View Currencies
        elif choice == '3':
            print("\n--- 3. SUPPORTED CURRENCIES ---")
            currencies = db.get_all_currencies()
            if not currencies:
                print("No currencies found.")
            else:
                for c in currencies:
                    print(f"ID: {c[0]} | Code: {c[1]} | Name: {c[2]} | Symbol: {c[3]}")

        # OPTION 4: View Customers
        elif choice == '4':
            print("\n--- 4. REGISTERED CUSTOMERS ---")
            customers = db.get_all_customers()
            if not customers:
                print("No customers found.")
            else:
                for cust in customers:
                    print(f"ID: {cust[0]} | Name: {cust[1]} {cust[2]} | Phone: {cust[3]} | Email: {cust[4]}")

        # OPTION 5: Register Customer
        elif choice == '5':
            print("\n--- 5. REGISTER NEW CUSTOMER ---")
            first = input("Enter First Name: ").strip()
            last = input("Enter Last Name: ").strip()
            phone = input("Enter Phone Number: ").strip()
            email = input("Enter Email Address: ").strip()

            if not first or not last or not email:
                print("\n[ERROR] Registration failed: First Name, Last Name, and Email cannot be empty!")
                continue

            try:
                new_id = db.add_customer(first, last, phone, email)
                print(f"\n[SUCCESS] Customer '{first} {last}' registered with Customer ID #{new_id}")
            except sqlite3.IntegrityError:
                print(f"\n[ERROR] Registration failed: Email '{email}' is already registered!")
            except Exception as e:
                print(f"\n[ERROR] Registration failed: {e}")

        # OPTION 6: Exit
        elif choice == '6':
            print("\nExiting Money Exchange System. Goodbye!")
            break

        else:
            print("\n[ERROR] Invalid option! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()