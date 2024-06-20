0x03. Log Parsing
=================

AlgorithmPython



Requirements
------------

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `PEP 8` style (version 1.7.x)
- All your files must be executable
- The length of your files will be tested using `wc`

Tasks
-----

### 0\. Log parsing

mandatory

Write a script that reads `stdin` line by line and computes metrics:

- Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>` (if the format is not this one, the line must be skipped)
- After every 10 lines and/or a keyboard interruption (`CTRL + C`), print these statistics from the beginning:
  - Total file size: `File size: <total size>`
  - where `<total size>` is the sum of all previous `<file size>` (see input format above)
  - Number of lines by status code:
    - possible status code: `200`, `301`, `400`, `401`, `403`, `404`, `405` and `500`
    - if a status code doesn't appear or is not an integer, don't print anything for this status code
    - format: `<status code>: <number>`
    - status codes should be printed in ascending order

**Warning:** In this sample, you will have random value - it's normal to not have the same output as this one.

```py
alexa@ubuntu:~/0x03-log_parsing$ cat 0-generator.py
#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()

alexa@ubuntu:~/0x03-log_parsing$ ./0-generator.py | ./0-stats.py
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
Traceback (most recent call last):
  File "./0-stats.py", line 15, in <module>
Traceback (most recent call last):
  File "./0-generator.py", line 8, in <module>
    for line in sys.stdin:
KeyboardInterrupt
    sleep(random.random())
KeyboardInterrupt
alexa@ubuntu:~/0x03-log_parsing$

```

```py
MAIN FILE

#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()

```

```
----Explanation------
The Above Code generates random log entries and writes them to the standard output (stdout).
Each log entry is in the format of an Apache log line and consists of the following information:

- IP address (randomly generated four integers separated by periods)
- Timestamp (current date and time)
- HTTP request ("GET /projects/260 HTTP/1.1")
- HTTP status code (randomly chosen from a list of status codes: 200, 301, 400, 401, 403, 404, 405, 500)
- Random file size (a random integer between 1 and 1024)


-----Random Log Generation -----
The code uses a loop (for i in range(10000)) to generate 10,000 log entries.
 For each iteration, it uses the random module to generate random numbers for the IP address,
 status code, and file size.

-----Sleeping between Log Entries --------
After generating each log entry, the code uses random.random() to obtain a random
floating-point number between 0 and 1, which is then used as the argument to sleep() to introduce
a random delay before generating the next log entry.
This simulates random time intervals between log entries,
which is often seen in real log data.

-----Writing Log Entries to stdout -----------
Each log entry is constructed as a formatted string and written to the
standard output using sys.stdout.write().
The sys.stdout.flush() call is not present here,
but it would be helpful to flush the output buffer if log entries
are not immediately displayed on the console.
```

```py
import sys

if __name__ == '__main__':

    filesize, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        print("File size: {:d}".format(filesize))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                filesize += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_stats(stats, filesize)
        print_stats(stats, filesize)
    except KeyboardInterrupt:
        print_stats(stats, filesize)
        raise
```

```
-----CODE EXPLANATION----

Python script for parsing log entries from standard input (stdin) and calculating
statistics based on the HTTP status codes and the accumulated file size, just like the previous version.

However, it lacks the log entry generation part that we had in the previous discussion.
Instead, this version expects you to provide log entries manually,
line by line, via the terminal.

-------- Initialization ---------------
The script initializes variables filesize and count to 0.
It also creates a list codes containing various HTTP status codes (strings),
and a dictionary stats with initial counts set to 0 for each status code.

---------Printing Statistics----------------
The script defines a function print_stats to print the calculated statistics.
It takes two parameters: stats (the dictionary with status code counts) and file_size (the accumulated file size).
The function prints the total file size and the count for each HTTP status code present in the log entries.
It only prints status codes with non-zero counts.

----------Parsing Log Entries-----------------
The script reads log entries line by line from standard input (stdin) using a for loop.
For each log entry, it increments the count variable,
splits the line into individual parts (using split()),
and tries to extract the status code and file size.
If the status code is one of the codes in the codes list,
it updates the count for that status code in the stats dictionary.

----------Accumulating File Size -----------------
The script also tries to extract the file size from each log entry
and accumulates it in the filesize variable.

-----------Printing Statistics Periodically----------------
The script checks if count % 10 == 0, which means every 10 log entries processed,
it prints the current statistics up to that point using the print_stats function.

-------------Printing Final Statistics-------------------
After processing all the log entries, the script prints the final statistics using the print_stats function.

--------------KeyboardInterrupt Handling ------------------
The script catches a KeyboardInterrupt (e.g., when the user presses Ctrl+C)
and prints the statistics up to that point before raising the KeyboardInterrupt again to terminate the script.
```
