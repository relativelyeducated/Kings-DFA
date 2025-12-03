import json
import numpy as np
import pandas as pd
from pathlib import Path

class LSparkCalculator:
    """
    L-Spark Equation:
    L_Spark(n, κ, D₂) = (R/(R+S)) × exp(-(n/456)^(2-D₂))

    Where:
    - κ = R/(R+S) : Coupling parameter (0-1)
    - 456 : Universal harmonic
    - D₂ : Correlation dimension (~1.46 at criticality)
    """

    def __init__(self, workspace="/home/king/Downloads/documentsforgi/workspace"):
        self.workspace = Path(workspace)
        self.D2_critical = 1.46
        self.harmonic = 456

    def calculate_kappa(self, s_measure: float, r_measure: float) -> float:
        """Calculate coupling parameter κ"""
        total = s_measure + r_measure
        if total == 0:
            return 0.5
        return r_measure / total

    def classify_failure_zone(self, kappa: float) -> str:
        """Classify failure by κ zone"""
        if kappa < 0.35:
            return "over_constrained"  # S-axis failure (too rigid)
        elif kappa > 0.65:
            return "under_constrained"  # R-axis failure (too loose)
        else:
            return "optimal_zone"  # Not a coupling failure

    def analyze_parenting_data(self, csv_path: str) -> dict:
        """
        Analyze parenting outcomes dataset
        Expected columns: style, outcome, outcome_severity
        """
        if not os.path.exists(csv_path):
            return {"error": "File not found"}
            
        df = pd.read_csv(csv_path)

        # Map parenting styles to κ
        style_kappa = {
            "authoritarian": 0.25,
            "authoritative": 0.45,
            "permissive": 0.70,
            "neglectful": 0.85
        }

        df["kappa"] = df["style"].map(style_kappa)
        df["failure_zone"] = df["kappa"].apply(self.classify_failure_zone)

        # Count failures by zone
        negative_outcomes = df[df["outcome"] == "negative"]

        over_constrained = len(negative_outcomes[
            negative_outcomes["failure_zone"] == "over_constrained"
        ])
        under_constrained = len(negative_outcomes[
            negative_outcomes["failure_zone"] == "under_constrained"
        ])

        # Calculate ratio
        if over_constrained == 0:
            ratio = float('inf')
        else:
            ratio = under_constrained / over_constrained

        return {
            "total_failures": len(negative_outcomes),
            "over_constrained_failures": over_constrained,
            "under_constrained_failures": under_constrained,
            "failure_ratio_high_to_low_kappa": ratio,
            "interpretation": self._interpret_ratio(ratio)
        }

    def _interpret_ratio(self, ratio: float) -> str:
        """Interpret the failure ratio"""
        if ratio > 4:
            return f"Failures cluster {ratio:.1f}:1 at high-κ (too loose). AI training data likely inverted."
        elif ratio > 2:
            return f"Moderate high-κ clustering ({ratio:.1f}:1). Some inversion likely."
        elif ratio > 0.5:
            return f"Balanced failure distribution ({ratio:.1f}:1). Minimal correction needed."
        else:
            return f"Failures cluster at low-κ (too rigid). Unusual pattern."

if __name__ == "__main__":
    import os
    calc = LSparkCalculator()
    
    # Create dummy data for testing
    dummy_data = Path("/home/king/Downloads/documentsforgi/workspace/data/parenting_outcomes.csv")
    if not dummy_data.exists():
        with open(dummy_data, "w") as f:
            f.write("style,outcome,outcome_severity\n")
            f.write("authoritarian,negative,high\n")
            f.write("permissive,negative,medium\n")
            f.write("authoritative,positive,low\n")
            f.write("neglectful,negative,high\n")
            f.write("permissive,negative,high\n")

    # Example: Analyze parenting data
    results = calc.analyze_parenting_data(str(dummy_data))

    # Save results
    with open("/home/king/Downloads/documentsforgi/workspace/results/lspark_ratios.json", "w") as f:
        json.dump(results, f, indent=2)

    print(f"Analysis complete: {results}")
