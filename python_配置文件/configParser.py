from configparser import ConfigParser

masks = "masks.cfg"
config = "config.ini"
section_name = "data"

def ConvertIfStringIsInt(input_string):
    try:
        float(input_string)
        try:
            if int(input_string) == float(input_string):
                return int(input_string)
            else:
                return float(input_string)
        except ValueError:
            return float(input_string)

    except ValueError:
        return input_string

if __name__ == '__main__':
    parser = ConfigParser()
    parser.optionxform = str
    parser.read(config)
    for name, value in parser.items(section_name):
        # value = ConvertIfStringIsInt(value)
        print(name)
        print(value)