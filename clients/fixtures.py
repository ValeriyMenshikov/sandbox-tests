from pathlib import Path

import pytest
import structlog
from vyper import v

import clients.http.account_service as account_service
import clients.http.auth_service as auth_service
import clients.http.mail_service as mail_service
import clients.http.register_service as register_service
import clients.http.users_service as users_service

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(
            indent=4,
            ensure_ascii=True,
        )
    ]
)

options = (
    "service.mail_service_mail_api",
    "service.account_service_account_api",
    "service.users_service_user_api",
    "service.auth_service_auth_api",
    "service.register_service_account_api",
)


@pytest.fixture(scope="session", autouse=True)
def set_config(request: pytest.FixtureRequest) -> None:
    config = Path(__file__).parent.parent.joinpath("config")
    config_name = request.config.getoption("--env")
    v.set_config_name(config_name)
    v.add_config_path(config)
    v.read_in_config()
    for option in options:
        v.set(f"{option}", request.config.getoption(f"--{option}"))


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--env", action="store", default="prod", help="run stg")

    for option in options:
        parser.addoption(f"--{option}", action="store", default=None)


@pytest.fixture
async def mail_service_mail_api() -> mail_service.MailApi:
    configuration = mail_service.Configuration(host=v.get("service.mail_service_mail_api"))
    api_client = mail_service.ApiClient(configuration=configuration)
    return mail_service.MailApi(api_client=api_client)


@pytest.fixture
async def account_service_account_api() -> account_service.AccountApi:
    configuration = account_service.Configuration(host=v.get("service.account_service_account_api"))
    api_client = account_service.ApiClient(configuration=configuration)
    return account_service.AccountApi(api_client=api_client)


@pytest.fixture
async def users_service_user_api() -> users_service.UserApi:
    configuration = users_service.Configuration(host=v.get("service.users_service_user_api"))
    api_client = users_service.ApiClient(configuration=configuration)
    return users_service.UserApi(api_client=api_client)


@pytest.fixture
async def auth_service_auth_api() -> auth_service.AuthApi:
    configuration = auth_service.Configuration(host=v.get("service.auth_service_auth_api"))
    api_client = auth_service.ApiClient(configuration=configuration)
    return auth_service.AuthApi(api_client=api_client)


@pytest.fixture
async def register_service_account_api() -> register_service.AccountApi:
    configuration = register_service.Configuration(host=v.get("service.register_service_account_api"))
    api_client = register_service.ApiClient(configuration=configuration)
    return register_service.AccountApi(api_client=api_client)
