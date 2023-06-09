from pydantic import BaseModel, Field
from typing import Optional

class Attribute(BaseModel):
    name: str
    value: int

class Bid(BaseModel):
    auction_id: str
    bidder: str
    profile_id: str
    amount: int
    timestamp: int

class AuctionData(BaseModel):
    uuid: str
    auctioneer: str
    profile_id: str
    start_unix: int
    end_unix: int
    item_name: str
    item_id: str
    item_lore_raw: str
    rarity: str
    price: int
    attributes: list[Attribute] = None    # make it pydantic compatible
    claimed: bool
    bin: bool
    highest_bid: int
    #bids: list[Bid] = None  # make it pydantic compatible

class LowestBinData(BaseModel):
    item_name: str
    data: AuctionData

class AuctionResponse(BaseModel):
    success: bool
    last_update: int
    data: Optional[AuctionData] = Field(...)

class MultipleAuctionResponse(BaseModel):
    success: bool
    last_update: int
    data: list[AuctionData] = None

class LowestBinResponse(BaseModel):
    success: bool
    last_update: int
    data: list[LowestBinData]

class EmptyResponse(BaseModel):
    success: bool
    last_update: int
    data: list[None] = []