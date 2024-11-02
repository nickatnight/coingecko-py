from unittest.mock import MagicMock

from coingecko_py.api.categories import CategoriesClient
from coingecko_py.utils import RequestsClient

from ..fixture_data import CoinGeckoAPIFixtureData


def test_categories_list_happy(
    mock_requests_get: MagicMock, mock_http_client: RequestsClient
) -> None:
    # Arrange
    mock_requests_get.return_value = MagicMock(
        json=lambda: CoinGeckoAPIFixtureData.categories_response()
    )

    # Act
    client = CategoriesClient(http=mock_http_client)

    # Assert
    assert client.categories_list() == CoinGeckoAPIFixtureData.categories_response()


def test_categories_list_with_market_data_happy(
    mock_requests_get: MagicMock, mock_http_client: RequestsClient
) -> None:
    # Arrange
    mock_requests_get.return_value = MagicMock(
        json=lambda: CoinGeckoAPIFixtureData.categories_with_market_data_response()
    )

    # Act
    client = CategoriesClient(http=mock_http_client)

    # Assert
    assert (
        client.categories_list_with_market_data()
        == CoinGeckoAPIFixtureData.categories_with_market_data_response()
    )
