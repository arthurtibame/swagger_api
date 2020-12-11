from app import flask_app

if __name__ == "__main__":
    #import logging
    #logFormatStr = '[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s'
    #logging.basicConfig(format = logFormatStr, filename = "logs/global.log", level=logging.DEBUG)
    #formatter = logging.Formatter(logFormatStr,'%m-%d %H:%M:%S')
    #fileHandler = logging.FileHandler("logs/summary.log")
    #fileHandler.setLevel(logging.DEBUG)
    #fileHandler.setFormatter(formatter)
    #streamHandler = logging.StreamHandler()
    #streamHandler.setLevel(logging.DEBUG)
    #streamHandler.setFormatter(formatter)
    #flask_app.logger.addHandler(fileHandler)
    #flask_app.logger.addHandler(streamHandler)
    #flask_app.logger.info("Logging is set up.")
    flask_app.run(host="0.0.0.0", port=8080)
