from homelink.auth import AbstractAuth


class AuthMock(AbstractAuth):
    """Mocks an authorized request by returning the data in resp_data
    resp_data should be organized by [url][method]"""

    def __init__(self, resp_data):
        self.resp_data = resp_data

    async def request(self, method, url, json=None, **kwargs):
        if not json:
            return RespDataMock(self.resp_data[url][method])
        else:
            return RespDataMock(self.resp_data[url][method][json["command"]])

    def async_get_access_token(self):
        pass


class RespDataMock:
    """Mock to provide data from the .json() method"""

    def __init__(self, resp_data):
        self.resp_data = resp_data

    async def json(self):
        return self.resp_data
