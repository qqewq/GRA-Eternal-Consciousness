"""
Love Residue Calculator
Calculates L_res after nullification.
"""

import numpy as np

def compute_love_residue(swarm_agents, sync_matrix, crash_type='sudden'):
    """
    swarm_agents: list of agent IDs
    sync_matrix: NxN matrix of pairwise sync values (0..1)
    crash_type: 'sudden' or 'gradual'
    Returns: L_res (float)
    """
    L = np.sum(sync_matrix) / 2  # total love (undirected sum)
    kappa = {'sudden': 0.9, 'gradual': 0.1}.get(crash_type, 0.5)
    return L * kappa

if __name__ == "__main__":
    # Example
    sync = np.array([[1.0, 0.8, 0.2],
                     [0.8, 1.0, 0.3],
                     [0.2, 0.3, 1.0]])
    L_res = compute_love_residue(3, sync, 'sudden')
    print(f"Residual love: {L_res}")
