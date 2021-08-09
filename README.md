# PyLogger
PyLogger is a simple script to create `log` files.

## Installation
Run these commands in your project folder.
-	Windows:
	```bash
	mkdir PyLogger
	Invoke-WebRequest https://raw.githubusercontent.com/Patitotective/PyLogger/main/main.py -OutFile PyLogger/main.py
	```
-	macOS and Linux:
	```bash
	mkdir PyLogger
	wget https://raw.githubusercontent.com/Patitotective/PyLogger/main/main.py -P PyLogger
	```

Then just import it using:
```py
import PyLogger.main as Logger
```

Usage
---
### `Logger`

The main class is `Logger`, with it you can create a file and log what you want.  
Example:
```py
import PyLogger.main as Logger

logger = Logger.Logger("Logs/log.txt")

logger.log("Successfully created file")
```
This code will generate a file called `log.txt` inside a folder called `Logs`.  
This file should look like:
```
--- [2021-08-09 10:43:00.812990] ---
[2021-08-09 10:43:00.813151] Successfully created file
``` 

If you want to log some large list, instead of using `log` function use `multiple_log` which expects a list (anyways convert the given parameter into a list) and writes the log more efficiently

Every time you run this program it will append more logs to the already existent one, if you want to replace the old file with the new, set `renew` parameter to `True`.  
Example:
```py
import PyLogger.main as Logger

logger = Logger.Logger("Logs/log.txt", renew=True)

logger.log("Successfully created file")
```

### `KeyLogger`

`KeyLogger` class inherits from `Logger` class, it just logs into a file any pressed and released key.  
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
This code will log all pressed keys in `Logs/keylog.txt` and will be stopped when you press `x`.

### `MouseLogger`
`MouseLogger` class inherits from `Logger` class, and it just logs all mouse events into the given file (move, click, scroll).
You can pass to it your custom functions:
-	`on_move`: to this function will be passed `x` and `y`.
-	`on_click`: to this function `x`, `y`, `button` and `pressed` will be passed. For `button` left is `1`, middle is `2` and right is `3`. `pressed` represents if the button was pressed or released. 
-	`on_scroll`: to this function will be passed `x`, `y`, `dx`, `dy`. Where `dy` and `dx` will be if the scroll is up (1), down (-1), left or right, respectively.
Example:
```py
import PyLogger.main as Logger

logger = Logger.MouseLogger("Logs/mouselog.txt")

logger.init_logging()
```

## Links

- GitHub page: https://github.com/Patitotective/PyLogger.

- Contact me:
  - Discord: **patitotective#0127**.
  - Email: **cristobalriaga@gmail.com**.


***v0.1***


