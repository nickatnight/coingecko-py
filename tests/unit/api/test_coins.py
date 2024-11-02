from unittest.mock import MagicMock

from coingecko_py.api.coins import CoinsClient
from coingecko_py.utils import RequestsClient

from ..fixture_data import CoinGeckoAPIFixtureData


def test_simple_price_api_expected_response(
    mock_requests_get: MagicMock, mock_http_client: RequestsClient
) -> None:
    # Arrange
    data = CoinGeckoAPIFixtureData.coins_list_response()
    mock_requests_get.return_value = MagicMock(json=lambda: data)

    # Act
    client = CoinsClient(http=mock_http_client)

    # Assert
    assert client.coins_list(request={"params": {"include_platform": False}}) == data


def test_coins_markets_api_expected_response(
    mock_requests_get: MagicMock, mock_http_client: RequestsClient
) -> None:
    # Arrange
    data = CoinGeckoAPIFixtureData.coins_markets_response()
    mock_requests_get.return_value = MagicMock(json=lambda: data)

    # Act
    client = CoinsClient(http=mock_http_client)

    # Assert
    assert client.coins_markets(request={"params": {"vs_currency": "usd"}}) == data
