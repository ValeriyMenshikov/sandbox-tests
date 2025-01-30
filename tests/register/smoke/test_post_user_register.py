from clients.http import register_service
from tests.conftest import User
import pytest


async def test_post_user_register(
    register_service_account_api: register_service.AccountApi, prepare_user_data: User
) -> None:
    response = await register_service_account_api.register_user_register_post(
        registration=register_service.Registration(
            email=prepare_user_data.email, password=prepare_user_data.password, login=prepare_user_data.login
        )
    )
    assert response


@pytest.mark.skip("Надо попроавить в сервисе")
async def test_post_user_register_twice(
    register_service_account_api: register_service.AccountApi, prepare_user_data: User
) -> None:
    await register_service_account_api.register_user_register_post(
        registration=register_service.Registration(
            email=prepare_user_data.email, password=prepare_user_data.password, login=prepare_user_data.login
        )
    )
    response = await register_service_account_api.register_user_register_post(
        registration=register_service.Registration(
            email=prepare_user_data.email, password=prepare_user_data.password, login=prepare_user_data.login
        )
    )
    assert response
