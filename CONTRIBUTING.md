# Contributing

This repository is the canonical reference for the draft **Philosophical AI
Architecture** shared for discussion, refinement, and review. Feedback is
welcome — including disagreement. This is a proposal, not a deployed system:
contributions are documentation and design feedback, not code to build or run.

All contributions must align with the narrative in
[docs/pitch-strategy.md](docs/pitch-strategy.md). For term definitions, see
[docs/glossary.md](docs/glossary.md).

## Ways to Participate

- **Ask a question or flag an issue:** open an [issue](../../issues/new/choose).
- **Suggest specific wording or structure edits:** open a pull request against `main`.
- **Raise a substantive design change:** open a **Proposal / RFC** issue so it can be
  discussed before a pull request.

## Helpful Feedback

- Logical inconsistencies or contradictions across documents
- Unclear, ambiguous, or unsupported claims
- Gaps in the five-layer model, the scoring rubric, or the catalog
- Real-world examples, references, or counterexamples
- Drift from the pitch strategy terminology or tone

## Proposal / RFC Process

For changes that affect the layer model, scoring semantics, or governance approach:

1. Open a **Proposal / RFC** issue describing the problem and the proposed change.
2. Allow discussion and refinement in the thread.
3. Once there is rough consensus, open a pull request that links the issue.
4. Substantive changes are versioned using semantic versioning (MAJOR.MINOR.PATCH).

## Style Notes

- Punchy, authoritative, direct — engineer-to-engineer, executive-to-executive.
- Ground abstract concepts in physical metaphors (Data Substrate, Control Plane, Catalog).
- Never conflate the **Philosophical AI Architecture** (ecosystem) with the **MOEPA 5-Layer Framework** (engineering blueprint and intake rubric).
- Preserve the five-layer structure (Metrology, Ontology, Epistemology, Praxeology, Axiology).
- Keep the GO / CONDITIONAL / NO-GO scoring model consistent across `ARCHITECTURE.md` and `catalog/`.