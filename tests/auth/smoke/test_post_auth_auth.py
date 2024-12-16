from clients.http import auth_service
from tests.conftest import User


async def test_post_auth_auth(
    auth_service_auth_api: auth_service.AuthApi,
    registered_user: User,
) -> None:
    password = registered_user.password
    login = registered_user.login
    await auth_service_auth_api.auth_auth_auth_post(
        login_credentials=auth_service.LoginCredentials(login=login, password=password)
    )
