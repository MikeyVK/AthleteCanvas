<!-- docs\adr\0001-use-litellm-as-provider-agnostic-ai-layer.md -->
<!-- template=adr version=b4627a40 created=2026-07-22T20:27Z updated= -->
# 0001: Use LiteLLM as Provider-Agnostic AI Layer

**Status:** ACCEPTED  
**Version:** 1.0.0  
**Last Updated:** 2026-07-22  
**Supersedes:** None  
**Superseded By:** None  
**Deciders:** MikeyVK, Antigravity Agent  

---

## Context & Problem Statement

ypsia requires an AI Layer that supports LiteLLM provider abstraction (Gemini primary, BYOK model), streaming responses, and user-controlled prompt filtering without vendor lock-in.

### Decision Drivers

- BYOK (Bring Your Own Key) model
- Streaming UI responses
- Provider-agnostic interface
- Strict data privacy filtering

---

## Considered Options

### Option 1: LiteLLM Adapter Layer (Chosen)

Wrap LiteLLM client behind an internal AIProvider interface.

**Pros (+):**
- Supports 100+ LLM providers out of the box
- Unified streaming response API
- Easy BYOK configuration

**Cons (-):**
- Adds LiteLLM dependency
- Requires adapter unit tests

### Option 2: Direct Google Gemini SDK

Directly call google-generativeai SDK.

**Pros (+):**
- Direct first-party SDK features
- Zero extra abstraction wrappers

**Cons (-):**
- Vendor lock-in to Google Gemini
- Difficult for users to switch to OpenAI or Anthropic (breaks BYOK strategy)


---

## Decision Outcome

**Chosen Option:** Option 1: LiteLLM Adapter Layer

### Rationale

LiteLLM satisfies the BYOK core requirement and prevents vendor lock-in, enabling ypsia users to choose their preferred provider while keeping Gemini as default.

---

## Consequences

### Positive Consequences (+)

- Provider independence across backend services.
- Unified streaming response handlers.

### Negative Consequences & Risks (-)

- Slight overhead of maintaining LiteLLM adapter interfaces.

### Agent Implementation Guardrails

- Agents MUST NOT write direct import statements for google.generativeai or openai SDKs outside the LiteLLM adapter layer.
- Agents MUST route all LLM invocation calls through the LiteLLM adapter interface.
- Any direct API key exposure in client code is a strict violation of this ADR.


---

## Confirmation & Verification

Verified via unit tests in tests/unit/ai/test_litellm_adapter.py and quality gates.

## Related Documentation
None
---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-22 | Agent | Initial draft |