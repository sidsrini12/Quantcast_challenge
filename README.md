# Most Active Cookie

## Problem Statement

Given a cookie log file in the following format:

```text
cookie,timestamp
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00
AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00
4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00
fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00
4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00
```

Write a command line program in your preferred language to process the log file and return the most active cookie for specified day. The example below shows how we'll execute your program.

### Command:

```text
$ ./most_active_cookie cookie_log.csv -d 2018-12-09
```

### Output:

```bash
AtY0laUfhglK3lC7
```

We define the most active cookie as one seen in the log the most times during a given day.

### Assumptions:

- If multiple cookies meet that criteria, please return all of them on separate lines.

```bash
$ ./most_active_cookie cookie_log.csv -d 2018-12-08

SAZuXPGUrfbcn5UA
4sMM2LxV07bPJzwf
fbcn5UAVanZf6UtG
```

- You're only allowed to use additional libraries for testing, logging and cli-parsing. There are libraries for most languages which make this too easy (e.g pandas) and we’d like you to show off you coding skills.
- You can assume -d parameter takes date in UTC time zone.
- You have enough memory to store the contents of the whole file.
- Cookies in the log file are sorted by timestamp (most recent occurrence is first line of the file).

We're looking for a concise, maintainable, extendable and correct solution. We're hoping you'll deliver your solution as production grade code and demonstrate:

- good testing practices,
- knowledge of build systems, testing frameworks, etc.
- clean coding practices (meaningful names, clean abstractions, etc.)

Please use a programming language you’re very comfortable with. The next stage of the interview will involve extending your code.

## Execution Commands

### Run

```bash
./run.sh
```

#### Output

```text
Most Active Cookies on date 2018-12-09:
AtY0laUfhglK3lC7
Most Active Cookies on date 2018-12-08:
SAZuXPGUrfbcn5UA
4sMM2LxV07bPJzwf
fbcn5UAVanZf6UtG
Most Active Cookies on date 2018-12-07:
4sMM2LxV07bPJzwf
Most Active Cookies on date 2018-12-06:

```

### Test

```bash
./test.sh
```

#### Output

```text
..
----------------------------------------------------------------------
Ran 2 tests in 0.003s

OK
```

## Logic

1. I store the input date from the command line
2. I parse the csv file and keep a count of all the cookies that occur on the input date in a hashset with the date as key
3. I use the `Counter()` module to store this count and return a sorted list of the most common cookies in descending order
4. Finally, I return the most active cookies while traversing this list

### Complexity Analysis

- Time: O(N)
- Space: O(N)
  
N is the number of elements in the log file