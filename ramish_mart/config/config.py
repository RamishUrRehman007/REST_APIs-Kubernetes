from pyconfigmanager import ConfigFactory


def register_config_manager():
    # Load App Config from external file
    """
    Provide required keys in the following format
    [{<required_class_name>: [<required_key_name>]}]
    :return: ConfigManager object
    """

    required_classes_and_keys = [
        {
            "class_name": "DatabaseConfig",
            "config_keys": [
                "HOST_URL",
                "USERNAME",
                "PASSWORD",
                "DATABASE_NAME",
                "PORT"
            ],
        }
    ]

    config_manager = ConfigFactory.get_config_manager(required_classes_and_keys)
    return config_manager
