from collections import namedtuple
from datetime import datetime

import orjson
import pytest

from clients.http import auth_service, mail_service, register_service

pytest_plugins = ["clients.fixtures"]

User = namedtuple("User", ["login", "password", "email"])


@pytest.fixture
async def prepare_user_data() -> User:
    now = datetime.now()
    data = now.strftime("%d_%m_%Y_%H_%M_%S_%f")
    login = f"vmenshikov_{data}"
    password = "1234567890"
    email = f"{login}@mail.ru"
    user = User(login=login, password=password, email=email)
    return user


@pytest.fixture
async def registered_user(
    auth_service_auth_api: auth_service.AuthApi,
    register_service_account_api: register_service.AccountApi,
    mail_service_mail_api: mail_service.MailApi,
    prepare_user_data: User,
) -> User:
    email = prepare_user_data.email
    password = prepare_user_data.password
    login = prepare_user_data.login
    await register_service_account_api.register_user_register_post(
        registration=register_service.Registration(email=email, password=password, login=login)
    )
    message_response = await mail_service_mail_api.search_mail_search_get(
        limit=50, kind="containing", query=email, start=0
    )
    token = ""
    if isinstance(message_response.items, list):
        for item in message_response.items:
            body = item.content.body if item.content else ""
            if isinstance(body, str):
                token = orjson.loads(body)["ConfirmationLinkUrl"].split("/")[-1]

    await register_service_account_api.activate_user_activate_put(token=token)
    return prepare_user_data
