from clients.http import account_service, auth_service
from tests.conftest import User


async def test_get_account_info(
    auth_service_auth_api: auth_service.AuthApi,
    account_service_account_api: account_service.AccountApi,
    registered_user: User,
) -> None:
    password = registered_user.password
    login = registered_user.login
    response = await auth_service_auth_api.auth_auth_auth_post(
        login_credentials=auth_service.LoginCredentials(login=login, password=password)
    )
    auth_token = response.metadata["token"]  # type: ignore[index]
    await account_service_account_api.get_info_account_info_get(token=auth_token)
