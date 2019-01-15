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
{'accepted_answers_average_score:': 9.75,
 'top_ten_answers_comment_count:': [[10, 48705695],
                                    [9, 48919908],
                                    [3, 48912764],
                                    [3, 48894968],
                                    [3, 48894749],
                                    [2, 48895101],
                                    [2, 48893017],
                                    [2, 48874269],
                                    [2, 48860937],
                                    [2, 48814356]],
 'total_accepted_answers:': 12}
```
