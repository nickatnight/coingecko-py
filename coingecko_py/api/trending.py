from typing import cast

from coingecko_py.utils import CoinGeckoApiUrls, IHttp


class TrendingClient:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def trending(self) -> dict:
        "Query trending search coins, nfts and categories on CoinGecko in the last 24 hours."
        response = self.http.send(path=CoinGeckoApiUrls.TRENDING)

        return cast(dict, response)
