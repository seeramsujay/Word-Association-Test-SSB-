# SSB WAT: Architectural Review & Psychometric Engineering Roadmap (future.md)

---

## 1. Architectural Code Review & Current State Analysis

The SSB Word Association Test (WAT) Immersive Simulator is a desktop training utility engineered with **Python & Pygame** to reproduce the high-stress psychological testing conditions of the Indian Armed Forces Services Selection Board (SSB). Candidates are presented with 60 words for 15 seconds each and must spontaneously record constructive, action-oriented responses without conscious filtering.

### Architectural Strengths
- **Aspect-Ratio Sensitive Font Scaling:** Dynamically scales typography according to monitor resolution (`SCALE_FACTOR = min(W/1024, H/768)`), preventing distortion across diverse display hardware.
- **Programmatic Audio Synthesis Fallback:** If `bell.wav` is missing, generates a mathematical triangle-wave audio buffer using `pygame.sndarray` and volume envelopes, ensuring zero hard crashes.
- **Sub-Millisecond Clock Deltas:** Uses physical timestamp differences (`time.time()`) rather than frame ticks to prevent timer slowdown during rendering stalls.

### Identified Bottlenecks & Modernization Needs
1. **Desktop Pygame Barrier:** Running as a native Python desktop script requires local Python and Pygame setup, limiting reach on mobile devices and Chromebooks.
2. **Absence of Evaluative Feedback:** Candidates currently write responses on physical paper; there is no automated analysis of word polarity, defense mechanisms, or Officer Like Qualities (OLQs).
3. **Flat-File Concurrency:** In-place line mutation of `wat.csv` can encounter file-lock conflicts if accessed across multiple processes.

---

## 2. Strategic Engineering Roadmap

```mermaid
flowchart TD
    subgraph Phase 1: WebAssembly (Wasm) Pygame Browser Port
        P1A[Pygbag WebAssembly Compilation] --> P1B[Zero-Install Browser Execution]
        P1B --> P1C[Mobile Responsive Canvas Scaling]
    end

    subgraph Phase 2: Speech-to-Text & Voice Response Engine
        P2A[Web Speech API / Local Whisper Ingestion] --> P2B[Spoken Sentence Transcription]
        P2B --> P2C[Reaction Time Latency Analyzer]
    end

    subgraph Phase 3: AI Officer Like Quality (OLQ) Evaluation
        P3A[Semantic Polarity & Determinism Scorer] --> P3B[15 Officer Like Quality (OLQ) Matrix]
        P3B --> P3C[Automated Psychological Psychodiagnostic Report]
    end

    subgraph Phase 4: Full Psychological Battery Integration
        P4A[TAT: Thematic Apperception Test Slides] --> P4B[SRT: Situation Reaction Test Prompts]
        P4B --> P4C[Unified SSB Psychology Dossier Generator]
    end

    Phase 1 --> Phase 2
    Phase 2 --> Phase 3
    Phase 3 --> Phase 4
```

---

## 3. Detailed Milestone Execution Plan

### Milestone 1: Zero-Install Web Port via Pygbag (WebAssembly)
- [ ] **Pygbag Web Build:** Compile `wat.py` to WebAssembly using Pygbag to run directly in modern browsers without installing Python.
- [ ] **Touch Gesture Controls:** Add touch tap controls (tap right half to advance, double-tap to pause) for mobile and tablet browsers.

### Milestone 2: Speech-to-Text Voice Mode & Latency Metrics
- [ ] **Real-Time Voice Dictation:** Allow candidates to speak their responses aloud under time pressure, transcribing audio in real time.
- [ ] **Hesitation & Latency Tracking:** Measure the elapsed time between word presentation and the candidate's first spoken syllable to quantify cognitive hesitation.

### Milestone 3: AI Psychometric Assessment & OLQ Scoring
- [ ] **Officer Like Quality (OLQ) Mapping:** Analyze candidate responses across the 15 standard OLQs (Effective Intelligence, Reasoning Ability, Organizing Ability, Power of Expression, Social Adaptability, Cooperation, Sense of Responsibility, Initiative, Self-Confidence, Speed of Decision, Ability to Influence, Liveliness, Determination, Courage, Stamina).
- [ ] **Passive/Avoidant Clause Detection:** Flag sentences that express escapism, passive observations (e.g. "Sun rises in the east"), or negative denial rather than decisive personal agency.

### Milestone 4: Comprehensive Psychological Suite (TAT + SRT + SDT)
- [ ] **Thematic Apperception Test (TAT):** Timed 30-second image projection followed by a 4-minute story writing module.
- [ ] **Situation Reaction Test (SRT):** Interactive prompt solver with 60 situational dilemmas in 30 minutes.
- [ ] **Exportable PDF Report:** Generate a comprehensive psychological appraisal PDF highlighting areas for cognitive reframing.
