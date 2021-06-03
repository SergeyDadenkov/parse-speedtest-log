def config_parser(config_path):
    with open(config_path, 'r') as config_file:
        config = dict()
        lines = list(filter(lambda x: x != '\n', config_file.readlines()))
        for line in lines:
            key, value = line.split(' = ')
            config[key] = value.split('\n')[0]
        return config
