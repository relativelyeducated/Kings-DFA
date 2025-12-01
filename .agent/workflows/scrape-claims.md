---
description: Scan conversation exports and extract all claims
---
1. **Input**: Path to conversation exports folder.
2. **Action**: Iterate through each markdown file.
3. **Extraction**: Identify statements that propose a relationship, constant, or mechanism.
4. **Output**: Create a list of claims in `claims/pending/` with format `{topic}_claim.md`.
