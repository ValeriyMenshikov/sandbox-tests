from clients.http import account_service
from tests.conftest import User


async def test_post_account_reset_password(
    account_service_account_api: account_service.AccountApi,
    registered_user: User,
) -> None:
    login = registered_user.login
    email = registered_user.email
    await account_service_account_api.reset_password_account_reset_password_post(
        reset_password=account_service.ResetPassword(login=login, email=email)
    )
