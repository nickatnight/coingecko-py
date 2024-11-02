from typing import Optional, cast

from coingecko_py.utils import CoinGeckoApiUrls, CoinGeckoRequestParams, IHttp


class AssetPlatformsClient:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def asset_platforms(self, request: Optional[CoinGeckoRequestParams] = None) -> list:
        "Query all the asset platforms on CoinGecko"
        data = request or {}
        response = self.http.send(path=CoinGeckoApiUrls.ASSET_PLATFORMS, **data)

        return cast(list, response)
