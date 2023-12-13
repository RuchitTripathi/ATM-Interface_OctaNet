# ATM Console Application

## Overview

This console-based ATM application is designed to simulate the functionality of an Automated Teller Machine (ATM). It is built using Python and includes a set of classes to manage user accounts, transactions, and the ATM itself. This project was completed during an internship at OctaNet Software Services.

## Features

1. **User Authentication:** Users are required to enter their User ID and PIN to access ATM functionalities.

2. **Main Menu Options:**
    - **Display Transaction History:** View a detailed history of transactions.
    - **Withdraw:** Withdraw funds from the user account.
    - **Deposit:** Deposit funds into the user account.
    - **Transfer:** Transfer funds to another user's account.
    - **Logout:** Logout from the current user account.

3. **Transaction History:**
    - Each transaction is recorded with a unique ID, type, amount, and timestamp.

4. **Error Handling:**
    - The application handles various input errors to ensure a smooth user experience.

## Classes

### 1. `User`

- Represents a user account with attributes such as User ID, PIN, name, and balance.
- Provides a method to display user information.

### 2. `Account`

- Manages user accounts and transaction history.
- Allows users to add transactions, display balances, and view transaction history.

### 3. `Transaction`

- Represents a transaction with a unique ID, type, amount, and timestamp.
- Provides a method to display transaction details.

### 4. `ATM`

- Simulates the ATM system with predefined user accounts.
- Handles user authentication and provides a menu for different operations.
- Displays transaction history for the current user.

### 5. `App`

- Main application class to run the ATM simulation.
- Manages user interaction, authentication, and processing of various operations.

## How to Run

1. Clone the repository to your local machine.
2. Run the `app.py` file using a Python interpreter.

```bash
python app.py
```

3. Follow the on-screen instructions to navigate through the ATM functionalities.

## Project Completion

This project was developed during an internship at OctaNet Software Services as part of the hands-on learning experience. It demonstrates the implementation of a console-based ATM application with user authentication, transaction management, and various banking operations.

Feel free to explore, provide feedback, or contribute to enhance the functionality of this ATM application.

**Author:** Ruchit Tripathi 
**Contact:** ruchittripathi21@gmail.com 
**Internship Period:** 1/09/2023 to 1/10/2023  
**Company:** OctaNet Software Services
