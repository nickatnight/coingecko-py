from unittest.mock import MagicMock

from coingecko_py.api.simple import SimpleClient
from coingecko_py.utils import RequestsClient

from ..fixture_data import CoinGeckoAPIFixtureData


def test_simple_price_api_expected_response(
    mock_requests_get: MagicMock, mock_http_client: RequestsClient
) -> None:
    # Arrange
    data = CoinGeckoAPIFixtureData.simple_price_api_response()
    mock_requests_get.return_value = MagicMock(json=lambda: data)

    # Act
    client = SimpleClient(http=mock_http_client)

    # Assert
    assert (
        client.coin_price_by_id(
            request={"params": {"ids": "bitcoin", "vs_currencies": "usd"}}
        )
        == data
    )


def test_simple_token_price_api_expected_response(
    mock_requests_get: MagicMock, mock_http_client: RequestsClient
) -> None:
    # Arrange
    data = CoinGeckoAPIFixtureData.simple_token_price_api_response()
    mock_requests_get.return_value = MagicMock(json=lambda: data)

    # Act
    client = SimpleClient(http=mock_http_client)

    # Assert
    assert (
        client.coin_price_by_token(
            asset_id="ethereum",
            request={
                "params": {
                    "contract_addresses": "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599",
                    "vs_currencies": "usd",
                }
            },
        )
        == data
    )


def test_simple_supported_vs_currencies_api_expected_response(
    mock_requests_get: MagicMock, mock_http_client: RequestsClient
) -> None:
    # Arrange
    data: list = []
    mock_requests_get.return_value = MagicMock(json=lambda: [])

    # Act
    client = SimpleClient(http=mock_http_client)

    # Assert
    assert client.supported_vs_currencies() == data
