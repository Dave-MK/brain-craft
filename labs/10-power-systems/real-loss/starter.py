"""
Lab: Real Loss
Lesson: power-generation-transmission-distribution

Compute physically grounded transmission loss. The planted bug this lab
targets: plugging power directly into the resistive-loss formula
instead of first converting to current.
"""


def transmission_loss_kw(power_kw, voltage_kv, resistance_ohms):
    """Resistive line loss for delivering power_kw at voltage_kv over a
    line with resistance_ohms.

    Physics: current I = P / V (with P in watts and V in volts), and
    loss = I^2 * R (in watts). Convert the result back to kW.
    """
    # TODO: convert kW->W and kV->V, compute I, then I^2 * R, then W->kW
    raise NotImplementedError("transmission_loss_kw is not implemented yet")


def loss_percent(power_kw, voltage_kv, resistance_ohms):
    """Loss as a percentage of the power being delivered."""
    # TODO: transmission_loss_kw / power_kw * 100
    raise NotImplementedError("loss_percent is not implemented yet")


if __name__ == "__main__":
    print(transmission_loss_kw(5000, 11, 0.5))
    print(transmission_loss_kw(5000, 400, 0.5))
