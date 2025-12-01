---
description: Execute validation (5 attempts max)
---
1. **Input**: Validation protocol.
2. **Action**:
   - Run defined tests (scripts, simulations).
   - **Retry Logic**: If failure, retry up to 5 times with adjusted parameters if appropriate.
   - Log all attempts.
3. **Output**: Test logs and final result (Pass/Fail).
