import pytest

from clients.http import mail_service


@pytest.mark.skip("Блочит другие тесты так как удаляет все письма")
async def test_delete_mail_messages(
    mail_service_mail_api: mail_service.MailApi,
) -> None:
    await mail_service_mail_api.delete_messages_mail_messages_delete()
    response = await mail_service_mail_api.get_messages_mail_messages_get(limit=50)
    if response.items is not None:
        assert len(response.items) == 0
