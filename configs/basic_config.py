""" Step 2: Understanding logging.basicConfig and its arguments.
"""
# interpreter packages
import logging

# local packages


def load_config_from_args():
    """ Create a basic logging config. This applies most principles, such as the level of logging and a default format.
    """

    # no FileHandler, only a StreamHandler
    logging.basicConfig(filename="logs/args.log",
                        filemode='w',
                        level=logging.INFO)

    # using asctime allows us to see a better timestamp
    # logging.basicConfig(filename="logs/args.log",
    #                     filemode='w',
    #                     format='%(asctime)s %(message)s',
    #                     level=logging.INFO)

    log = logging.getLogger("shared_logger")
    log.info("Now this is a big step up from unreadable logging messages!")


def load_config_from_dict():
    """ Using a config from a dict is helpful if you are picking or passing a config between files.
        In practice, it's going to be much easier to understand how the file read processes, but
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
    from logging.config import fileConfig
    fileConfig('basic_config.ini')

    log = logging.getLogger("shared_logger")

    log.info("Now we're using a config effectively!")


def timestamping_logs():
    pass

def autogenerate_new_logfiles():
    pass

if __name__ == "__main__":
    load_config_from_args()
    # load_config_from_dict()
    # load_config_from_fileConfig()