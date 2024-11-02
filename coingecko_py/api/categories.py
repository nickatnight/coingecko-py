from typing import Optional, cast

from coingecko_py.utils import CoinGeckoApiUrls, CoinGeckoRequestParams, IHttp


class CategoriesClient:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def categories_list(self) -> list:
        "Query all the coins categories on CoinGecko."
        response = self.http.send(path=CoinGeckoApiUrls.CATEGORIES)

        return cast(list, response)

    def categories_list_with_market_data(
        self, *, request: Optional[CoinGeckoRequestParams] = None
    ) -> list:
        "Query all the coins categories with market data (market cap, volume, etc.) on CoinGecko."
        data = request or {}
        response = self.http.send(path=CoinGeckoApiUrls.CATEGORIES_MARKETS, **data)

        return cast(list, response)
