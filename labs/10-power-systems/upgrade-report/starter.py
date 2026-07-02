"""
Lab: Upgrade Report
Lesson: power-digital-twin-fidelity (boss battle)

Wire the Mission 6 fidelity upgrades into the Digital Twin so the
toggles actually propagate. The planted bug this lab targets: a toggle
that is implemented but never connected, so "upgrading" the twin
silently changes nothing downstream.
"""


def transmission_loss_kw(power_kw, voltage_kv, resistance_ohms):
    """Realistic resistive loss (same physics as the real-loss lab)."""
    current_amps = (power_kw * 1000) / (voltage_kv * 1000)
    return ((current_amps ** 2) * resistance_ohms) / 1000


def marginal_price(supply_bids_sorted, demand_kw):
    """Marginal clearing price (same logic as the marginal-price lab)."""
    cumulative = 0
    for bid_price, bid_quantity_kw in supply_bids_sorted:
        cumulative += bid_quantity_kw
        if cumulative >= demand_kw:
            return bid_price
    return supply_bids_sorted[-1][0]


class DigitalTwinV2:
    """The fidelity-upgraded twin. Both helper functions above are
    provided -- your job is to WIRE them in so the toggles actually
    change behavior."""

    def __init__(self, supply_bids, flat_price=0.10,
                 use_realistic_loss=True, use_marginal_pricing=True):
        self.supply_bids = supply_bids
        self.flat_price = flat_price
        self.use_realistic_loss = use_realistic_loss
        self.use_marginal_pricing = use_marginal_pricing

    def edge_loss(self, edge, power_flow_kw):
        """edge: {"voltage_kv": ..., "resistance_ohms": ..., "flat_loss_percent": ...}

        Realistic mode: transmission_loss_kw with the edge's physical values.
        Flat mode: power_flow_kw * edge["flat_loss_percent"].
        """
        # TODO: branch on self.use_realistic_loss -- and actually USE it
        raise NotImplementedError("edge_loss is not implemented yet")

    def current_price(self, demand_kw, renewable_output_kw):
        """Marginal mode: marginal_price against the NET demand
        (demand minus renewable output, floored at 0).
        Flat mode: self.flat_price regardless of conditions.
        """
        # TODO: branch on self.use_marginal_pricing -- and actually USE it
        raise NotImplementedError("current_price is not implemented yet")


if __name__ == "__main__":
    twin = DigitalTwinV2(supply_bids=[(0.02, 2000), (0.35, 800)])
    edge = {"voltage_kv": 11, "resistance_ohms": 0.5, "flat_loss_percent": 0.02}
    print(twin.edge_loss(edge, 5000))
    print(twin.current_price(demand_kw=2500, renewable_output_kw=1000))
