import unittest

import torch
import torch.optim as optim

from starter import PolicyNetwork, policy_gradient_loss


class TestPolicyNetwork(unittest.TestCase):
    def test_outputs_a_valid_probability_distribution(self):
        torch.manual_seed(0)
        policy = PolicyNetwork(state_size=2, n_actions=3)
        probs = policy(torch.tensor([0.5, 0.3]))
        self.assertEqual(tuple(probs.shape), (3,))
        self.assertAlmostEqual(probs.sum().item(), 1.0, places=5)
        self.assertTrue((probs >= 0).all().item())

    def test_batched_input_gives_batched_distributions(self):
        torch.manual_seed(0)
        policy = PolicyNetwork(state_size=2, n_actions=3)
        probs = policy(torch.randn(5, 2))
        self.assertEqual(tuple(probs.shape), (5, 3))
        sums = probs.sum(dim=-1)
        self.assertTrue(torch.allclose(sums, torch.ones(5), atol=1e-5))


class TestPolicyGradientLoss(unittest.TestCase):
    def test_hand_computed_value(self):
        log_probs = torch.tensor([-1.0, -2.0])
        rewards = torch.tensor([3.0, 1.0])
        # -((-1*3) + (-2*1)) / 2 = -(-5)/2 = 2.5
        self.assertAlmostEqual(policy_gradient_loss(log_probs, rewards).item(), 2.5)

    def test_zero_rewards_give_zero_loss(self):
        # The unweighted-loss bug: ignoring rewards would give a nonzero
        # loss here and wrongly reinforce unrewarded actions.
        log_probs = torch.tensor([-1.0, -2.0, -0.5])
        rewards = torch.zeros(3)
        self.assertAlmostEqual(policy_gradient_loss(log_probs, rewards).item(), 0.0)

    def test_loss_scales_linearly_with_reward(self):
        log_probs = torch.tensor([-1.0, -2.0])
        small = policy_gradient_loss(log_probs, torch.tensor([1.0, 1.0])).item()
        double = policy_gradient_loss(log_probs, torch.tensor([2.0, 2.0])).item()
        self.assertAlmostEqual(double, 2 * small)

    def test_one_update_step_increases_probability_of_the_rewarded_action(self):
        torch.manual_seed(0)
        policy = PolicyNetwork(state_size=2, n_actions=3)
        optimizer = optim.SGD(policy.parameters(), lr=0.5)
        state = torch.tensor([0.5, 0.3])
        rewarded_action = 2

        prob_before = policy(state)[rewarded_action].item()

        probs = policy(state)
        log_prob = torch.log(probs[rewarded_action])
        loss = policy_gradient_loss(log_prob.unsqueeze(0), torch.tensor([1.0]))
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        prob_after = policy(state)[rewarded_action].item()
        self.assertGreater(prob_after, prob_before, "a positively-rewarded action's probability should increase after the update")


if __name__ == "__main__":
    unittest.main()
