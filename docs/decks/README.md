# docs/decks

Presentation decks derived from the MOEPA documentation, built with [Marp](https://marp.app/).

## Purpose

This directory contains Marp-formatted Markdown source files for slide decks. Each deck is a derived view of an existing guide — the **source of truth always remains the corresponding Markdown guide in `docs/`**.

Using Marp keeps the deck source in plain Markdown so it stays version-controlled, diff-friendly, and audit-accessible — consistent with the MOEPA "agency-owned, open-format" principles the guides advocate.

## Available Decks

| Deck source | Based on |
| --- | --- |
| [`moepa-federal-leaders-guide.slides.md`](moepa-federal-leaders-guide.slides.md) | [`../moepa-federal-leaders-guide.md`](../moepa-federal-leaders-guide.md) |

## How to Rebuild Locally

Requires [Node.js](https://nodejs.org/) (v20+). No global install required — `npx` handles it.

```bash
# Build PPTX
npx @marp-team/marp-cli@latest --pptx docs/decks/moepa-federal-leaders-guide.slides.md -o moepa-federal-leaders-guide.pptx

# Build PDF
npx @marp-team/marp-cli@latest --pdf  docs/decks/moepa-federal-leaders-guide.slides.md -o moepa-federal-leaders-guide.pdf
```

Both commands write output files to the current working directory. Run them from the repository root.

## How to Download the Auto-Built Deck

Every push to `main` and every pull request targeting `main` that touches `docs/decks/**` triggers the [Build Decks workflow](../../.github/workflows/build-decks.yml). The PPTX and PDF are uploaded as a workflow artifact named **`moepa-federal-leaders-deck`**.

To download:
1. Go to the **Actions** tab in GitHub.
2. Click the latest **Build Decks** run.
3. Scroll to **Artifacts** and download `moepa-federal-leaders-deck`.

## Notes

- The deck is a **derived view** — it condenses and reformats content for executive briefings.
- Do **not** edit the source guide (`../moepa-federal-leaders-guide.md`) to fix deck issues; update the `.slides.md` file instead.
- Vendor pattern assessments in the Appendix slide are illustrative only and are not endorsements or disqualifications of any vendor.
