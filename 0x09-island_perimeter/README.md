0x09. Island Perimeter
======================

AlgorithmPython


-   Weight: 1

Requirements
------------

### General

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
-   All your files should end with a new line
-   The first line of all your files should be exactly `#!/usr/bin/python3`
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   Your code should use the `PEP 8` style (version 1.7)
-   You are not allowed to import any module
-   All modules and functions must be documented
-   All your files must be executable

Tasks
-----

### 0\. Island Perimeter

mandatory

Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`:

-   `grid` is a list of list of integers:
    -   0 represents water
    -   1 represents land
    -   Each cell is square, with a side length of 1
    -   Cells are connected horizontally/vertically (not diagonally).
    -   `grid` is rectangular, with its width and height not exceeding 100
-   The grid is completely surrounded by water
-   There is only one island (or nothing).
-   The island doesn't have "lakes" (water inside that isn't connected to the water surrounding the island).

```
guillaume@ubuntu:~/0x09$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

guillaume@ubuntu:~/0x09$
guillaume@ubuntu:~/0x09$ ./0-main.py
12
guillaume@ubuntu:~/0x09$

```
**-----------SOLUTION-----------**

```
#!/usr/bin/python3
"""
Island Perimeter
"""

def island_perimeter(grid):
    """
     returns the perimeter of the island described in grid
    :param grid:
    :return:
    """
    area = 0
    for row in grid + list(map(list, zip(*grid))):
        for i1, i2 in zip([0] + row, row + [0]):
            area += int(i1 != i2)
    return area
```

**----------------CODE EXPLANATION-------------------**

- It uses a clever trick to calculate the perimeter by iterating over the rows of the grid and adding the number of transitions from land (1) to water (0) for each row, as well as the number of transitions between rows.

Code Breakdown:

`grid + list(map(list, zip(*grid)))` concatenates the original grid with its transpose. This is done to efficiently iterate through both rows and columns of the grid in a single loop.

`for row in grid + list(map(list, zip(*grid)))`: iterates through each row of the combined grid (original grid and its transpose).

`for i1, i2 in zip([0] + row, row + [0])`: iterates through each pair of adjacent elements in the row, including the beginning and end.

`area += int(i1 != i2)` increments the area by 1 whenever there is a transition from land (1) to water (0) or vice versa, which effectively counts the perimeter.

This code is a great example of utilizing the properties of the grid to simplify the perimeter calculation and avoid nested loops. It produces the same output as the previous code you provided, which is 12 for the given example.
