import random
import numpy as np
import matplotlib.pyplot as plt

class Agent:
    def __init__(self, S, R, mutation_strategy='random', mu_base=0.01, alpha=5.0):
        self.S = S  # Structure
        self.R = R  # Relation
        self.mutation_strategy = mutation_strategy
        self.mu_base = mu_base
        self.alpha = alpha
        self.fitness = 0
        self.surplus = 0

    def calculate_tension(self):
        # Tension T = |S - R| / (S + R)
        if self.S + self.R == 0: return 0
        return abs(self.S - self.R) / (self.S + self.R)

    def calculate_fitness(self, target_S, target_R):
        # Simple distance-based fitness (closer is better)
        dist = np.sqrt((self.S - target_S)**2 + (self.R - target_R)**2)
        # Fitness = 1 / (1 + dist)
        self.fitness = 1.0 / (1.0 + dist)
        return self.fitness

    def mutate(self):
        # Determine mutation rate
        if self.mutation_strategy == 'tension':
            T = self.calculate_tension()
            # Mutation rate scales with Tension squared
            mu = self.mu_base * (1 + self.alpha * (T**2))
        else:
            # Constant mutation rate (Control)
            mu = self.mu_base

        # Apply mutation
        if random.random() < mu:
            self.S += np.random.normal(0, 0.1)
        if random.random() < mu:
            self.R += np.random.normal(0, 0.1)
        
        # Keep values positive
        self.S = max(0.1, self.S)
        self.R = max(0.1, self.R)

def run_simulation(strategy, generations=500, pop_size=1000):
    # Target Environment (Moving Target to force adaptation)
    target_S = 5.0
    target_R = 5.0
    
    population = [Agent(S=1.0, R=1.0, mutation_strategy=strategy) for _ in range(pop_size)]
    
    avg_fitness_history = []
    surplus_history = []
    
    for gen in range(generations):
        # 1. Evaluate Fitness
        fitnesses = [agent.calculate_fitness(target_S, target_R) for agent in population]
        avg_fit = np.mean(fitnesses)
        avg_fitness_history.append(avg_fit)
        
        # 2. Selection (Survival of the fittest)
        # Sort by fitness
        sorted_pop = [x for _, x in sorted(zip(fitnesses, population), key=lambda pair: pair[0], reverse=True)]
        # Keep top 50%
        survivors = sorted_pop[:pop_size//2]
        
        # 3. Reproduction & Mutation
        next_gen = []
        for _ in range(pop_size):
            parent = random.choice(survivors)
            child = Agent(parent.S, parent.R, strategy)
            child.mutate()
            next_gen.append(child)
        
        population = next_gen
        
        # Move target slightly every 50 generations to simulate environmental shift
        if gen % 50 == 0:
            target_S += np.random.normal(0, 0.5)
            target_R += np.random.normal(0, 0.5)

    return avg_fitness_history

def plot_results():
    print("Running Control Simulation (Random Mutation)...")
    control_fitness = run_simulation('random')
    
    print("Running Experimental Simulation (Tension-Driven Mutation)...")
    tension_fitness = run_simulation('tension')
    
    plt.figure(figsize=(10, 6))
    plt.plot(control_fitness, label='Control (Random Mutation)', color='gray', linestyle='--')
    plt.plot(tension_fitness, label='Experiment (Tension-Driven)', color='blue', linewidth=2)
    
    plt.xlabel('Generation')
    plt.ylabel('Average Fitness')
    plt.title('Adaptation Speed: Tension-Driven vs Random Mutation')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    output_path = 'evidence/biology_simulation_results.png'
    plt.savefig(output_path)
    print(f"Simulation complete. Plot saved to {output_path}")
    
    # Calculate improvement
    final_control = np.mean(control_fitness[-50:])
    final_tension = np.mean(tension_fitness[-50:])
    improvement = (final_tension - final_control) / final_control * 100
    print(f"Final Fitness Improvement: {improvement:.2f}%")

if __name__ == "__main__":
    plot_results()
