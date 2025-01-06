# from kafka import KafkaConsumer
#
# consumer = KafkaConsumer(
#     "register-events",
#     bootstrap_servers="5.63.153.31:19092",
#     group_id="test_group_1",
#     auto_offset_reset="earliest",
# )
# for message in consumer:
#     print(f"Получено сообщение: {message}")
#     # print(f"Получено сообщение: {message.value.decode('utf-8')}")
import asyncio
import json

from aiokafka import AIOKafkaConsumer


async def main():
    kafka = AIOKafkaConsumer(
        "register-events",
        bootstrap_servers=["5.63.153.31:9092"],  # Убедитесь, что это правильный адрес
        value_deserializer=lambda message: json.loads(message.decode("utf-8")),
    )
    try:
        await kafka.start()
        async for message in kafka:
            print(f"Получено сообщение: {message}")
    finally:
        await kafka.stop()


asyncio.run(main())
