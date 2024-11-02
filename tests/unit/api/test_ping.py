from unittest.mock import MagicMock

from coingecko_py.api.ping import PingClient
from coingecko_py.utils import RequestsClient

from ..fixture_data import CoinGeckoAPIFixtureData


def test_ping_api_happy(
    mock_requests_get: MagicMock, mock_http_client: RequestsClient
) -> None:
    # Arrange
    mock_requests_get.return_value = MagicMock(
        json=lambda: CoinGeckoAPIFixtureData.ping_response()
    )

    # Act
    client = PingClient(http=mock_http_client)

    # Assert
    assert client.ping() == CoinGeckoAPIFixtureData.ping_response()
