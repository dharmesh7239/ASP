# calculate_salary.py
import numpy as np
from mongo_storage import collection

salaries = [float(job['salary'].replace('$', '').replace(',', '')) for job in collection.find({'salary': {'$exists': True}})]
average_salary = np.mean(salaries)
print(f"Average Salary for Python Developers: ${average_salary:.2f}")
