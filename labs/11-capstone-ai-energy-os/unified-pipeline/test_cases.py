import unittest

from starter import AIEnergyOS


class StubTwin:
    def get_features(self, state):
        return {"hour": state["hour"]}


class StubForecaster:
    def predict(self, features):
        return 4821.0  # KILOWATTS


class RecordingAgent:
    def __init__(self):
        self.seen_state = None

    def choose_action(self, state):
        self.seen_state = state
        return "discharge"


class StubRouter:
    def __init__(self, ok=True):
        self.ok = ok
        self.checked_action = None

    def check_route(self, action):
        self.checked_action = action
        return {"route_ok": self.ok}


def make_system(router_ok=True):
    agent = RecordingAgent()
    router = StubRouter(ok=router_ok)
    system = AIEnergyOS(StubTwin(), StubForecaster(), agent, router)
    return system, agent, router


class TestRecommendBatteryAction(unittest.TestCase):
    def test_agent_receives_the_forecast_in_megawatts(self):
        # THE planted bug: 4821 kW passed straight through as if it were
        # MW. The agent must see 4.821, not 4821.
        system, agent, _ = make_system()
        system.recommend_battery_action({"hour": 9})
        self.assertAlmostEqual(agent.seen_state["forecast_mw"], 4.821)

    def test_returns_the_agents_action_and_the_converted_forecast(self):
        system, _, _ = make_system()
        result = system.recommend_battery_action({"hour": 9})
        self.assertEqual(result["action"], "discharge")
        self.assertAlmostEqual(result["forecast_mw"], 4.821)

    def test_original_state_keys_still_reach_the_agent(self):
        system, agent, _ = make_system()
        system.recommend_battery_action({"hour": 9})
        self.assertEqual(agent.seen_state["hour"], 9)


class TestRecommendWithRouting(unittest.TestCase):
    def test_router_checks_the_chosen_action(self):
        system, _, router = make_system()
        result = system.recommend_with_routing({"hour": 9})
        self.assertEqual(router.checked_action, "discharge")
        self.assertTrue(result["route_ok"])

    def test_routing_failure_is_surfaced_not_swallowed(self):
        system, _, _ = make_system(router_ok=False)
        result = system.recommend_with_routing({"hour": 9})
        self.assertFalse(result["route_ok"])


if __name__ == "__main__":
    unittest.main()
