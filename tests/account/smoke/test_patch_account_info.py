from clients.http import account_service, auth_service
from tests.conftest import User


async def test_patch_account_info(
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
    await account_service_account_api.update_info_account_info_patch(
        token=auth_token,
        user_schema=account_service.UserSchema(
            name="Vladimir",
            location="Russia",
            icq="1234567890",
            skype="vmenshikov",
            info="",
            profile_picture_url="picture_url",
            medium_profile_picture_url="medium_picture_url",
            small_profile_picture_url="small_picture_url",
        ),
    )
