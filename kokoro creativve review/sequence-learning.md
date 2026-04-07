# Meta Sequence Learning (Temporal Intelligence) | Master Doc 2026
**Version**: 1.0.0
**Nickname**: "The Memory Game" (El Juego de Memoria)
**Last Updated**: 2026-02-26

## Abstract
Sequence Learning is the "Memory Layer" of Meta Ads. Unlike legacy systems that see actions as isolated events, Sequence Learning analyzes the **chronological order** of user interactions to predict the logical "Next Step" in their consumer journey.

## The "Why": The Ski Resort Problem
Legacy models often showed redundant ads. If a user booked a ski resort, they would keep seeing ads for *other* ski resorts (irrelevant, money wasted). 
**Sequence Learning** recognizes the state change:
- **Action A**: Booked Resort.
- **Prediction B**: User now needs ski gear, lift tickets, or mountain-ready luggage.

## Technical Deep Dive: Chronological Embeddings
The model processes user interactions as a **Temporal Chain**:
1. **State 1**: Impression + View (Interest established).
2. **State 2**: Website Visit (Intent confirmed).
3. **State 3**: Purchase/Conversion (Need fulfilled).

### The Transformer Logic:
Using "Self-Attention" mechanisms, the system assigns weights to past actions. A purchase 5 minutes ago is weighted higher than a click from 3 months ago (Temporal Decay).

## Performance Metrics
| Metric | Improvement (vs. Legacy) |
| :--- | :--- |
| **Ad Relevance** | +30% (User perception) |
| **Conversion Waste** | -18% (Less redundant impressions) |
| **Predicted LTV** | +10% Accuracy |

## Strategic Playbook: Playing the Memory Game
1. **Vertical Ad Sequencing**: Ensure your creatives follow a logical flow (Hook -> Education -> Objection Handling -> Offer).
2. **Dynamic Retargeting 2.0**: Don't just show the same product viewed. Show the **Complementary Product** (Upsell/Cross-sell) that Sequence Learning predicts is the next logical need.
3. **Lifecycle Content**: Create content for the "Post-Purchase" state. Sequence Learning will prioritize these users for "Product Aware" or "Decisión" hooks that add value to their recent purchase.

## Ecosystem Integration
- **GEM**: Provides the foundational intent predictions that Sequence Learning refines chronologically.
- **Andromeda**: Retrieval clusters are updated in real-time based on the user's latest "Sequence State."
- **Lattice**: Unifies sequential data across all platforms (WhatsApp, IG, FB) to ensure the memory is ecosystem-wide.
