"""
Lab: Controlled Experiment
Lesson: capstone-research-workspace

Run a baseline-vs-modified comparison that is actually controlled. The
planted bug: a comparison where MORE than the tested variable differs
between the two configs, silently confounding the result.
"""


def check_controlled(baseline_config, modified_config, tested_variable):
    """Return a list of problem strings (empty = the experiment is
    genuinely controlled):

      - tested_variable must actually DIFFER between the two configs
      - every OTHER shared key must be identical
      - the two configs must have the same set of keys
    """
    # TODO: collect problems per the three rules
    raise NotImplementedError("check_controlled is not implemented yet")


def run_experiment(hypothesis, baseline_config, modified_config, tested_variable, simulate_fn):
    """Refuse to run a confounded experiment: if check_controlled reports
    problems, return {"hypothesis": hypothesis, "error": <the problems list>}.

    Otherwise simulate both configs (simulate_fn(config) -> {"total_cost": ...,
    "total_emissions": ...}) and return:
      {"hypothesis": ..., "cost_change": modified - baseline,
       "emissions_change": modified - baseline}
    """
    # TODO: gate on check_controlled, then compute the two deltas
    raise NotImplementedError("run_experiment is not implemented yet")
