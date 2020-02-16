from enum import Enum

from yarl import URL


class Environment(Enum):
    SANDBOX = 'SANDBOX'
    PRODUCTION = 'PRODUCTION'
    STREAMING = 'STREAMING'


EnvironmentURL = {
    Environment.SANDBOX: URL('https://api-invest.tinkoff.ru/openapi/sandbox/'),
    Environment.PRODUCTION: URL('https://api-invest.tinkoff.ru/openapi/'),
    Environment.STREAMING: URL(
        'wss://api-invest.tinkoff.ru/openapi/md/v1/md-openapi/ws'),
}


__all__ = [
    'Environment',
    'EnvironmentURL',
]
