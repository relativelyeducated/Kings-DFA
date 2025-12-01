import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

def draw_vesica():
    # Setup
    R = 1.0
    d = 0.5 * R  # Virial equilibrium
    
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Colors (Premium Palette)
    color_S = '#2E86AB'  # Blue for Structure
    color_R = '#F24236'  # Red for Relation
    color_overlap = '#564256' # Dark Purple for Overlap
    color_text = '#333333'
    
    # Circles
    circle_S = patches.Circle((-d/2, 0), R, linewidth=2, edgecolor=color_S, facecolor=color_S, alpha=0.1, label='Structure (S)')
    circle_R = patches.Circle((d/2, 0), R, linewidth=2, edgecolor=color_R, facecolor=color_R, alpha=0.1, label='Relation (R)')
    
    ax.add_patch(circle_S)
    ax.add_patch(circle_R)
    
    # Overlap Region (Clip path logic simplified for visual representation)
    # We will just draw the intersection area conceptually or use fill_between
    theta = np.linspace(0, 2*np.pi, 200)
    
    # Intersection points calculation
    # x^2 + y^2 = R^2 shifted by +/- d/2
    # Intersection at x=0? No, intersection is at x=0 for d=2R (touching). 
    # For d=0.5R:
    # (x + d/2)^2 + y^2 = R^2
    # (x - d/2)^2 + y^2 = R^2
    # Subtracting: (x+d/2)^2 - (x-d/2)^2 = 0 => 2x*d = 0 => x=0.
    # So intersection is at x=0.
    # y^2 = R^2 - (d/2)^2 => y = +/- sqrt(R^2 - d^2/4)
    
    h = np.sqrt(R**2 - (d/2)**2)
    
    # Fill overlap
    # Left boundary of overlap is right arc of left circle: (x+d/2)^2 + y^2 = R^2 => x = -d/2 + sqrt(R^2 - y^2)
    # Right boundary of overlap is left arc of right circle: (x-d/2)^2 + y^2 = R^2 => x = d/2 - sqrt(R^2 - y^2)
    # Wait, for x=0 to be the center of the overlap, the circles are at +/- d/2.
    # The overlap is bounded by x > 0 arc of Left Circle and x < 0 arc of Right Circle?
    # No.
    # Left Circle Center: (-0.25, 0). Right Circle Center: (0.25, 0).
    # Overlap is x between intersection points? No, intersection is at x=0, y=+/-h.
    # The overlap region is the lens.
    # Boundary 1 (Right side): Part of Circle S (Center -d/2). x = -d/2 + sqrt(R^2 - y^2)
    # Boundary 2 (Left side): Part of Circle R (Center +d/2). x = d/2 - sqrt(R^2 - y^2)
    # Actually, for the standard Vesica, the overlap is the area *between* the centers if d=R.
    # Here d=0.5R, so they overlap heavily.
    
    y_vals = np.linspace(-h, h, 200)
    x_left_arc = -d/2 + np.sqrt(R**2 - y_vals**2) # Arc of Left Circle (S)
    x_right_arc = d/2 - np.sqrt(R**2 - y_vals**2) # Arc of Right Circle (R)
    
    # Correct logic:
    # The overlap is bounded by the arc of the RIGHT circle on the LEFT, and the LEFT circle on the RIGHT?
    # Let's visualize.
    # Circle S (Left): Center (-0.25, 0). Right edge at 0.75.
    # Circle R (Right): Center (0.25, 0). Left edge at -0.75.
    # Overlap is between x = -0.75 and x = 0.75? No.
    # Intersection is at x=0, y=+/- 0.968.
    # The "lens" is formed by:
    # The right part of Circle S (x > -0.25) and left part of Circle R (x < 0.25)?
    # No, the intersection is the set of points in BOTH.
    # Boundary is:
    # max(x_left_circle_left_edge, x_right_circle_left_edge) ??
    # Let's just use fill_between with the correct functions.
    # Circle S: (x+d/2)^2 + y^2 = R^2. Right arc: x = -d/2 + sqrt(R^2 - y^2)
    # Circle R: (x-d/2)^2 + y^2 = R^2. Left arc: x = d/2 - sqrt(R^2 - y^2)
    # The overlap is bounded by x_right_arc (from Circle R) on the LEFT? No.
    # Circle R is at x=0.25. Its Left arc is at 0.25 - sqrt... which is negative.
    # Circle S is at x=-0.25. Its Right arc is at -0.25 + sqrt... which is positive.
    # So the overlap is between Circle R's left arc and Circle S's right arc.
    
    x_R_left_arc = d/2 - np.sqrt(R**2 - y_vals**2)
    x_S_right_arc = -d/2 + np.sqrt(R**2 - y_vals**2)
    
    ax.fill_betweenx(y_vals, x_R_left_arc, x_S_right_arc, color=color_overlap, alpha=0.3, label='Overlap (Dark Energy)')

    # Annotations
    ax.text(0, 0, r'$\Omega_{DE} \approx 0.685$', ha='center', va='center', fontsize=14, fontweight='bold', color='white')
    ax.text(0, -0.2, 'Overlap Area', ha='center', va='center', fontsize=10, color='white')
    
    ax.text(-0.8, 0, r'$\Omega_{M} \approx 0.315$', ha='center', va='center', fontsize=12, color=color_text)
    ax.text(-0.8, -0.15, 'Non-Overlap', ha='center', va='center', fontsize=9, color=color_text)
    
    ax.text(0.8, 0, r'$D_2 \approx 1.46$', ha='center', va='center', fontsize=12, color=color_text)
    ax.text(0.8, -0.15, 'Inverse Overlap', ha='center', va='center', fontsize=9, color=color_text)
    
    # Dimensions
    ax.plot([-d/2, d/2], [0, 0], 'k--', linewidth=1)
    ax.text(0, 0.05, r'$d = 0.5R$', ha='center', va='bottom', fontsize=10)
    
    # Outer Edge Annotation
    ax.annotate('Edge of Half Circle\n(Data Horizon?)', xy=(d/2 + R, 0), xytext=(d/2 + R + 0.2, 0.3),
                arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

    # Title
    plt.title('Vesica Piscis Geometric Unification\n(Virial Equilibrium $d/R = 0.5$)', fontsize=16, pad=20)
    
    # Limits
    ax.set_xlim(-1.8, 1.8)
    ax.set_ylim(-1.2, 1.2)
    
    plt.tight_layout()
    plt.savefig('figures/vesica_piscis_geometry.png', dpi=300, bbox_inches='tight')
    print("Figure saved to figures/vesica_piscis_geometry.png")

if __name__ == "__main__":
    draw_vesica()
