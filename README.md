# Pretty Logger
## Description
This is python package has been developed to emulate the nest.js integrated logger.
It allows for colorful terminal logs as well as activating or deactivating debug/warn or error print statements. <br>
It is able to save all logs to text files for better quiet program running, or could be used while running in verbose. <br>
Lastly, it allows for the overwrite of print statements within a function by the use of function decorators.
## Install
```
pip install kayer-pretty-logger
```

---

## In-code usage
To use the pretty logger, you have two main options which I have split into procedural or object-oriented programming examples.
### Example 1 - Procedural Programming:
To use it with procedural programming, you may either create an instance of the Logger similarly to the OOP example seen later,
or you may use the decorators found in `pretty_logger.decorators` to overwrite the print statements. 
In this example we will show you how to use the decorators to change the behaviour of your functions. <br><br>
The code before:
```python
def my_function(a: int, b: int) -> int:
    print('We have entered the function')
    return a + b

print(my_function(1, 2))
```
The updated code:
```python
from pretty_logger.decorators import pretty_debug

@pretty_debug
def my_function(a: int, b: int) -> int:
    print('We have entered the function')
    return a + b

print(my_function(1, 2))
```
### Example 2 - OOP:
To use it in an OOP context, you first create an instance of the Logger class within the class you wish to have this logger run for and give it the class's name.
Once you have an object for the logger, replace all instances of your print statements to the new object's log functions.
Here you will be able to decide if your previous print statements should be of type: log, debug, or error. <br><br>
The code before:
```python
class TestClass:
    def __init__(self):
        print('Object created')

    def something(self, number: str) -> int:
        print('We are here')
        
        try:
            return int(number)
        except ValueError as e:
            print(e)
            
            return 0
```
The updated code:
```python
from pretty_logger import Logger

class TestClass:
    logger: Logger
    
    def __init__(self):
        self.logger = Logger(TestClass.__name__)
        self.logger.log('Object created')

    def something(self, number: str) -> int:
        self.logger.debug('We are here')
        
        try:
            return int(number)
        except ValueError as e:
            self.logger.error(e)
            
            return 0
```

---

## Running a program which has a Pretty Logger
After the pretty logger has been implemented, you can use the following flags when launching your python script to customize you log experience:
- `--pretty-debug`: Allows for displaying debug/warn logs
- `--pretty-error`: Allows for displaying error logs
- `--pretty-all`: Activates all logs for script
- `--pretty-none`: Disables all logs for script
- `--pretty-save`: Activates the system which will save all logs to their corresponding files
- `--pretty-save-silent`: Activates the system which will save all logs to their corresponding files in silent mode
- `--logger-folder-path path/to/folder`: [Optional] Custom path to a directory to save the logs in

### Examples:
This will run the script `main.py` with all the possible loggers:
```
python main.py --pretty-all
```
This will run the script `main.py` with in silent mode and save the logs to the `./custom_logs/` directory:
```
python main.py --pretty-save-silent --logger-folder-path ./custom_logs/
```

---

## Buy me a coffee
If you wish to offer me a coffee, please buy yourself one instead and cheer in my name xD