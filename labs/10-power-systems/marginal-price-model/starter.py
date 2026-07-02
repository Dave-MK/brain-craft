"""
Lab: Marginal Price Model
Lesson: power-energy-markets-pricing

The market clears at the MARGINAL bid -- the most expensive generator
actually needed -- not the average of dispatched bids. That distinction
is exactly the planted bug this lab targets.
"""


def marginal_price(supply_bids_sorted, demand_kw):
    """supply_bids_sorted: list of (bid_price, bid_quantity_kw), sorted
    cheapest first. Walk down the stack accumulating quantity until
    cumulative supply covers demand_kw; return THAT tier's bid_price.

    If demand exceeds the entire stack, return the most expensive tier's
    price (the market is short -- every generator is dispatched).
    """
    # TODO: accumulate quantities, return the marginal tier's price
    raise NotImplementedError("marginal_price is not implemented yet")


def price_curve(supply_bids_sorted, demand_levels):
    """Return [marginal_price(bids, d) for each d in demand_levels]."""
    # TODO: map marginal_price over the demand levels
    raise NotImplementedError("price_curve is not implemented yet")


if __name__ == "__main__":
    bids = [(0.02, 2000), (0.08, 1500), (0.15, 1000), (0.35, 800)]
    print(marginal_price(bids, 4200))
    print(price_curve(bids, [1000, 3000, 4200, 6000]))
