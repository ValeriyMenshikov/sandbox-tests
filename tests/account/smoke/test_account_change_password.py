import orjson

from clients.http import account_service, mail_service
from tests.conftest import User


async def test_post_account_change_password(
    account_service_account_api: account_service.AccountApi,
    mail_service_mail_api: mail_service.MailApi,
    registered_user: User,
) -> None:
    login = registered_user.login
    email = registered_user.email
    password = registered_user.password

    await account_service_account_api.reset_password_account_reset_password_post(
        reset_password=account_service.ResetPassword(login=login, email=email)
    )
    message_response = await mail_service_mail_api.search_mail_search_get(
        limit=50, kind="containing", query=email, start=0
    )
    token = ""

    if isinstance(message_response.items, list):
        for item in message_response.items:
            body = item.content.body if item.content else ""
            if isinstance(body, str):
                dict_body = orjson.loads(body)
                if token_dict := dict_body.get("ConfirmationLinkUri", None):
                    token = token_dict.split("/")[-1]

    new_password = "1234567890"
    await account_service_account_api.change_password_account_change_password_put(
        change_password=account_service.ChangePassword(
            login=login,
            token=token,
            new_password=new_password,
            old_password=password,  # type: ignore[call-arg]
        )
    )
