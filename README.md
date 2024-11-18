# Atm-System

ATM System - Python Implementation
This project is a Python-based ATM system that simulates basic banking functionalities. It uses a CSV file to store and manage account details, such as user name, password, account number, balance, and PIN. The system incorporates PIN verification to ensure secure transactions.

Features
Secure Authentication: Users log in with their name and password for added security.
PIN Verification: For any transaction (withdrawal, deposit, or balance inquiry), users must provide the correct 4-digit PIN. If the PIN is incorrect, the operation will be denied, mimicking real-world ATM security protocols.
Account Balance Inquiry: Users can view their current account balance.
Cash Withdrawal: Ensures sufficient funds and correct PIN verification before processing.
Cash Deposit: Allows users to deposit money into their accounts after PIN verification.
Data Persistence: All account details are stored in a CSV file and dynamically updated.
CSV File Format
The accounts.csv file is used to store account details in the following format:

Name	Password	Account Number	Balance	PIN
Aditya	myaccount	5391 0375 9387 5309	1223	1234
CSV Fields
Name: The account holder's name (string).
Password: The account password for secure authentication (string).
Account Number: A unique 16-digit account number (string).
Balance: The account's current balance (integer or float).
PIN: A 4-digit numeric PIN required for transactions (integer).
PIN Functionality
The user must enter their PIN to access any account feature beyond login.
Three failed PIN attempts will lock the session, requiring the user to restart the application.
Correct PIN entry allows transactions to proceed seamlessly.
Prerequisites
Ensure you have the following before running the program:

Python 3.8 or higher installed.
The accounts.csv file in the project directory with the correct format.
Installation
Clone this repository:

bash
Copy code
git clone https://github.com/yourusername/atm-system-python.git
cd atm-system-python
Install dependencies: (No external libraries are needed; Python's standard library suffices.)

Place the accounts.csv file in the project directory.

Usage
Run the Python script:

bash
Copy code
python atm_system.py
Follow the on-screen prompts:

Log in with your name and password.
Enter your PIN for transactions.
Perform desired actions such as balance inquiry, withdrawal, or deposit.
Code Structure
atm_system.py: The main script containing the ATM logic.
accounts.csv: The data file storing account information.
Features to Add
Future enhancements might include:

Password and PIN encryption for enhanced security.
GUI-based interface for improved user experience.
Enhanced error handling for input validation.
Support for multiple concurrent sessions.
Contribution
Contributions are welcome! To contribute:

Fork this repository.
Create a new branch:
bash
Copy code
git checkout -b feature-name
Commit your changes and push them to the branch.
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
Aditya Deshmukh
GitHub Profile
Feel free to reach out with feedback, suggestions, or feature requests!








