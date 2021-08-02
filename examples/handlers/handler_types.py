""" Handlers serve as a way to manage connections to the file logs being stored.

"""
import sys
import logging


#StreamHandler - send logs to file-like objects in memory
def stream_handler(stream_name):
    from logging import StreamHandler
    hdlr = StreamHandler(stream_name) ## will use sys.stderr by default
    log = logging.getLogger("shared")
    log.addHandler(hdlr)

    send_a_thousand(log)

#FileHandler - send logs to disk
def file_handler(log_location):
    from logging import FileHandler
    hdlr = FileHandler(log_location, mode="a", encoding="UTF-8")
    log = logging.getLogger("shared")
    log.addHandler(hdlr)

    send_a_thousand(log)


#RotatingFileHandler - send logs to disk with a maximum bytesize
def rotating_file_handler(log_location):
    from logging.handlers import RotatingFileHandler
    hdlr = RotatingFileHandler(log_location, maxBytes=2000, backupCount=10)
    log = logging.getLogger("shared")
    log.addHandler(hdlr)

    send_a_thousand(log)

#TimedRotatingFileHandler - send logs to disk on a timed interval
def timed_rotating_file_handler(log_location):
    from logging.handlers import TimedRotatingFileHandler
    from datetime import time
    rollover_time = time(11, 34, second=55)
    hdlr = TimedRotatingFileHandler(log_location, when="H", backupCount=10, atTime=rollover_time)

    log = logging.getLogger("shared")
    log.addHandler(hdlr)

    send_a_thousand(log)

def send_a_thousand(log):
    for _ in range(1000):
        log.warning("Check the logs, they're there!")

if __name__ == "__main__":
    # stream_handler(sys.stderr)
    # file_handler("logs/file_handling")
    # rotating_file_handler("logs/rotation/rotation_file_handling")
    timed_rotating_file_handler("logs/rotation/timed/timed_file_handling")
