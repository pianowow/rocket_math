## Rocket Math

![rocket math image](images/rocket-math.png)

A curses based terminal program to practice addition, subtraction, multiplication and division.


#### How to run
```
❯ ./rocket-math.py -h
usage: rocket-math.py [-h] [-s] [operation] [number]

positional arguments:
  operation      operation (a,s,m,d)
  number         number of questions/seconds

options:
  -h, --help     show this help message and exit
  -s, --seconds  fixed seconds mode
```
#### Examples

For 50 multiplication questions (default):

`❯ ./rocket-math.py`

For 50 subtraction questions:

`❯ ./rocket-math.py s`

For 60 seconds of as many multiplication questions as you can answer:

`❯ ./rocket-math.py -s m 60`

