# פרופילים
from smolagents import Tool

fake_profiles = [
    {"id": "123", "name": "Alice", "age": 30},
    {"id": "456", "name": "Bob", "age": 25},
    {"id": "789", "name": "Charlie", "age": 20},
    {"id": "321", "name": "Diana", "age": 35},
    {"id": "654", "name": "Eve", "age": 28},
]

# עסקאות
fake_transactions = [
    {"transaction_id": "tx1", "customer_id": "123", "amount": 100, "date": "2025-01-01"},
    {"transaction_id": "tx2", "customer_id": "789", "amount": 50, "date": "2025-02-01"},
    {"transaction_id": "tx3", "customer_id": "456", "amount": 200, "date": "2025-03-01"},
    {"transaction_id": "tx4", "customer_id": "999", "amount": 80, "date": "2025-03-15"},  # מזהה שלא קיים בפרופילים
]

# אנשי קשר (טלפונים)
fake_contacts = [
    {"owner_phone": "0501234567", "contact_phone": "0507654321"},
    {"owner_phone": "0507654321", "contact_phone": "0501234567"},
    {"owner_phone": "0501111111", "contact_phone": "0502222222"},
    {"owner_phone": "0501234567", "contact_phone": "0503333333"},
    {"owner_phone": "0504444444", "contact_phone": "0505555555"},
]

# מיקומים
fake_locations = [
    {"phone": "0501234567", "city": "Tel Aviv", "timestamp": "2025-04-01"},
    {"phone": "0507654321", "city": "Haifa", "timestamp": "2025-04-02"},
    {"phone": "0501111111", "city": "Jerusalem", "timestamp": "2025-04-03"},
    {"phone": "0505555555", "city": "New York", "timestamp": "2025-04-04"},
    {"phone": "0509999999", "city": "Paris", "timestamp": "2025-04-05"},  # טלפון שלא מופיע באנשי קשר
]

# תעסוקה
fake_employment = [
    {"employee_email": "alice@example.com", "company": "BigCorp", "role": "Engineer"},
    {"employee_email": "bob@example.com", "company": "StartUpX", "role": "Designer"},
    {"employee_email": "charlie@example.com", "company": "InnovateLtd", "role": "Analyst"},
    {"employee_email": "diana@example.com", "company": "BigCorp", "role": "Manager"},
]

# קשרי משפחה
fake_family = [
    {"parent_id": "123", "child_id": "456"},  # אליס היא אמא של בוב
    {"parent_id": "456", "child_id": "789"},  # בוב הוא אבא של צ'ארלי
    {"parent_id": "321", "child_id": "654"},  # דיאנה היא אמא של איב
    {"parent_id": "123", "child_id": "654"},  # אליס גם אמא של איב
]

class Porfile(Tool):
    name = "model_download_counter"
    description = """
    This is a tool that returns the most downloaded model of a given task on the Hugging Face Hub.
    It returns the name of the checkpoint."""
    inputs = {
        "task": {
            "type": "string",
            "description": "the task category (such as text-classification, depth-estimation, etc)",
        }
    }
    output_type = "string"

    def forward(self, task: str):
        from huggingface_hub import list_models

        model = next(iter(list_models(filter=task, sort="downloads", direction=-1)))
        return model.id