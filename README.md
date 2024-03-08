# Pretty Logger
## Description
This is python package has been developed to emulate the nest.js integrated logger.
It allows for colorful terminal logs as well as activating or deactivating debug/warn or error print statements.

---

## In-code usage
To use it, create an instance of the Logger class within the class you wish to have this logger run for and give it the class's name.
Once you have an object for the logger, replace all instances of your print statements to the new object.
Now you will be able to decide if that print statement should be of type: log, debug, or error.
### Example:
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
        self.logger = Logger('TestClass')
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
After the pretty logger has been implemented, you can use the following flags when launching your python script to activate the various logs:
- `--pretty-debug`: Allows for displaying debug/warn logs
- `--pretty-error`: Allows for displaying error logs
- `--pretty-none`: Disables all logs for script

### Example:
This will run the script `main.py` with all the possible loggers:
```
python main.py --pretty-debug --pretty-error
```
