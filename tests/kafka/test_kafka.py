import queue
import threading
import time

import pytest
from kafka import KafkaConsumer

stop_event = threading.Event()  # Событие для остановки консумера


@pytest.fixture(scope="function")
def kafka_message_queue():
    # Создаём очередь с максимальным размером 1
    message_queue = queue.Queue(maxsize=1)

    def kafka_consumer():
        consumer = KafkaConsumer(
            "register-events",
            bootstrap_servers=["5.63.153.31:9092"],
            group_id="test_group",
            auto_offset_reset="latest",
        )
        while not stop_event.is_set():
            print("Прослушиваем очередь...")
            m = consumer.poll(timeout_ms=1000)
            print(f"Получено сообщение: {m}")
            time.sleep(1)
            # for message in consumer:
            #     print(f"Получено сообщение: {message.value.decode('utf-8')}")
            #     try:
            #         # Пытаемся положить сообщение в очередь (блокируется, если очередь заполнена)
            #         message_queue.put(message.value.decode("utf-8"), timeout=1)
            #     except queue.Full:
            #         print("Очередь заполнена, ожидаем...")
            #     if stop_event.is_set():
            #         print("Остановка консумера")
            #         break
            #     time.sleep(1)

        consumer.close()

    # Запускаем консумер в отдельном потоке
    consumer_thread = threading.Thread(target=kafka_consumer, daemon=True)
    consumer_thread.start()

    # Передаём очередь в тесты
    yield message_queue

    # Останавливаем консумер после завершения теста
    stop_event.set()
    consumer_thread.join()


# Пример теста
def test_kafka_consumer_logic(kafka_message_queue):
    for _ in range(5):  # Пример: Проверяем 5 сообщений
        # Получаем сообщение из очереди
        if kafka_message_queue.empty():
            print("Очередь пуста, ожидаем...")
            time.sleep(2)
            continue

        message = kafka_message_queue.get(timeout=10)
        print(f"Получено сообщение: {message}")
        if "strin1123" in str(message):
            stop_event.set()
            break
    else:
        stop_event.set()
        raise AssertionError("Тест не прошёл")


# def test_kafka_consumer_logic():
#     consumer = KafkaConsumer(
#         "register-events",
#         bootstrap_servers=["5.63.153.31:9092"],
#         group_id="test_group",
#         auto_offset_reset="earliest",
#     )
#     for message in consumer:
#         print(f"Получено сообщение: {message.value.decode('utf-8')}")
