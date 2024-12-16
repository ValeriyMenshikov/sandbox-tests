from clients.http import mail_service, register_service
from tests.conftest import User


async def test_get_message_message_id(
    register_service_account_api: register_service.AccountApi,
    mail_service_mail_api: mail_service.MailApi,
    prepare_user_data: User,
) -> None:
    email = prepare_user_data.email
    password = prepare_user_data.password
    login = prepare_user_data.login
    await register_service_account_api.register_user_register_post(
        registration=register_service.Registration(email=email, password=password, login=login)
    )

    message_response = await mail_service_mail_api.search_mail_search_get(
        limit=50, kind="containing", query=email, start=0
    )
    if isinstance(message_response.items, list):
        for item in message_response.items:
            message_id = item.id if item.id else ""
            response = await mail_service_mail_api.get_message_mail_message_message_id_get(message_id=message_id)
            assert response.id == message_id
