# Layer 3 — Epistemology: Truth, Verification, and Accountability

> **Core principle:** AI systems produce probabilistic outputs — educated guesses, not facts. Epistemology capabilities are the controls that distinguish verified organizational knowledge from model inference, and build auditable chains of evidence for every decision.

---

## What Epistemology Covers

| Capability Domain | Description |
|---|---|
| **Fact verification** | Distinguishing confirmed facts from model-generated inferences |
| **Retrieval-Augmented Generation (RAG)** | Grounding AI responses in owned, cited sources |
| **Confidence scoring** | Quantifying and communicating uncertainty in outputs |
| **Audit trail generation** | Creating an evidence chain for every significant decision |
| **Hallucination detection** | Catching outputs not supported by owned evidence |
| **Cryptographic validation** | Tamper-evident verification of pipeline integrity |

---

## Core Capabilities

### E1 — Source-Grounded Retrieval (Owned RAG)
**What it does:** Before generating a response, retrieves relevant documents, records, and facts from the agency's owned knowledge store and uses them as the primary context for the response — with citations.

**Why it matters for government:** A model that answers questions from its training data alone is essentially citing "things I've heard." A model grounded in your agency's owned, up-to-date records is citing "our official data, record ID X, validated on date Y." The difference is auditable accountability.

**Minimum acceptable standard (Score 3):** RAG pipeline retrieves from agency-controlled document store; source citations included in responses.

**Good practice (Score 4–5):** RAG grounded in the Data Substrate; every response cites specific records with IDs and validation timestamps; confidence score reported; responses that cannot be grounded are flagged rather than guessed.

---

### E2 — Fact Verification Gate
**What it does:** For high-stakes decisions, compares the AI system's output against independently verified ground truth before that output is acted upon.

**Why it matters for government:** When an AI system says "taxpayer's income is $87,400 from three sources," a verification gate checks that claim against the agency's own authoritative data before any action is taken. This is the difference between using AI as a decision support tool and using it as an unquestioned oracle.

**Minimum acceptable standard (Score 3):** Key outputs verified against a primary source before consequential actions; mismatches logged.

**Good practice (Score 4–5):** Automated verification gate for all consequential outputs; multi-source cross-checking; verification results stored in Data Substrate; discrepancies trigger review workflow.

---

### E3 — Confidence Scoring and Uncertainty Communication
**What it does:** Every significant output carries a confidence score with an explanation of its components — and that score is communicated meaningfully to the decision-maker.

**Why it matters for government:** A confidence score of "94%" means nothing without knowing what contributes to it. Is that 94% based on one source or five? Is the remaining 6% uncertainty due to a missing record or a conflicting one? Decision-makers need to understand uncertainty, not just receive a number.

**Minimum acceptable standard (Score 3):** Confidence scores reported; methodology documented.

**Good practice (Score 4–5):** Confidence scores decomposed by contributing evidence; uncertainty sources identified (missing data, conflicting sources, model uncertainty); scores are traceable to specific records.

---

### E4 — Immutable Decision Audit Log
**What it does:** Creates a tamper-evident record of every significant AI-assisted decision: what question was asked, what sources were retrieved, what the output was, what the confidence was, who reviewed it, and what action was taken.

**Why it matters for government:** The audit log is the evidentiary foundation for every investigation, appeal, oversight inquiry, and compliance review. Without it, an agency cannot demonstrate what happened — only assert it.

**Minimum acceptable standard (Score 3):** Decision log maintained; includes inputs, outputs, and reviewer; retained per policy.

**Good practice (Score 4–5):** Cryptographically signed log entries; immutable storage; end-to-end trace from input data through verification through decision; searchable by case, date, reviewer, or confidence band.

---

### E5 — Hallucination Detection
**What it does:** Detects when a model's output makes claims that are not supported by the retrieved sources or the owned knowledge base — and flags or blocks those outputs before they reach decision-makers.

**Why it matters for government:** Language models sometimes state things confidently that are simply wrong. In a tax administration or benefits context, an undetected hallucination could affect thousands of citizens before the error is discovered.

**Minimum acceptable standard (Score 3):** Response-level hallucination checking for high-stakes workflows; flagged outputs reviewed before use.

**Good practice (Score 4–5):** Automated hallucination detection on all consequential outputs; output not passed to decision-maker if it cannot be grounded; detection results logged.

