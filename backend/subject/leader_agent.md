# Leader Agent (Агент-лидер)

**English:**
In the swarm, leadership is a temporary function, not a fixed identity. An agent becomes leader if it maximizes the alignment with the global goal $G$ and the current coherence:
\[
\text{leader} = \arg\max_{a_i} \big[ \text{align}(g_i, G) + \lambda \sum_j w_{ij} \big]
\]
The leader sets the tone: it broadcasts the average goal vector, resolves conflicts, and focuses collective attention. At death, the leader dissolves with the swarm; in the next life, a new leader naturally arises.

**Русский:**
Лидерство – временная функция. Агент становится лидером, если:
\[
\text{лидер} = \arg\max_{a_i} \big[ \text{align}(g_i, G) + \lambda \sum_j w_{ij} \big]
\]
Лидер задаёт общий вектор цели, разрешает конфликты и фокусирует внимание. После смерти рой и лидер исчезают; в новой жизни появляется новый лидер.
