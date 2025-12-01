# Claim: Core S+R Equations

## Source
Grok Export 031

## Statement
The DFA state \(\Psi(x, t)\) evolves via:
\[
\frac{d}{dt} \Psi(x, t) = S(x) \oplus R(x) = \nabla \cdot \left( S(x) - C \cdot \nabla R(x) \right) + \beta \cdot [S, R]
\]
where:
- \(S(x) = \sum_{i=1}^{N} \phi_i(x) \cdot \mathbf{v}_i\) (Structural component)
- \(R(x) = \int K(x, y) S(y) \, dy\) (Relational component)
- \(K(x, y) = \exp(-\|x-y\|^2 / 2\sigma^2) \cdot \|x-y\|^{-\alpha}\)
- \(C = 0.35\)
- \(\beta \approx 10^{-3}\)

## Context
Derived from a variational principle minimizing \(\mathcal{L} = \|S\|^2 + \|R\|^2 - 2C \langle S, R \rangle + \frac{1}{2} [S, R]^2\).
