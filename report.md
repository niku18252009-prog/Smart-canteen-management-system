# Smart College Canteen Management and Billing System
## Project Report

## 1. Introduction
The Smart College Canteen Management and Billing System is a beginner-level Python application. It helps a user select food items, enter quantities and calculate the final bill.

## 2. Problem Statement
Manual calculation of food bills can take time and may lead to mistakes. This project provides a simple way to calculate the bill using Python.

## 3. Objectives
- To practice Python programming.
- To use lists for storing menu data.
- To use loops for repeated input.
- To use functions to divide the program into parts.
- To calculate a food bill automatically.
- To provide a simple and readable output.

## 4. Functional Requirements
- Display menu.
- Accept customer name.
- Accept multiple food items.
- Accept quantity.
- Calculate item amount.
- Calculate total.
- Apply discount.
- Display final bill.

## 5. Non-Functional Requirements
- Simple interface through the terminal.
- Correct arithmetic calculations.
- Basic validation for item number and quantity.
- Easy-to-understand code.

## 6. System Architecture
Input -> Order Processing -> Bill Calculation -> Output

## 7. Workflow
1. Start program.
2. Enter customer name.
3. Display menu.
4. Select food item.
5. Enter quantity.
6. Repeat selection until 0 is entered.
7. Calculate item amounts.
8. Calculate total.
9. Apply discount.
10. Display final bill.
11. End.

## 8. Design Decisions
Lists are used because they are simple and are suitable for the current level of the Python course. Functions are used to separate menu display, order taking and bill calculation.

No database or advanced Python library is required.

## 9. Implementation Details
The program has four main functions:
- show_menu()
- take_order()
- make_bill()
- main()

The menu names and prices are stored in two lists. The program uses loops to display the menu and process multiple orders.

## 10. Testing Approach
The program is tested with valid item selections, multiple quantities, invalid item numbers, zero/negative quantities and no order.

## 11. Challenges Faced
- Handling repeated food selection.
- Keeping item numbers connected with prices.
- Calculating the discount correctly.
- Displaying a readable bill.

## 12. Learnings
- Learned how to create and use lists.
- Learned how loops can handle repeated tasks.
- Learned how functions make code easier to organize.
- Practiced if-elif-else conditions.
- Practiced arithmetic calculations.

## 13. Future Enhancements
- Add a graphical user interface.
- Store bills in a file or database.
- Add login for staff.
- Add daily sales reports.
- Add more food categories.

## 14. References
- VITyarthi Python Essentials course material.
- Python 3 language documentation.
