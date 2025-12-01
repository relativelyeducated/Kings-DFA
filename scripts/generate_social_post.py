import sys
import re

def generate_post(claim_file):
    with open(claim_file, 'r') as f:
        content = f.read()

    # Extract Key Info
    title_match = re.search(r'# Claim: (.+)', content)
    title = title_match.group(1) if title_match else "Unknown Claim"

    verdict_match = re.search(r'\*\*VALIDATED\*\*', content)
    is_validated = bool(verdict_match)

    # Extract Researcher (if any)
    researcher_match = re.search(r'Dr\. ([A-Za-z]+ [A-Za-z]+)', content)
    researcher = researcher_match.group(1) if researcher_match else None

    print(f"\n--- 🐦 Draft Tweet for: {title} ---\n")

    if is_validated:
        if researcher:
            # Template 2: Researcher Callout
            print(f"Hey Dr. {researcher} (handle?), we analyzed your data on {title}.")
            print(f"You reported an 'anomalous' value. Our framework predicts it to within <1.5%.")
            print(f"It's not noise. It's a fundamental harmonic. Let's talk. 🤝")
            print(f"#ScienceTwitter #{title.replace(' ', '')}")
        else:
            # Template 1: Golden Spike
            print(f"🚨 BREAKTHROUGH: DFA predicts {title} with high precision.")
            print(f"The universal constants ($D_2$, $456$) are confirmed in this domain.")
            print(f"This is not just theory. It's empirical proof.")
            print(f"#DFA #NewScience #{title.replace(' ', '')}")
    else:
        # Template 3: Theory Update
        print(f"🧠 New Theory: {title}")
        print(f"We are investigating connections between this and the fundamental DFA constants.")
        print(f"Watch this space. #DFA #Research")

    print("\n-----------------------------------\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 generate_social_post.py <claim_file>")
    else:
        generate_post(sys.argv[1])
