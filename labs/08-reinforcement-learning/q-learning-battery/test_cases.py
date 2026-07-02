import random
import unittest

from battery_env import CHARGE, DISCHARGE, HOLD, N_ACTIONS, BatteryEnv

from starter import greedy_action, run_greedy_episode, train_q_learning


class TestGreedyAction(unittest.TestCase):
    def test_picks_the_argmax(self):
        q_table = {("s",): [0.1, 0.9, 0.3]}
        self.assertEqual(greedy_action(q_table, ("s",)), 1)


class TestTraining(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.env = BatteryEnv()
        cls.q_table = train_q_learning(cls.env, episodes=3000, alpha=0.1, gamma=0.9, epsilon=0.2, seed=0)

    def test_learns_to_charge_when_cheap_and_empty(self):
        self.assertEqual(greedy_action(self.q_table, (0, 0)), CHARGE)

    def test_learns_to_discharge_when_expensive_and_full(self):
        self.assertEqual(greedy_action(self.q_table, (1, 1)), DISCHARGE)

    def test_learns_not_to_sell_cheap(self):
        # at (0, 1) -- cheap phase, battery full -- holding to sell at 5
        # beats selling now at 1
        self.assertEqual(greedy_action(self.q_table, (0, 1)), HOLD)

    def test_greedy_policy_is_clearly_profitable(self):
        # The optimal policy earns exactly 24 per episode (buy at 1, sell
        # at 5, six cycles). Relational bound: well above random (~0).
        total = run_greedy_episode(self.env, self.q_table)
        self.assertGreater(total, 20.0)

    def test_greedy_policy_beats_a_random_policy(self):
        rng = random.Random(1)
        random_totals = []
        for _ in range(50):
            env = BatteryEnv()
            env.reset()
            total, done = 0.0, False
            while not done:
                _, reward, done = env.step(rng.randrange(N_ACTIONS))
                total += reward
            random_totals.append(total)
        random_avg = sum(random_totals) / len(random_totals)
        self.assertGreater(run_greedy_episode(self.env, self.q_table), random_avg)

    def test_training_is_reproducible_with_the_same_seed(self):
        q_a = train_q_learning(BatteryEnv(), episodes=500, seed=42)
        q_b = train_q_learning(BatteryEnv(), episodes=500, seed=42)
        for state in q_a:
            self.assertEqual(q_a[state], q_b[state], "same seed must produce identical Q-tables -- is all randomness coming from the seeded rng?")

    def test_exploration_actually_visits_multiple_actions(self):
        # With epsilon=1.0 (pure exploration) every action gets tried, so
        # nonzero Q-values should appear for every action somewhere -- a
        # zero-exploration bug would leave whole columns untouched.
        q_table = train_q_learning(BatteryEnv(), episodes=200, epsilon=1.0, seed=0)
        touched_actions = set()
        for values in q_table.values():
            for action, value in enumerate(values):
                if value != 0.0:
                    touched_actions.add(action)
        self.assertEqual(touched_actions, {0, 1, 2}, "with epsilon=1.0, all three actions should have been explored somewhere")


if __name__ == "__main__":
    unittest.main()
