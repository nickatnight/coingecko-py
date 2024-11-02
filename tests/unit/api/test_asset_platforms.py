from unittest.mock import MagicMock

from coingecko_py.api.asset_platforms import AssetPlatformsClient
from coingecko_py.utils import RequestsClient

from ..fixture_data import CoinGeckoAPIFixtureData


def test_asset_platforms_happy(
    mock_requests_get: MagicMock, mock_http_client: RequestsClient
) -> None:
    # Arrange
    mock_requests_get.return_value = MagicMock(
        json=lambda: CoinGeckoAPIFixtureData.asset_platforms_response()
    )

    # Act
    client = AssetPlatformsClient(http=mock_http_client)

    # Assert
    assert (
        client.asset_platforms() == CoinGeckoAPIFixtureData.asset_platforms_response()
    )
