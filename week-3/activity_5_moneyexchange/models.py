class Customer:
    """Represents a customer in the money exchange system."""
    def __init__(self, customer_id: int, first_name: str, last_name: str, phone_number: str, email: str):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Currency:
    """Represents a supported currency."""
    def __init__(self, currency_id: int, currency_code: str, currency_name: str, symbol: str):
        self.currency_id = currency_id
        self.currency_code = currency_code
        self.currency_name = currency_name
        self.symbol = symbol


class ExchangeTransaction:
    """Encapsulates exchange calculation and business logic."""
    def __init__(self, customer_id: int, from_currency_id: int, to_currency_id: int, 
                 amount_from: float, applied_exchange_rate: float, service_fee: float = 0.0, transaction_id: int = None):
        self.transaction_id = transaction_id
        self.customer_id = customer_id
        self.from_currency_id = from_currency_id
        self.to_currency_id = to_currency_id
        self.amount_from = amount_from
        self.applied_exchange_rate = applied_exchange_rate
        self.service_fee = service_fee
        self.amount_to = self.calculate_exchange()

    def calculate_exchange(self) -> float:
        """Calculates converted amount minus service fee."""
        converted = self.amount_from * self.applied_exchange_rate
        final_val = converted - self.service_fee
        return round(max(0.0, final_val), 2)