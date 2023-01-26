# Import necessary modules
from datetime import datetime

# Define a function to retrieve patients with exemptions or loans
def get_patients_with_exemptions_or_loans():
    # Connect to the database
    conn = sqlite3.connect("icare.db")
    c = conn.cursor()

    # Retrieve patients with exemptions
    c.execute("SELECT patient_id, exemption_type, start_date, end_date FROM exemptions")
    exemptions = c.fetchall()

    # Retrieve patients with loans
    c.execute("SELECT patient_id, loan_amount, start_date, end_date FROM loans")
    loans = c.fetchall()

    # Close the database connection
    conn.close()

    # Combine the results and return
    results = exemptions + loans
    return results

# Example usage
patients = get_patients_with_exemptions_or_loans()
for patient in patients:
    print(patient)
