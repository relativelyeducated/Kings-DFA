import random
import numpy as np
import matplotlib.pyplot as plt

class Agent:
    def __init__(self, S, R, mutation_strategy='random', mu_base=0.02, alpha=10.0):
        self.S = S
        self.R = R
        self.mutation_strategy = mutation_strategy
        self.mu_base = mu_base
        self.alpha = alpha
        self.fitness = 0

    def calculate_tension(self):
        if self.S + self.R == 0: return 0
        return abs(self.S - self.R) / (self.S + self.R)

    def calculate_fitness(self, target_S, target_R):
        dist = np.sqrt((self.S - target_S)**2 + (self.R - target_R)**2)
        self.fitness = 1.0 / (1.0 + dist)
        return self.fitness

    def mutate(self):
        if self.mutation_strategy == 'tension':
            T = self.calculate_tension()
            # Stronger response to tension
            mu = self.mu_base * (1 + self.alpha * (T**2))
        else:
            mu = self.mu_base

        if random.random() < mu:
            self.S += np.random.normal(0, 0.2) # Increased mutation step
        if random.random() < mu:
            self.R += np.random.normal(0, 0.2)
        
        self.S = max(0.1, self.S)
        self.R = max(0.1, self.R)

def run_simulation_v2(strategy, generations=500, pop_size=1000):
    # Dynamic Environment
    target_S = 5.0
    target_R = 5.0
    
    population = [Agent(S=1.0, R=1.0, mutation_strategy=strategy) for _ in range(pop_size)]
    
    avg_fitness_history = []
    
    for gen in range(generations):
        # 1. Evaluate
        fitnesses = [agent.calculate_fitness(target_S, target_R) for agent in population]
        avg_fitness_history.append(np.mean(fitnesses))
        
        # 2. Selection (Weaker pressure: 63% survival = 1/e death rate)
        sorted_pop = [x for _, x in sorted(zip(fitnesses, population), key=lambda pair: pair[0], reverse=True)]
        survivors = sorted_pop[:int(pop_size * 0.63)] 
        
        # 3. Reproduction
        next_gen = []
        for _ in range(pop_size):
            parent = random.choice(survivors)
            child = Agent(parent.S, parent.R, strategy)
            child.mutate()
            next_gen.append(child)
        
        population = next_gen
        
        # 4. Volatile Environment (Oscillation + Shocks)
        # Continuous drift
        target_S += np.sin(gen / 10.0) * 0.2
        target_R += np.cos(gen / 10.0) * 0.2
        
        # Occasional Shocks
        if gen % 100 == 0:
            target_S += np.random.normal(0, 2.0)
            target_R += np.random.normal(0, 2.0)

    return avg_fitness_history

def plot_results_v2():
    print("Running Control (Random)...")
    control = run_simulation_v2('random')
    
    print("Running Experiment (Tension)...")
    tension = run_simulation_v2('tension')
    
    plt.figure(figsize=(10, 6))
    plt.plot(control, label='Control (Random)', color='gray', alpha=0.7)
    plt.plot(tension, label='Experiment (Tension)', color='blue', linewidth=2)
    
    plt.xlabel('Generation')
    plt.ylabel('Average Fitness')
    plt.title('Biology V2: Volatile Environment (Selection ~ 1/e)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    output_path = 'evidence/biology_simulation_v2.png'
    plt.savefig(output_path)
    print(f"Plot saved to {output_path}")
    
    # Calculate Tracking Improvement (Mean fitness over run)
    mean_control = np.mean(control)
    mean_tension = np.mean(tension)
    improvement = (mean_tension - mean_control) / mean_control * 100
    
    print(f"Tracking Improvement: {improvement:.2f}%")
    
    if improvement > 5.0:
        print("SUCCESS: Tension-Driven Mutation adapts better in volatile environment.")
    else:
        print("FAILURE: No significant advantage found.")

if __name__ == "__main__":
    plot_results_v2()
