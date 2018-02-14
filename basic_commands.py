import settings


class BasicHandler(object):

    @staticmethod
    def get_help_str():
        with open(settings.COMMANDS_FILENAME, 'r') as f:
            return f.read()
