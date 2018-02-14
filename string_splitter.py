import re
import logger


class NotSplittableError(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


str_pattern = r'^[A-Za-z0-9]+( (-)?[\w,.\'=_*]+)*$'


class StringSplitter(object):

    @staticmethod
    def split(string: str):
        """Return tuple:
            (cmd, args, kwargs)

            throw splitter.NotSplittableError if string is not correctly formatted

            cmd is the first word of string
            args is a list of other words is string
            kwargs is a dict of all words starting with -{word}
            if word is formatted -{word}={word2}, the dict value is word2. None otherwise
        """

        if not re.match(str_pattern, string):
            logger.error("String not matching pattern while trying to split: {}".format(string))
            raise NotSplittableError("String: '{}' not matching pattern".format(string))

        cmd = string.strip().split()[0]
        args = list()
        kwargs = dict()

        for word in string.strip().split()[1:]:
            if re.match(r'^-[A-Za-z0-9]+=[0-9A-Za-z]+$', word):
                kwargs[word.split('=')[0]] = word.split('=')[1]

            elif re.match(r'^-[0-9A-Za-z]+$', word):
                kwargs[word] = None

            elif re.match(r'^[\w.,\'*]+$', word):
                args.append(word)

        return cmd, args, kwargs

    @staticmethod
    def get_command(string: str):
        try:
            cmd, args, kwargs = StringSplitter.split(string)
            return cmd, args, kwargs
        except NotSplittableError:
            return None, None, None
