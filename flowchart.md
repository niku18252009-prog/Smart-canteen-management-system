# Project Workflow / Flowchart

```text
START
  |
  v
Enter Customer Name
  |
  v
Display Menu
  |
  v
Select Item
  |
  +---- Is item number 0? ---- Yes ----> Calculate Bill
  |                                      |
  No                                     v
  |                                  Apply Discount
  v                                      |
Enter Quantity                           v
  |                                  Display Bill
  v                                      |
Add Item to Order                        v
  |                                     END
  +----------> Display Menu
```

## Simple System Architecture

```text
+------------------+
|      USER        |
+--------+---------+
         |
         v
+------------------+
|   Order Input    |
+--------+---------+
         |
         v
+------------------+
| Python Processing|
|  Lists + Loops   |
| If-Else + Funcs  |
+--------+---------+
         |
         v
+------------------+
| Bill Calculation |
+--------+---------+
         |
         v
+------------------+
|   Final Output   |
+------------------+
```
