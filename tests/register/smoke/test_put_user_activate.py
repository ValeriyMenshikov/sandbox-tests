import orjson

from clients.http import mail_service, register_service
from tests.conftest import User


async def test_put_user_activate(
    register_service_account_api: register_service.AccountApi,
    mail_service_mail_api: mail_service.MailApi,
    prepare_user_data: User,
) -> None:
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

    assert message_response
