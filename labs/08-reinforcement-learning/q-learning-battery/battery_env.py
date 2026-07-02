"""A tiny, fully deterministic battery environment for the Q-learning lab.

Price alternates every step: cheap (1), then expensive (5). The state is
(phase, soc):
  phase: position in the price cycle, 0-1 (prices [1, 5])
  soc:   battery charge level, 0-1 (capacity of one unit)

Actions: 0 = charge, 1 = hold, 2 = discharge.
  charge at soc<1:    soc+1, reward = -price  (buying energy)
  discharge at soc>0: soc-1, reward = +price  (selling energy)
  invalid charge/discharge (full/empty) acts as hold: reward 0.

The optimal policy is unique and strongly separated in value:
  (0, 0) -> charge     (buy at 1)
  (0, 1) -> hold       (wait to sell at 5, not at 1)
  (1, 0) -> hold       (never buy at 5)
  (1, 1) -> discharge  (sell at 5)
Profit: 4 per two-step cycle, 24 over the 12-step episode. Every
transition is deterministic, so all randomness in training comes from
exploration.

(Design note: an earlier version of this env used a 4-phase cycle with
capacity 2; Q-learning at the lab's default hyperparameters reliably
converged to a locally-stable one-unit strategy instead of the true
optimum, making exact-policy assertions flaky. This 2-phase version has
a unique optimum with a wide value gap, so tests can assert the exact
learned policy.)
"""

PRICES = [1, 5]
EPISODE_LENGTH = 12  # six full price cycles
N_ACTIONS = 3
CHARGE, HOLD, DISCHARGE = 0, 1, 2


class BatteryEnv:
    def __init__(self):
        self._t = 0
        self._soc = 0

    def reset(self):
        self._t = 0
        self._soc = 0
        return self._state()

    def _state(self):
        return (self._t % 2, self._soc)

    def step(self, action):
        price = PRICES[self._t % 2]
        reward = 0.0
        if action == CHARGE and self._soc < 1:
            self._soc += 1
            reward = -float(price)
        elif action == DISCHARGE and self._soc > 0:
            self._soc -= 1
            reward = float(price)
        self._t += 1
        done = self._t >= EPISODE_LENGTH
        return self._state(), reward, done

    @staticmethod
    def all_states():
        return [(phase, soc) for phase in range(2) for soc in range(2)]
