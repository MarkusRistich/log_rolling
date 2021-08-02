""" Step 2: Understanding logging.basicConfig and its arguments.
"""
# interpreter packages
import logging

# local packages


def load_config_from_args():
    """ Create a basic logging config. This applies most principles, such
        as the level of logging and a default format.
    """

    # A basic config will usually specify a log file and a logging level
    # logging.basicConfig(filename="logs/args.log",
    #                     filemode='w',
    #                     level=logging.INFO)

    # Using asctime allows us to see a better timestamp
    logging.basicConfig(filename="logs/args.log",
                        filemode='w',
                        format='%(asctime)s %(message)s',
                        level=logging.INFO)

    # Storing the name of the file and the logging level for the LogRecord
    # saves a lot of troubleshooting.
    logging.basicConfig(filename="logs/args.log",
                        filemode='w',
                        format='%(asctime)s %(message)s',
                        level=logging.INFO)
    log = logging.getLogger("shared_logger")
    log.info("Now this is a big step up from unreadable logging messages!")


def load_config_from_dict():
    """ Using a config from a dict is helpful if you are picking or moving between files.
        However this relies on external formatting modules, which have long load times
        and introduce dependencies.
    """
    import logging.config as logging_config
    import yaml

    path_to_config = "basic_config.yaml"
    with open(path_to_config, 'rt') as f:
        config = yaml.safe_load(f.read())

    logging_config.dictConfig(config)

    log = logging.getLogger("shared_logger")
    log.info("Better config management, but not perfect.")


def load_config_from_fileConfig():
    """ Best practice format for storing config files as of Python 2.7+
    """
    from logging.config import fileConfig

    path_to_config = "basic_config.ini"
    fileConfig(path_to_config)
    """
    handlers:
        console:
            class : logging.StreamHandler
            formatter: brief
            level   : INFO
            filters: [allow_foo]
            stream  : ext://sys.stdout
        file:
            class : logging.handlers.RotatingFileHandler
            formatter: precise
            filename: logconfig.log
            maxBytes: 1024
            backupCount: 3
    """


    log = logging.getLogger("shared_logger")
    log.info("Now we're using a config effectively!")


def timestamping_logs():
    pass

def autogenerate_new_logfiles():
    pass

if __name__ == "__main__":
    # load_config_from_args()
    # load_config_from_dict()
    load_config_from_fileConfig()