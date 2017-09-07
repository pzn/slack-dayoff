class OauthAccessException(Exception):
    def __init__(self, message, errors):
        super(OauthAccessException, self).__init__(message)
        self.errors = errors

class AccessTokenException(Exception):
    def __init__(self, message, errors):
        super(AccessTokenException, self).__init__(message)
        self.errors = errors

class SlackMissiveException(Exception):
    def __init__(self, message, errors):
        super(SlackMissiveException, self).__init__(message)
        self.errors = errors