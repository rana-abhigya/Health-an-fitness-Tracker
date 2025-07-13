import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
from config import db_config

# Connect to MySQL
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Fetch health data
cursor.execute("SELECT date, steps, calories, sleep_hours FROM records ORDER BY date")
rows = cursor.fetchall()
conn.close()

if not rows:
    print("⚠️ No data found.")
    exit()

# Process data
dates = [row[0].strftime('%Y-%m-%d') for row in rows]
steps = [row[1] for row in rows]
calories = [row[2] for row in rows]
sleep = [row[3] for row in rows]

# Stats
avg_steps = np.mean(steps)
avg_calories = np.mean(calories)
avg_sleep = np.mean(sleep)

# Create plots
plt.figure(figsize=(12, 8))
plt.suptitle("Health & Fitness Tracker Report", fontsize=18, fontweight='bold')

# Subplot 1: Steps
plt.subplot(3, 1, 1)
plt.plot(dates, steps, marker='o', color='blue', label='Steps')
plt.axhline(avg_steps, color='gray', linestyle='--', label=f'Avg: {avg_steps:.0f}')
plt.title('Steps Over Time')
plt.ylabel('Steps')
plt.xticks(rotation=45)
plt.legend()

# Subplot 2: Calories
plt.subplot(3, 1, 2)
plt.plot(dates, calories, marker='o', color='green', label='Calories')
plt.axhline(avg_calories, color='gray', linestyle='--', label=f'Avg: {avg_calories:.0f}')
plt.title('Calories Over Time')
plt.ylabel('Calories')
plt.xticks(rotation=45)
plt.legend()

# Subplot 3: Sleep Hours
plt.subplot(3, 1, 3)
plt.plot(dates, sleep, marker='o', color='purple', label='Sleep Hours')
plt.axhline(avg_sleep, color='gray', linestyle='--', label=f'Avg: {avg_sleep:.1f} hrs')
plt.title('Sleep Hours Over Time')
plt.ylabel('Hours')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
