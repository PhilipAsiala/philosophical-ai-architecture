"""Reference guardrail pipeline for the MOEPA dual-domain split.

Policy agents do not import or call an LLM. Callers hand in an uncommitted
candidate from whatever proposer they use.
"""

from moepa_guard.pipeline.orchestrator import GuardrailPipeline, PipelineResult

__all__ = ["GuardrailPipeline", "PipelineResult"]
