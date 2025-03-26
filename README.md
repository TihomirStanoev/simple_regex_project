![regex_bannerg](https://github.com/user-attachments/assets/3a042dca-ddc6-4797-baff-8fb5914715e1)


# 🧩Simple Regex Project 🐍

Simple Python regex project for password validation, email extraction, and phone number extraction.

## ✨Features


* **Interactive Command-Line Interface:**
    * Presents a menu-driven interface for easy interaction.
    * Allows users to choose between password validation, email validation, email extraction, phone number extraction, combined email and phone extraction, and text replacement.
* **Password Validation:**
    * Utilizes the `PasswordValidator` class to check password strength against predefined criteria.
    * Validates passwords for minimum length, uppercase letters, numbers, and special characters.
* **Email Validation:**
    * Uses the `EmailValidator` class to validate email addresses against a comprehensive regular expression.
* **Email and Phone Extraction:**
    * Employs the `Extractor` class to extract email addresses and phone numbers from user-provided text.
    * Provides separate methods for extracting emails and phone numbers, as well as a combined method.
* **Text Replacement:**
    * Offers the `StringProcessor` class for replacing text within a string using regular expressions.
    * Allows the user to select between case sensitive, and insensitive modes.
* **Regular Expression Utility Class (`RegEx`):**
    * Contains pre-defined regular expressions for password validation, email validation, and data extraction.
    * Centralizes regular expression patterns for easy maintenance and reusability.
* **Modular Design:**
    * Organized into separate modules (`manipulate_text.py`, `validators.py`, `regex.py`) for clear separation of concerns.
    * Classes are designed for easy extension and modification.
* **Object-Oriented Implementation:**
    * Uses classes and objects to represent validators and text processors.
    * Enhances code organization and readability.


## 🛠️ Usage

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/TihomirStanoev/simple_regex_project.git
    ```

2.  **Navigate to the project directory:**

    ```bash
    cd simple_regex_project
    ```

3.  **Run the example:**
   
    * Execute the `main.py` script from the `simple_regex_project` directory.

    ```bash
    python main.py
    ```

## Requirements

* Python 3.x
