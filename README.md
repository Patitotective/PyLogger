# PyLogger
PyLogger is a simple script to create `log` files.

## Installation
Run these commands in your project folder.
Windows:
```sh
mkdir PyLogger
Invoke-WebRequest https://raw.githubusercontent.com/Patitotective/PyLogger/main/main.py -OutFile PyLogger/main.py
```
macOS and Linux:
```sh
mkdir PyLogger
wget https://raw.githubusercontent.com/Patitotective/PyLogger/main/main.py -P PyLogger
```

Then just import it using:
```py
import PyLogger.main as Logger
```

## Usage
-	`Logger`

	The main class is `Logger`, with it you can create a file and log what you want.  
	Example:
	```py
	import PyLogger.main as Logger

	logger = Logger.Logger("Logs/log.txt")

	logger.log("Succesfuly created file")
	```
	This code will generate a file called `log.txt` inside a folder called `Logs`.  
	This file should look like:
	```
	--- [2021-08-09 10:43:00.812990] ---
	[2021-08-09 10:43:00.813151] Succesfuly created file
	``` 

	Everytime you run this program it will append more logs to the already existent one, if you want to replace the old file with the new, set `renew` parameter to `True`.  
	Example:
	```py
	import PyLogger.main as Logger

	logger = Logger.Logger("Logs/log.txt", renew=True)

	logger.log("Succesfuly created file")
	```

-	`KeyLogger`

	`KeyLogger` class inherits from `Logger` class, it just logs into a file any pressed and realeased key.  
	Example: 
	```py
	import PyLogger.main as Logger

	logger = Logger.KeyLogger("Logs/keylog.txt")

	logger.init_logging()
	```

	This will log until you press `escape`, or kill the program.
	You can define your own `on_press` and `on_release` function and pass them into `KeyLogger.init_logging` function.

	Also you can change the escape key by changing `on_press_escape_key` or `on_release_escape_key`, which needs to be a string or a `Logger.Key.KEY` where `KEY` is your key (from `pynput.Key`).  
	Example:
	```py
	import PyLogger.main as Logger

	logger = Logger.KeyLogger("Logs/keylog.txt")

	logger.init_logging(on_release_escape_key="x")
	```
	This code will log all pressed keys in `Logs/keylog.txt` and will be stoped when you press `x`.

	 
## Links

- GitHub page: https://github.com/Patitotective/PyLogger.

- Contact me:
  - Discord: **patitotective#0127**.
  - Email: **cristobalriaga@gmail.com**.


***v0.1***


