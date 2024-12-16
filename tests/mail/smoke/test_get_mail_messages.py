from clients.http import mail_service


async def test_get_messages(
    mail_service_mail_api: mail_service.MailApi,
) -> None:
    await mail_service_mail_api.get_messages_mail_messages_get(limit=50)
