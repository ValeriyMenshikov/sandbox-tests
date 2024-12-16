from clients.http import users_service


async def test_get_users_users_search(
    users_service_user_api: users_service.UserApi,
) -> None:
    await users_service_user_api.search_users_users_users_search_get(limit=50, search="test")
