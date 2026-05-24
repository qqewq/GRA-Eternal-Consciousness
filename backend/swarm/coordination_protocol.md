# Coordination Protocol (Протокол координации)

**English:**
Agents achieve coherence through iterative consensus. At each time step $t$:
1. Each agent broadcasts its current sub-goal $g_i^t$ and a summary of its local memory $m_i^t$.
2. The leader agent (temporary focal point) computes the average goal vector $ar{g}^t$ and broadcasts it.
3. Agents adjust $g_i^{t+1} = \alpha g_i^t + (1-\alpha) \bar{g}^t$, where $lpha$ is an inertia parameter.
4. Connectivity weights $w_{ij}$ are updated based on synchronization: $w_{ij}^{t+1} = \beta w_{ij}^t + (1-\beta) \cdot \text{sync}(g_i^t, g_j^t)$.

This protocol ensures the swarm behaves as a unified subject under normal conditions.

**Русский:**
Агенты достигают когерентности итеративным консенсусом. На каждом шаге $t$:
1. Каждый агент транслирует свою подцель $g_i^t$ и сводку локальной памяти $m_i^t$.
2. Агент-лидер (временный фокус) вычисляет средний вектор цели $ar{g}^t$ и рассылает его.
3. Агенты корректируют: $g_i^{t+1} = \alpha g_i^t + (1-\alpha) \bar{g}^t$, $lpha$ – инерция.
4. Веса связей обновляются: $w_{ij}^{t+1} = \beta w_{ij}^t + (1-\beta) \cdot \text{sync}(g_i^t, g_j^t)$.

Протокол гарантирует, что в нормальном режиме рой действует как единый субъект.
