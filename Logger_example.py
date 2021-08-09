import main as Logger # import PyLogger.main as Logger

logger = Logger.Logger("Logs/log.txt")

logger.log("Successfully created file")
logger.multiple_log([f"event{i}" for i in range(100)])