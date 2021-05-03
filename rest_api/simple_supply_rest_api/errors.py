
import json

from aiohttp.web import HTTPError


class _ApiError(HTTPError):
    status_code = None
    message = None

    def __init__(self):
        assert self.status_code is not None, 'Invalid ApiError, status not set'
        assert self.message is not None, 'Invalid ApiError, message not set'

        super().__init__(
            content_type='application/json',
            text=json.dumps(
                {'error': self.message},
                indent=2,
                separators=(',', ': '),
                sort_keys=True))


class ApiBadRequest(_ApiError):
    def __init__(self, message):
        self.status_code = 400
        self.message = 'Bad Request: ' + message
        super().__init__()


class ApiInternalError(_ApiError):
    def __init__(self, message):
        self.status_code = 500
        self.message = 'Internal Error: ' + message
        super().__init__()


class ApiNotFound(_ApiError):
    def __init__(self, message):
        self.status_code = 404
        self.message = 'Not Found: ' + message
        super().__init__()


class ApiUnauthorized(_ApiError):
    def __init__(self, message):
        self.status_code = 401
        self.message = 'Unauthorized: ' + message
        super().__init__()
