import numpy as np

def circle_intersection_area(R, d):
    """
    Calculate the area of intersection (overlap) between two circles of radius R
    separated by distance d.
    Formula: A = 2 * R^2 * arccos(d / (2*R)) - (d / 2) * sqrt(4*R^2 - d^2)
    """
    if d >= 2 * R:
        return 0.0
    if d <= 0:
        return np.pi * R**2
    
    term1 = 2 * (R**2) * np.arccos(d / (2 * R))
    term2 = (d / 2) * np.sqrt(4 * (R**2) - d**2)
    return term1 - term2

def find_d_for_target_area(R, target_area_fraction):
    """
    Find the d/R ratio that yields a specific overlap area fraction.
    """
    target_area = target_area_fraction * (np.pi * R**2)
    
    # Binary search for d
    low = 0.0
    high = 2.0 * R
    for _ in range(100):
        mid = (low + high) / 2
        area = circle_intersection_area(R, mid)
        if area > target_area:
            low = mid
        else:
            high = mid
            
    return (low + high) / 2

def main():
    R = 1.0
    d_virial = 0.5 * R
    
    # 1. Check Claude's claim about d/R = 0.5
    area_virial = circle_intersection_area(R, d_virial)
    total_area = np.pi * R**2
    fraction_virial = area_virial / total_area
    
    print(f"--- CHECK 1: d/R = 0.5 ---")
    print(f"Overlap Area: {area_virial:.6f}")
    print(f"Total Circle Area: {total_area:.6f}")
    print(f"Overlap Fraction: {fraction_virial:.6f}")
    print(f"Claude's Claim: 'Impossible' (> pi*R^2)? No, Claude's manual calc was wrong.")
    print(f"Gemini's Claim: 0.685? Let's see.")
    
    # 2. Find d/R for target 0.685 (Dark Energy)
    target_de = 0.685
    d_target = find_d_for_target_area(R, target_de)
    
    print(f"\n--- CHECK 2: Target Omega_DE = {target_de} ---")
    print(f"Required d/R: {d_target:.6f}")
    
    # 3. Check d/R = 1/e (Threshold)
    d_threshold = (1/np.e) * R
    area_threshold = circle_intersection_area(R, d_threshold)
    fraction_threshold = area_threshold / total_area
    
    print(f"\n--- CHECK 3: d/R = 1/e ({1/np.e:.4f}) ---")
    print(f"Overlap Fraction: {fraction_threshold:.6f}")

if __name__ == "__main__":
    main()