---

### E6 — Cryptographic Pipeline Integrity
**What it does:** Uses cryptographic hashes (SHA-256 or equivalent) to verify that the data, model configuration, and pipeline components used for a given decision are exactly what they are supposed to be — and have not been tampered with.

**Why it matters for government:** Compliance and security frameworks require assurance that the system being run is the system that was approved. Cryptographic integrity checks make it possible to prove this.

**Minimum acceptable standard (Score 3):** Model configuration files hashed and verified at deployment; mismatches block deployment.

**Good practice (Score 4–5):** End-to-end pipeline integrity verification; every artifact (data, model, config, code) hashed and verified before execution; continuous integrity monitoring in production.

---

## Recommended Tools

### Self-Hosted / Open Source (Preferred)

| Tool | Category | Description |
|---|---|---|
| **LlamaIndex** | RAG framework | Open-source RAG orchestration; integrates with self-hosted vector stores and LLMs |
| **Haystack** | RAG + QA pipeline | Open-source NLP framework with retrieval, verification, and answer generation |
| **LangChain** | AI application framework | Widely used open-source framework for building RAG and agent pipelines |
| **Guardrails AI** | Output validation | Open-source framework for defining and enforcing output constraints and fact checks |
| **RAGAS** | RAG evaluation | Open-source framework for evaluating RAG pipeline quality and grounding |
| **TruLens** | LLM evaluation | Open-source LLM evaluation and observability; tracks faithfulness and relevance |
| **Giskard** | AI testing and validation | Open-source AI quality testing; detects hallucinations and bias in model outputs |
| **Loguru / OpenTelemetry** | Audit logging | Structured logging and distributed tracing for pipeline observability |
| **Sigstore / cosign** | Cryptographic signing | Open-source tooling for signing and verifying software artifacts and configurations |

### Deployment Notes

- **For RAG:** LlamaIndex and Haystack both integrate well with self-hosted vector stores (Chroma, Qdrant) and self-hosted LLMs (Ollama, vLLM)
- **For output validation:** Guardrails AI is the leading open-source tool for defining and enforcing output schemas and constraints
- **For audit logging:** OpenTelemetry is the open standard; integrates with most observability backends
- **For air-gapped environments:** All RAG tools can be run without internet access when paired with a self-hosted LLM

---

## Patterns

### Pattern E-A: Grounded Response with Citation Chain
Every response includes: the answer, the records retrieved to support it, the confidence score, and a list of source citations with IDs and timestamps. Responses that cannot be grounded in owned sources are returned as "insufficient evidence" rather than as a best-guess.

### Pattern E-B: Two-Layer Verification (Inference + Verification)
AI inference layer produces a candidate answer. A separate, deterministic verification layer checks that answer against owned ground-truth records. The final output includes both the inference and the verification result — distinguishing "model said X" from "verified against record Y: confirmed / unconfirmed / conflicting."

### Pattern E-C: Confidence Banding
Outputs are classified into confidence bands that determine required handling:
- **High (≥ 90%):** Automated processing with human spot-check
- **Medium (70–89%):** Human review before action
- **Low (< 70%):** Escalation required; no automated action

Band thresholds are policy-configurable and version-controlled.

---

## Common Weaknesses to Watch For

| Weakness | Risk | Signal |
|---|---|---|
| No source citations on AI outputs | Cannot audit or defend decisions | "The model gave us a score of 87" |
| Verification depends on vendor data | Cannot independently confirm results | "We verify using [Vendor]'s cross-reference service" |
| Confidence scores without methodology | Numbers mean nothing; false confidence | Scores reported but not explained |
| No hallucination detection | Fabricated facts reach decision-makers | No testing for unsupported claims |
| Audit logs not immutable | Log tampering risk; compliance gap | Logs stored in editable format |

---

## Related Capabilities

- **Metrology (Layer 1):** Epistemology's verification gates depend on Metrology's quality-validated, provenanced data as the ground truth source.
- **Ontology (Layer 2):** Fact verification uses the Ontology layer's entity model to check that claims about entities are consistent with known relationships.
- **Praxeology (Layer 4):** Epistemology determines whether evidence is sufficient before Praxeology takes action; confidence bands gate workflow progression.
- **Data Substrate:** All verification results, confidence scores, and audit records are written to the Data Substrate.
