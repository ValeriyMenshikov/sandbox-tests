from checkers.http_checkers import check_status_code_http
from clients.http import account_service, auth_service, mail_service
from clients.http.account_service import ApiException
from tests.conftest import User


async def test_delete_account(
    auth_service_auth_api: auth_service.AuthApi,
    account_service_account_api: account_service.AccountApi,
    registered_user: User,
) -> None:
    password = registered_user.password
    login = registered_user.login
    email = registered_user.email
    response = await auth_service_auth_api.auth_auth_auth_post(
        login_credentials=auth_service.LoginCredentials(login=login, password=password)
    )
    auth_token = response.metadata["token"]  # type: ignore[index]
    await account_service_account_api.delete_account_account_delete(email=email, token=auth_token)


async def test_delete_account_after_confirmation(
    auth_service_auth_api: auth_service.AuthApi,
    account_service_account_api: account_service.AccountApi,
    mail_service_mail_api: mail_service.MailApi,
    registered_user: User,
) -> None:
    password = registered_user.password
    login = registered_user.login
    email = registered_user.email
    response = await auth_service_auth_api.auth_auth_auth_post(
        login_credentials=auth_service.LoginCredentials(login=login, password=password)
    )
    auth_token = response.metadata["token"]  # type: ignore[index]
    await account_service_account_api.delete_account_account_delete(email=email, token=auth_token)
    message_response = await mail_service_mail_api.search_mail_search_get(
        limit=50, kind="containing", query=email, start=0
    )
    delete_token = ""
    if isinstance(message_response.items, list):
        for item in message_response.items:
            body = item.content.body if item.content else ""
            try:
                delete_token = body.split()[13][:-1] if isinstance(body, str) else ""
            except IndexError:
                pass

    await account_service_account_api.confirmation_delete_account_account_confirmation_delete_delete(
        delete_token=delete_token, token=auth_token
    )
    with check_status_code_http(
        exception=ApiException, expected_status_code=401, expected_message="Authorization failed"
    ):
        await account_service_account_api.delete_account_account_delete(email=email, token=auth_token)
