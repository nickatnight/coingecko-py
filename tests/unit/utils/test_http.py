from unittest.mock import MagicMock

import pytest
import requests

from coingecko_py.utils.exceptions import CoinGeckoRequestError
from coingecko_py.utils.http import RequestsClient


def test_client_coingecko_request_error(mocker: MagicMock) -> None:
    # Arrange
    mocker.patch(
        "coingecko_py.utils.http.requests.get",
        side_effect=requests.exceptions.HTTPError("Error"),
    )

    # Act
    client = RequestsClient()

    # Assert
    with pytest.raises(CoinGeckoRequestError):
        client.send("fakeurl")


def test_client_coingecko_other_error(mocker: MagicMock) -> None:
    # Arrange
    mocker.patch(
        "coingecko_py.utils.http.requests.get",
        side_effect=ValueError("Error"),
    )

    # Act
    client = RequestsClient()

    # Assert
    with pytest.raises(ValueError):
        client.send("fakeurl")
