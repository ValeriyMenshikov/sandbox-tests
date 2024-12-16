from clients.http import account_service
from tests.conftest import User


async def test_put_account_change_email(
    account_service_account_api: account_service.AccountApi,
    registered_user: User,
) -> None:
    password = registered_user.password
    login = registered_user.login
    new_email = "1" + registered_user.email
    await account_service_account_api.change_email_account_change_email_put(
        change_email=account_service.ChangeEmail(login=login, password=password, email=new_email)
    )
