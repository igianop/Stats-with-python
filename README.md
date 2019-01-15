# Stats-with-python
This package use **StackExchange API** to collect and return calculated statistics
# Installation

To be able to use it you must first check the python version of your machine (supports Python 2.7 and above),
after that you must run from cmd:
```
$ pip install requests
```

## How to run the application

Once you are sure that its finished you navigate to the folder you extract the .zip file.
To run the programm you type:
```
python __init__.py 2018-02-03 2018-02-23
```
The two dates determine the range of the result you want to colect.
It must be in the format **YYYY-MM-DD**.

For the given example above the output on your window is:
```
{'accepted_answers_average_score:': 9.84,
 'top_ten_answers_comment_count:': [[48930521, 0],
                                    [48919908, 9],
                                    [48917513, 0],
                                    [48912764, 3],
                                    [48911240, 0],
                                    [48906304, 0],
                                    [48895101, 2],
                                    [48894968, 3],
                                    [48894749, 3],
                                    [48882134, 1]],
 'total_accepted_answers:': 13}
```
at the top_ten_answers_comment_count the first element is the answer id and the second is the comment count for thiw answer.It depends to the score of the answer.
