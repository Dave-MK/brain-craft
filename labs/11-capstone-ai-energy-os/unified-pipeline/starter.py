"""
Lab: Unified Pipeline
Lesson: capstone-system-integration

Wire cross-mission components into one system. The planted bug this lab
targets: the forecaster outputs kW, the RL agent was trained on MW --
pass the number straight through and every downstream decision is wrong
by a factor of 1000, silently.
"""


class AIEnergyOS:
    """Thin orchestration layer over already-built components.

    digital_twin.get_features(state) -> feature dict
    forecaster.predict(features)     -> demand forecast in KILOWATTS
    rl_agent.choose_action(state)    -> action string; expects the state's
                                        "forecast_mw" key in MEGAWATTS
    router.check_route(action)       -> {"route_ok": bool, ...}
    """

    def __init__(self, digital_twin, forecaster, rl_agent, router):
        self.digital_twin = digital_twin
        self.forecaster = forecaster
        self.rl_agent = rl_agent
        self.router = router

    def recommend_battery_action(self, current_state):
        """Full pipeline: features -> forecast (kW) -> agent (MW!) -> action.

        Return {"action": <agent's choice>, "forecast_mw": <converted forecast>}.
        The unit conversion at the forecaster->agent boundary is YOUR job --
        neither component does it for you.
        """
        # TODO: get features, predict (result is kW), convert to MW,
        #       call the agent with {**current_state, "forecast_mw": ...}
        raise NotImplementedError("recommend_battery_action is not implemented yet")

    def recommend_with_routing(self, current_state):
        """Same as above, but also run the router's check on the chosen
        action. Return {"action": ..., "forecast_mw": ..., "route_ok": bool}."""
        # TODO: reuse recommend_battery_action, then router.check_route
        raise NotImplementedError("recommend_with_routing is not implemented yet")
