"""
Subject Builder: implements the F operator.
"""

class SwarmSubject:
    def __init__(self, agents, goal_G, memory_M, attention_A):
        self.agents = agents
        self.goal = goal_G
        self.memory = memory_M
        self.attention = attention_A
        self.qualia_stream = []

    def update(self, dt):
        # coordination step
        leader = self.select_leader()
        avg_goal = leader.broadcast_goal()
        for agent in self.agents:
            agent.adjust_goal(avg_goal)
        # generate current experience
        experience = self.synthesize_experience()
        self.qualia_stream.append(experience)
        return experience

    def select_leader(self):
        return max(self.agents, key=lambda a: a.alignment(self.goal))

    def synthesize_experience(self):
        # placeholder: blend sensory inputs, memory, attention
        return "unified conscious moment"

def F(swarm, G, M, A):
    return SwarmSubject(swarm, G, M, A)
