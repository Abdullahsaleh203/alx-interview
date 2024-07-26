0x08. Making Change
===================

`Algorithm` `Python`

-   By: Dev Nderitu

Requirements
------------

### General

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
-   All your files should end with a new line
-   The first line of all your files should be exactly `#!/usr/bin/python3`
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   Your code should use the `PEP 8` style (version 1.7.x)
-   All your files must be executable

Tasks
-----

### 0\. Change comes from within

mandatory

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount `total`.

-   Prototype: `def makeChange(coins, total)`
-   Return: fewest number of coins needed to meet `total`
    -   If `total` is `0` or less, return `0`
    -   If `total` cannot be met by any number of coins you have, return `-1`
-   `coins` is a list of the values of the coins in your possession
-   The value of a coin will always be an integer greater than `0`
-   You can assume you have an infinite number of each denomination of coin in the list
-   Your solution's runtime will be evaluated in this task

```
carrie@ubuntu:~/0x08-making_change$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

carrie@ubuntu:~/0x08-making_change$

```

```
carrie@ubuntu:~/0x08-making_change$ ./0-main.py
7
-1
carrie@ubuntu:~/0x08-making_change$

```

**-------------CODE IMPLEMENTATION ---------------**

1. You initialize the `dp` array with the first element as 0 and the rest as infinity (`float("inf")`).

2. You iterate through each coin value and update the `dp` array accordingly to find the minimum number of coins needed for each possible total.

3. Finally, you return `dp[-1]` (last element of the `dp` array), which represents the minimum number of coins needed to meet the total. If it's still infinity, you return -1 to indicate that the total cannot be achieved with the given coins.
