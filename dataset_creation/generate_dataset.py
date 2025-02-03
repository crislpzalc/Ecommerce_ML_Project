import pandas as pd
import numpy as np
from faker import Faker
import random

# Initialize Faker to generate random data
fake = Faker()

# Configurate size of dataset
num_samples = 5000


# Function to generate data
def generate_data(num_samples):
    data = []

    for i in range(num_samples):
        # Unique client ID
        customer_id = f"{i + 1:05d}"

        #name
        first_name = fake.first_name()
        last_name = fake.last_name()
        name = f"{first_name} {last_name}"

        # Email
        email_domain = fake.free_email_domain()
        email = f"{first_name.lower()}.{last_name[:2].lower()}@{email_domain}"

        # Age (normal distribution)
        age = int(np.clip(np.random.normal(35, 10), 18, 70))

        # Gender (Male, Female, Other)
        gender = random.choices(["Male", "Female", "Other"], weights=[0.48, 0.48, 0.04])[0]

        # Annual income (truncated normal distribution)
        income = int(np.clip(np.random.normal(50000, 15000), 10000, 200000))

        # Purchase frequency (monthly)
        purchase_freq = max(1, int(np.random.poisson(2)))  # At least one purchase

        # Amount spent based on purchase frequency
        amount_spent = round(np.random.uniform(10, 500) * purchase_freq, 2)

        # Most purchased product category
        product_category = random.choice(["Electronic", "Fashion", "Home", "Sports", "Books", "Toys"])

        # Time spent on web (correlated with purchases)
        time_spent = round(np.random.uniform(5, 60) + (purchase_freq * 2), 2)

        # Payment method
        payment_method = random.choice(["Credit Card", "Debit Card", "PayPal", "Wire"])

        # Discount used (inverse probability to income and expenditure)
        discount_used = 1 if random.uniform(0, 1) < (0.5 if amount_spent < 100 else 0.2) else 0

        # Fraud detection (atypical cases)
        is_fraud = 1 if random.uniform(0, 1) < 0.02 else 0  # 2% of fraud simulated

        # Add data to the list
        data.append([customer_id, name, email, age, gender, income, purchase_freq, amount_spent,
                     product_category, time_spent, payment_method, discount_used, is_fraud])

    # Convert to a DataFrame
    df = pd.DataFrame(data, columns=[
        "Client_ID", "Username", "Email", "Age", "Gender", "Annual_Income", "Purchase_Frequency",
        "Amount_Spent", "Product_Category", "Time_Spent", "Payment_Method",
        "Discount_Used", "Fraud"
    ])

    return df


# Generate dataset
df_ecommerce = generate_data(num_samples)

# Save in CSV
df_ecommerce.to_csv("ecommerce_data.csv", index=False)



