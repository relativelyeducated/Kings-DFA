import numpy as np

# DFA Constants
D2 = 1.4615  # Packing Conflict Dimension (19/13)
BASE_HARMONIC = 312.0  # Geometric Base
STELLAR_HEARTBEAT = 456.0  # 312 * D2

def check_harmonics(observed_freq, system_name):
    """
    Checks if an observed frequency matches the DFA harmonic series.
    Series 1: N * 312 (Base)
    Series 2: N * 456 (Heartbeat)
    """
    print(f"\n--- Analyzing {system_name} ---")
    print(f"Observed Frequency: {observed_freq:.2f} µHz (or equivalent)")

    # Check Base Harmonic (312)
    n_base = observed_freq / BASE_HARMONIC
    n_base_round = round(n_base)
    if n_base_round == 0: n_base_round = 1
    diff_base = abs(observed_freq - (n_base_round * BASE_HARMONIC))
    error_base = (diff_base / observed_freq) * 100
    
    # Check Heartbeat Harmonic (456)
    n_heart = observed_freq / STELLAR_HEARTBEAT
    n_heart_round = round(n_heart)
    if n_heart_round == 0: n_heart_round = 1
    diff_heart = abs(observed_freq - (n_heart_round * STELLAR_HEARTBEAT))
    error_heart = (diff_heart / observed_freq) * 100

    # Determine Best Fit
    if error_base < error_heart:
        best_fit = "BASE (312)"
        harmonic = n_base_round
        error = error_base
        pred = n_base_round * BASE_HARMONIC
    else:
        best_fit = "HEARTBEAT (456)"
        harmonic = n_heart_round
        error = error_heart
        pred = n_heart_round * STELLAR_HEARTBEAT

    print(f"Best Fit: {best_fit}")
    print(f"Harmonic N: {harmonic}")
    print(f"Predicted: {pred:.2f}")
    print(f"Error: {error:.4f}%")
    
    if error < 2.0:
        print("✅ VALIDATED (< 2%)")
    else:
        print("❌ NO MATCH (> 2%)")

# --- Test Data from Dr. Reed & Solar Cycle ---

# 1. KIC 010139564 (Dr. Reed 2010)
# Anomalous mode at 3165 seconds period
# Frequency = 1 / 3165 Hz = 0.0003159 Hz = 315.9 µHz
check_harmonics(315.9, "KIC 010139564 (Anomalous Mode)")

# 2. 2M1938+4603 (Dr. Reed 2010)
# Strongest peak at 2265.8 µHz
check_harmonics(2265.8, "2M1938+4603 (Dominant Peak)")

# --- CSV Processing ---
import csv

def process_csv(filepath):
    print(f"\n=== Processing Dataset: {filepath} ===")
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            system = row['System']
            val = float(row['Observed_Value'])
            type_ = row['Type']
            
            # Convert Periods (days) to Frequency-like check or direct Period check
            # For this simple script, we treat 'Period' as a target for 456-days
            # and 'Frequency' as a target for 312/456 uHz
            
            if "Period" in type_:
                # Check Period Harmonic: N * Period = 456
                target = 456.0
                ratio = target / val
                n_round = round(ratio)
                if n_round == 0: n_round = 1
                error = abs(ratio - n_round) / n_round * 100
                print(f"\nSystem: {system}")
                print(f"Period: {val} days -> Target 456")
                print(f"Harmonic: {n_round} (Ratio {ratio:.2f})")
                print(f"Error: {error:.2f}%")
                if error < 2.0: print("✅ VALIDATED")
                else: print("❌ NO MATCH")
            else:
                # Frequency Check
                check_harmonics(val, system)

if __name__ == "__main__":
    # Run on manual dataset
    # process_csv("data/manual_heartbeat_stars.csv")
    
    import sys
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        if filepath.endswith('.tsv'):
            print(f"\n=== Processing Kirk 2016 TSV: {filepath} ===")
            with open(filepath, 'r') as f:
                lines = f.readlines()
            
            data_start = False
            for line in lines:
                if line.startswith("---"):
                    data_start = True
                    continue
                if not data_start: continue
                
                parts = line.split()
                if len(parts) < 6: continue
                
                # Kirk 2016 Format: Index, KIC, REF, TP, DV, Per, ...
                # Sometimes DV is empty, shifting columns? 
                # The header says: V3 KIC REF TP DV Per
                # Let's be careful.
                # Line 41: 1 01573836 0 0 3.557093 ... -> DV is empty
                # Line 44: 1 02697935 0 0 DV 21.513359 ... -> DV is present
                
                kic = parts[1]
                
                # Find the period. It's usually the first float after the flags.
                # Flags are usually 0 or 1.
                # Let's look for the first number > 0 that has a decimal point and is after index 4
                
                period = 0.0
                for part in parts[4:]:
                    try:
                        val = float(part)
                        if "." in part and val > 0:
                            period = val
                            break
                    except:
                        continue
                
                if period > 0:
                    # Check Period Harmonic: N * Period = 456
                    target = 456.0
                    ratio = target / period
                    n_round = round(ratio)
                    if n_round == 0: n_round = 1
                    error = abs(ratio - n_round) / n_round * 100
                    
                    if error < 1.5: # Strict 1.5% threshold
                        print(f"\nSystem: KIC {kic}")
                        print(f"Period: {period} days -> Target 456")
                        print(f"Harmonic: {n_round} (Ratio {ratio:.2f})")
                        print(f"Error: {error:.2f}%")
                        print("✅ VALIDATED")
        else:
            process_csv(filepath)
    else:
        print("Please provide a file path (CSV or TSV).")
