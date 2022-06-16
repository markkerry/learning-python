# StackOverflow Questions

Name: Mark Kerry | Country: England, UK | Email: mark-kerry@outlook.com | Website: https://markkerry.github.io | GitHub: https://github.com/markkerry

## Video Demo:  <URL HERE>

## Description:

This program which performs an HTTP GET request against the StackExchange API for the latest questions on StackOverflow, specified by tag, and returns them in appending order of last activity. The person running the program can specify the tag, count of questions to gather, and  whether output the results as text or table.

There are two modules/libraries required to install, which are specified in the requirements.txt file.

* pyshorteners
* tabulate

Pyshorteners will take the URL of the post and shorten it to a "tinyurl". Tabulate will output the results to a table if specified.

### Help

Get the programs built-in help as follows:

```terminal
python project.py -h
python project.py --help
```

Will return:

```terminal
usage: project.py [-h] [-t TAG] [-c COUNT] [-o {text,table}]

Get the latest Stack Overflow questions from desired 'tag'

optional arguments:
  -h, --help            show this help message and exit
  -t TAG, --tag TAG     Subject tag to search for E.g. 'python', 'c' or 'cs50'
  -c COUNT, --count COUNT
                        Number of items to show
  -o {text,table}, --output {text,table}
                        Output as text or table
```

Argpasrse does have some defaults if the user does not specify any arguments, for example `python project.py`. The tag is set to `CS50`, the count is set to `10`, and the output is set to `text`

### Example 1

In the following example I will specify the tag as `CS50`, the count to return as `3` and to output as a `table`

```terminal
 python project.py -t CS50 -c 3 -o table
```

Will return a table similar to as follows:

```terminal
Gathering information... Tag CS50, count 3, output table

╒══════════════════════════════════════════════════════════════════════╤══════════════════════════════╤═════════════════════╤══════════════════════╕
│ Title                                                                │ URL                          │ Creation Date       │ Last Activity Date   │
╞══════════════════════════════════════════════════════════════════════╪══════════════════════════════╪═════════════════════╪══════════════════════╡
│ Why can an array used in fread/fwrite in a position of a buffer b... │ https://tinyurl.com/2aw4wtpq │ 2022-06-13 19:29:28 │ 2022-06-16 13:28:07  │
├──────────────────────────────────────────────────────────────────────┼──────────────────────────────┼─────────────────────┼──────────────────────┤
│ cs50 Pset5 Speller segmentation fault and memory leaks               │ https://tinyurl.com/26jf8v4b │ 2022-06-15 16:43:06 │ 2022-06-16 06:37:10  │
├──────────────────────────────────────────────────────────────────────┼──────────────────────────────┼─────────────────────┼──────────────────────┤
│ CS50 Speller - Check function stops working after finding first 4... │ https://tinyurl.com/262acu3v │ 2022-06-15 19:41:01 │ 2022-06-15 22:52:00  │
╘══════════════════════════════════════════════════════════════════════╧══════════════════════════════╧═════════════════════╧══════════════════════╛
```

### Example 2

The same command but this time to return the output as `text`

```terminal
 python project.py -t CS50 -c 3 -o text
```

Will return text similar to as follows:

```terminal
Gathering information... Tag CS50, count 3, output text

Title: Why can an array used in fread/fwrite in a position of a buffer b...
URL: https://tinyurl.com/2aw4wtpq
Creation date: 2022-06-13 19:29:28
Last activity date 2022-06-16 13:28:07

Title: cs50 Pset5 Speller segmentation fault and memory leaks
URL: https://tinyurl.com/26jf8v4b
Creation date: 2022-06-15 16:43:06
Last activity date 2022-06-16 06:37:10

Title: CS50 Speller - Check function stops working after finding first 4...
URL: https://tinyurl.com/262acu3v
Creation date: 2022-06-15 19:41:01
Last activity date 2022-06-15 22:52:00
```

### Example 3

If you enter a `tag` which does not exist:

```terminal
 python project.py -t footag -c 3 -o text
```

The program will return the following:

```terminal
No posts for tag footag found. Try another
```

> __NOTE__: _It can take some time to convert the URL to a tinyurl. So the higher the count, the longer it takes for the program to run. If you specify a count of greater than 25 your will receive the following_
>>  

```terminal
python project.py -t java -c 50 -o text

A count of 50 is too many and will take some time. Try 25 or less.
```