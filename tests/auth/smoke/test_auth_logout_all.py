from clients.http import auth_service
from tests.conftest import User


async def test_delete_auth_logout_all(
    auth_service_auth_api: auth_service.AuthApi,
    registered_user: User,
) -> None:
    password = registered_user.password
    login = registered_user.login
    response = await auth_service_auth_api.auth_auth_auth_post(
        login_credentials=auth_service.LoginCredentials(login=login, password=password)
    )
    auth_token = response.metadata["token"]  # type: ignore[index]

    await auth_service_auth_api.logout_all_auth_logout_all_delete(token=auth_token)
