import sqlite3
import pandas as pd
from openai import OpenAI
import random
from datetime import datetime, timedelta

# SQLite database file
DB_FILE = "demo_database.db"

# NVIDIA API configuration
NVIDIA_API_KEY = "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"
NVIDIA_BASE_URL = "https://integrate.api.nvidia.com/v1"


def create_sample_data():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    print("Creating sample data in SQLite database...")
    # Create the table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customer_purchases (
        customer_id INTEGER PRIMARY KEY,
        product_name TEXT,
        purchase_date TEXT,
        ai_description TEXT
    )
    """)

    # Sample product names
    products = [
        "Smartphone X", "Laptop Pro", "Wireless Earbuds", "Smart Watch",
        "4K TV", "Gaming Console", "Bluetooth Speaker", "Fitness Tracker",
        "Robot Vacuum", "Coffee Maker"
    ]

    # Generate sample data
    sample_data = []
    for i in range(1, 101):  # 100 sample records
        customer_id = i
        product_name = random.choice(products)
        purchase_date = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime('%Y-%m-%d')
        sample_data.append((customer_id, product_name, purchase_date))

    # Insert sample data
    cursor.executemany("""
    INSERT OR REPLACE INTO customer_purchases (customer_id, product_name, purchase_date)
    VALUES (?, ?, ?)
    """, sample_data)

    conn.commit()
    conn.close()
    print("Sample data created successfully. 100 records inserted.")


def generate_text(prompt):
    print(f"\nMaking NVIDIA NIM API call for prompt: '{prompt}'")
    client = OpenAI(
        base_url=NVIDIA_BASE_URL,
        api_key=NVIDIA_API_KEY
    )

    try:
        print("Sending request to NVIDIA NIM...")
        completion = client.chat.completions.create(
            model="meta/llama-3.1-8b-instruct",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            top_p=0.7,
            max_tokens=256,
            stream=False
        )
        print("Received response from NVIDIA NIM.")
        return completion.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    print("Starting the NVIDIA NIM integration demo...")

    # Create sample data
    create_sample_data()

    conn = sqlite3.connect(DB_FILE)

    try:
        print("\nFetching data from SQLite database...")
        # Fetch data from SQLite
        query = """
        SELECT customer_id, product_name, ai_description
        FROM customer_purchases
        WHERE purchase_date >= date('now', '-7 days')
        LIMIT 5
        """
        df = pd.read_sql_query(query, conn)

        print(f"\nRetrieved {len(df)} rows from SQLite database")

        print("\nInitial state of data (before AI-generated descriptions):")
        print(df.to_string(index=False))

        print("\nGenerating AI descriptions using NVIDIA NIM...")
        # Generate product descriptions using NVIDIA's AI model
        for index, row in df.iterrows():
            print(f"\nProcessing product: {row['product_name']}")
            ai_description = generate_text(
                f"Write a short, catchy description for this product in 20 words or less: {row['product_name']}")
            df.at[index, 'ai_description'] = ai_description

        print("\nAI-generated descriptions completed")

        print("\nFinal state of data (after AI-generated descriptions):")
        print(df.to_string(index=False))

        print("\nUpdating SQLite database with AI-generated descriptions...")
        # Update SQLite with results
        cursor = conn.cursor()
        for _, row in df.iterrows():
            cursor.execute("""
            UPDATE customer_purchases
            SET ai_description = ?
            WHERE customer_id = ?
            """, (row['ai_description'], row['customer_id']))
        conn.commit()

        print(f"Updated {len(df)} rows in SQLite database")

    finally:
        conn.close()
        print("Demo completed. Database connection closed.")


if __name__ == "__main__":
    main()