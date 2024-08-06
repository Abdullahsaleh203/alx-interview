0x00. Pascal's Triangle
=======================

Algorithm Python

### Concepts

*For this project, we expect you to look at this concept:*

- [Technical interview](https://alx-intranet.hbtn.io/concepts/100005)

Tasks
-----

### 0\. Pascal's Triangle



Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal's triangle of `n`:

- Returns an empty list if `n <= 0`
- You can assume `n` will be always an integer

```
guillaume@ubuntu:~/0x00$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/0x00$
guillaume@ubuntu:~/0x00$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
guillaume@ubuntu:~/0x00$

```

**Repo:**

- GitHub repository: `alx-interview`
- Directory: `0x00-pascal_triangle`
- File: `0-pascal_triangle.py`

**SOLUTION**

```
def pascal_triangle(n):
    """
         returns a list of lists of
         integers representing
          the Pascal’s triangle of n
         Returns an empty list if n <= 0
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle

-----------------------------------------------------------------
The pascal_triangle function you provided generates Pascal's triangle up to a given number of rows n. Pascal's triangle is a triangular array of binomial coefficients, named after the French mathematician Blaise Pascal. Each number in the triangle is the sum of the two numbers directly above it.

-----------------------------------------------------------------

The function starts by checking if n is less than or equal to 0.
If it is, an empty list is returned because Pascal's triangle is not defined for non-positive values of n.

If n is greater than 0, an initial row [1] is added to the triangle list.
This represents the first row of Pascal's triangle, which always contains a single element, 1.

Then, a loop runs from 1 to n-1 (excluding n).
This loop generates each row of the triangle starting from the second row.

Inside the loop, a new row list is initialized with the first element as 1.
This represents the leftmost element of each row, which is always 1.

Another loop runs from 1 to i-1 (excluding i), where i is the current row number.
This loop calculates the values between the leftmost and rightmost elements of each row.

Inside the nested loop, the value at position (i-1, j-1) and the value
at position (i-1, j) in the previous row are added together and appended to the current row.
This step computes the binomial coefficients.

After the nested loop, the rightmost element of each row, which is always 1, is appended to the row.

Finally, the completed row is appended to the triangle list.

After the outer loop completes, the function returns the triangle list,
which represents Pascal's triangle up to n rows.

```
