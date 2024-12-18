import json
from contextlib import contextmanager
from typing import Any, Generator, Optional

import requests


@contextmanager
def check_status_code_http(
    exception: type[Exception],
    expected_status_code: requests.codes = requests.codes.OK,
    expected_message: Optional[str] = "",
) -> Generator[Any, None, None]:
    try:
        yield
        if expected_status_code != requests.codes.OK:
            raise AssertionError(f"Ожидаемый статус код должен быть равен {expected_status_code}")
        if expected_message:
            raise AssertionError(f"Должно быть получено сообщение '{expected_message}', но запрос прошел успешно!")
    except exception as e:
        assert e.status == expected_status_code, f"Ожидаемый статус код {expected_status_code}, получен {e.status}"  # type: ignore[attr-defined]
        error_message = json.loads(e.body)["detail"]  # type: ignore[attr-defined]
        assert error_message == expected_message, f"Ожидаемое сообщение {expected_message}, получено {error_message}"  # type: ignore[attr-defined]
