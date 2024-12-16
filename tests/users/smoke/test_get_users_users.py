from clients.http import users_service


async def test_get_users_users(
    users_service_user_api: users_service.UserApi,
) -> None:
    await users_service_user_api.get_users_users_users_get(limit=50)
