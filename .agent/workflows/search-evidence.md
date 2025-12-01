---
description: Find evidence for a claim
---
1. **Input**: Claim file path.
2. **Action**:
   - Parse keywords from claim.
   - Search PubMed, arXiv, and local conversation exports.
   - Search specifically for data matching DFA constants (0.35, 456, etc.).
3. **Output**: Update claim file with `## Search Results` section.
