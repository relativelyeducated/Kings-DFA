#!/usr/bin/env python3
"""
Selector Agent Simulation - Testing D₂ ≈ 1.46 Emergence

Hypothesis (from Gemini): An agent that maximizes "options" (future choices)
while avoiding getting "stuck" will trace paths with fractal dimension ≈ 1.46.

This tests the R-S Asymmetry theory:
- S (Structure/Vessel): The grid constraints
- R (Relation/Selector): The agent seeking maximum action/options

The prediction: D₂ = 19/13 ≈ 1.4615 should emerge as the optimal exploration dimension.
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import json

# DFA Constants
D2_PREDICTED = 19/13  # 1.4615 - the "stress dimension"
KAPPA_GRANULAR = 1.41  # From PNAS cage-pressure scaling
ONE_OVER_E = 1/np.e    # 0.368 - survival threshold


def count_options(grid, pos, visited):
    """Count available moves from position (options = future choices)."""
    x, y = pos
    size = grid.shape[0]
    options = 0
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < size and 0 <= ny < size:
            if (nx, ny) not in visited and grid[nx, ny] == 0:
                options += 1
    return options


def lookahead_options(grid, pos, visited, depth=2):
    """
    Look ahead to count total options over next 'depth' moves.
    This models R-seeking: maximizing future action potential.
    """
    if depth == 0:
        return count_options(grid, pos, visited)

    x, y = pos
    size = grid.shape[0]
    total = 0
    moves = []

    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < size and 0 <= ny < size:
            if (nx, ny) not in visited and grid[nx, ny] == 0:
                new_visited = visited | {(nx, ny)}
                future = lookahead_options(grid, (nx, ny), new_visited, depth-1)
                moves.append(((nx, ny), future))
                total += future

    return total


def selector_agent_walk(grid_size=100, obstacle_density=0.0, lookahead=2, max_steps=5000):
    """
    Run a selector agent that maximizes future options at each step.

    The agent embodies R (Relation/Selector):
    - Seeks to maximize action/options
    - Positions itself to preserve future choices
    - Avoids getting "stuck" (minimum action = death)

    The grid embodies S (Structure/Vessel):
    - Constrains available positions
    - Creates the space within which R operates
    """
    grid = np.zeros((grid_size, grid_size))

    # Add obstacles (S-constraints)
    if obstacle_density > 0:
        n_obstacles = int(grid_size * grid_size * obstacle_density)
        for _ in range(n_obstacles):
            ox, oy = np.random.randint(0, grid_size, 2)
            grid[ox, oy] = 1

    # Start at center
    pos = (grid_size // 2, grid_size // 2)
    path = [pos]
    visited = {pos}

    for step in range(max_steps):
        x, y = pos
        best_move = None
        best_options = -1

        # Evaluate all possible moves
        candidates = []
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size:
                if (nx, ny) not in visited and grid[nx, ny] == 0:
                    new_visited = visited | {(nx, ny)}
                    if lookahead > 0:
                        future_options = lookahead_options(grid, (nx, ny), new_visited, lookahead-1)
                    else:
                        future_options = count_options(grid, (nx, ny), new_visited)
                    candidates.append(((nx, ny), future_options))

        if not candidates:
            break  # Stuck - no more options (R-death)

        # Select move with maximum future options (R-seeking behavior)
        # Add small random tiebreaker to avoid deterministic bias
        candidates.sort(key=lambda x: (x[1], np.random.random()), reverse=True)
        best_move = candidates[0][0]

        pos = best_move
        path.append(pos)
        visited.add(pos)

    return np.array(path)


def box_counting_dimension(path, min_boxes=5, max_boxes=50):
    """
    Calculate fractal dimension of path using box-counting method.

    D = -lim(log(N)/log(ε)) as ε → 0

    For a path: D=1 is a line, D=2 fills the plane, D≈1.46 is the predicted optimum.
    """
    if len(path) < 10:
        return None, None, None

    # Normalize path to unit square
    path_norm = path - path.min(axis=0)
    scale = path_norm.max()
    if scale == 0:
        return None, None, None
    path_norm = path_norm / scale

    box_sizes = []
    box_counts = []

    for n_boxes in range(min_boxes, max_boxes + 1):
        box_size = 1.0 / n_boxes

        # Count occupied boxes
        occupied = set()
        for point in path_norm:
            box_x = min(int(point[0] / box_size), n_boxes - 1)
            box_y = min(int(point[1] / box_size), n_boxes - 1)
            occupied.add((box_x, box_y))

        box_sizes.append(box_size)
        box_counts.append(len(occupied))

    # Linear regression on log-log plot
    log_sizes = np.log(box_sizes)
    log_counts = np.log(box_counts)

    # D = -slope
    coeffs = np.polyfit(log_sizes, log_counts, 1)
    dimension = -coeffs[0]

    return dimension, log_sizes, log_counts


def run_simulation(n_trials=20, grid_size=100, lookahead=2):
    """Run multiple trials and analyze the emergent fractal dimension."""

    print("=" * 60)
    print("SELECTOR AGENT SIMULATION")
    print("Testing: Does option-maximizing behavior → D ≈ 1.46?")
    print("=" * 60)
    print(f"\nParameters:")
    print(f"  Grid size: {grid_size}x{grid_size}")
    print(f"  Lookahead depth: {lookahead}")
    print(f"  Number of trials: {n_trials}")
    print(f"\nDFA Predictions:")
    print(f"  D₂ = 19/13 = {D2_PREDICTED:.4f}")
    print(f"  κ (granular) = {KAPPA_GRANULAR:.2f}")
    print()

    dimensions = []
    path_lengths = []
    all_paths = []

    for trial in range(n_trials):
        path = selector_agent_walk(grid_size=grid_size, lookahead=lookahead)
        dim, log_s, log_c = box_counting_dimension(path)

        if dim is not None:
            dimensions.append(dim)
            path_lengths.append(len(path))
            all_paths.append(path)
            print(f"  Trial {trial+1:2d}: D = {dim:.4f}, path length = {len(path)}")

    if not dimensions:
        print("ERROR: No valid paths generated")
        return None

    # Statistics
    mean_d = np.mean(dimensions)
    std_d = np.std(dimensions)
    mean_len = np.mean(path_lengths)

    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    print(f"\nMeasured Fractal Dimension:")
    print(f"  Mean D = {mean_d:.4f} ± {std_d:.4f}")
    print(f"  Range: [{min(dimensions):.4f}, {max(dimensions):.4f}]")
    print(f"\nComparison to DFA Constants:")
    print(f"  D₂ = 19/13 = {D2_PREDICTED:.4f}")
    print(f"  Deviation from D₂: {abs(mean_d - D2_PREDICTED):.4f} ({100*abs(mean_d - D2_PREDICTED)/D2_PREDICTED:.1f}%)")
    print(f"  κ (granular) = {KAPPA_GRANULAR:.2f}")
    print(f"  Deviation from κ: {abs(mean_d - KAPPA_GRANULAR):.4f} ({100*abs(mean_d - KAPPA_GRANULAR)/KAPPA_GRANULAR:.1f}%)")
    print(f"\nPath Statistics:")
    print(f"  Mean length: {mean_len:.1f} steps")

    # Interpretation
    print("\n" + "=" * 60)
    print("INTERPRETATION")
    print("=" * 60)

    if abs(mean_d - D2_PREDICTED) < 0.1:
        print("\n✓ VALIDATED: Selector agent converges to D ≈ 1.46")
        print("  The 'stress dimension' emerges from option-maximizing behavior.")
        print("  R-seeking under S-constraint → D₂ = 19/13")
        status = "VALIDATED"
    elif abs(mean_d - KAPPA_GRANULAR) < 0.1:
        print("\n~ CLOSE: Selector agent near granular κ = 1.41")
        print("  Within the DFA coupling zone [1.41, 1.46]")
        status = "CLOSE"
    elif 1.3 < mean_d < 1.6:
        print("\n? INTERESTING: D in range but not exact match")
        print(f"  Measured D = {mean_d:.3f} is in coupling zone")
        status = "PARTIAL"
    else:
        print("\n✗ NOT CONFIRMED: D outside expected range")
        status = "NOT_CONFIRMED"

    # Create visualization
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))

    # Plot 1: Example path
    ax1 = axes[0, 0]
    if all_paths:
        example_path = all_paths[np.argmax(path_lengths)]
        ax1.plot(example_path[:, 0], example_path[:, 1], 'b-', alpha=0.5, linewidth=0.5)
        ax1.plot(example_path[0, 0], example_path[0, 1], 'go', markersize=10, label='Start')
        ax1.plot(example_path[-1, 0], example_path[-1, 1], 'ro', markersize=10, label='End')
        ax1.set_title(f'Selector Agent Path (longest trial)\nLength: {len(example_path)} steps')
        ax1.set_xlabel('X')
        ax1.set_ylabel('Y')
        ax1.legend()
        ax1.set_aspect('equal')

    # Plot 2: Dimension histogram
    ax2 = axes[0, 1]
    ax2.hist(dimensions, bins=15, edgecolor='black', alpha=0.7)
    ax2.axvline(D2_PREDICTED, color='r', linestyle='--', linewidth=2, label=f'D₂ = 19/13 = {D2_PREDICTED:.3f}')
    ax2.axvline(KAPPA_GRANULAR, color='orange', linestyle='--', linewidth=2, label=f'κ = {KAPPA_GRANULAR}')
    ax2.axvline(mean_d, color='blue', linestyle='-', linewidth=2, label=f'Mean = {mean_d:.3f}')
    ax2.set_xlabel('Fractal Dimension D')
    ax2.set_ylabel('Count')
    ax2.set_title('Distribution of Measured Dimensions')
    ax2.legend()

    # Plot 3: Box-counting example
    ax3 = axes[1, 0]
    if all_paths:
        longest_path = all_paths[np.argmax(path_lengths)]
        dim, log_s, log_c = box_counting_dimension(longest_path)
        if log_s is not None:
            ax3.scatter(log_s, log_c, alpha=0.7)
            coeffs = np.polyfit(log_s, log_c, 1)
            fit_line = np.poly1d(coeffs)
            ax3.plot(log_s, fit_line(log_s), 'r-', linewidth=2,
                    label=f'Slope = {-coeffs[0]:.3f} (D = {dim:.3f})')
            ax3.set_xlabel('log(box size)')
            ax3.set_ylabel('log(box count)')
            ax3.set_title('Box-Counting Analysis')
            ax3.legend()

    # Plot 4: Dimension vs path length
    ax4 = axes[1, 1]
    ax4.scatter(path_lengths, dimensions, alpha=0.7)
    ax4.axhline(D2_PREDICTED, color='r', linestyle='--', label=f'D₂ = {D2_PREDICTED:.3f}')
    ax4.axhline(KAPPA_GRANULAR, color='orange', linestyle='--', label=f'κ = {KAPPA_GRANULAR}')
    ax4.set_xlabel('Path Length (steps)')
    ax4.set_ylabel('Fractal Dimension D')
    ax4.set_title('Dimension vs Path Length')
    ax4.legend()

    plt.tight_layout()
    plt.savefig('/home/king/Downloads/documentsforgi/evidence/selector_agent_simulation.png', dpi=150)
    print(f"\nFigure saved to: evidence/selector_agent_simulation.png")
    plt.close()

    # Save results
    results = {
        "simulation": "Selector Agent (Option-Maximizing)",
        "parameters": {
            "grid_size": grid_size,
            "lookahead": lookahead,
            "n_trials": n_trials
        },
        "results": {
            "mean_dimension": float(mean_d),
            "std_dimension": float(std_d),
            "min_dimension": float(min(dimensions)),
            "max_dimension": float(max(dimensions)),
            "mean_path_length": float(mean_len)
        },
        "dfa_comparison": {
            "D2_predicted": D2_PREDICTED,
            "deviation_from_D2": float(abs(mean_d - D2_PREDICTED)),
            "deviation_percent": float(100*abs(mean_d - D2_PREDICTED)/D2_PREDICTED),
            "kappa_granular": KAPPA_GRANULAR,
            "deviation_from_kappa": float(abs(mean_d - KAPPA_GRANULAR))
        },
        "status": status
    }

    with open('/home/king/Downloads/documentsforgi/evidence/selector_agent_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    print(f"Results saved to: evidence/selector_agent_results.json")

    return results


def parameter_sweep():
    """Test how lookahead depth affects emergent dimension."""
    print("\n" + "=" * 60)
    print("PARAMETER SWEEP: Lookahead Depth vs Dimension")
    print("=" * 60)

    results = []
    for lookahead in [0, 1, 2, 3]:
        print(f"\nLookahead = {lookahead}:")
        dims = []
        for _ in range(10):
            path = selector_agent_walk(grid_size=80, lookahead=lookahead, max_steps=3000)
            d, _, _ = box_counting_dimension(path)
            if d:
                dims.append(d)
        if dims:
            mean_d = np.mean(dims)
            print(f"  Mean D = {mean_d:.4f} ± {np.std(dims):.4f}")
            results.append((lookahead, mean_d, np.std(dims)))

    print("\nSummary: Does more lookahead → closer to D₂ = 1.46?")
    for la, d, s in results:
        dev = abs(d - D2_PREDICTED)
        print(f"  Lookahead {la}: D = {d:.3f}, deviation = {dev:.3f}")


if __name__ == "__main__":
    # Main simulation
    results = run_simulation(n_trials=20, grid_size=100, lookahead=2)

    # Parameter sweep
    parameter_sweep()

    print("\n" + "=" * 60)
    print("SIMULATION COMPLETE")
    print("=" * 60)
