# Meta Andromeda (Ads Retrieval System) | Master Doc 2026
**Version**: 1.5.0 (Global Rollout Oct 2025)
**Last Updated**: 2026-02-26

## Abstract
Meta Andromeda is the **"Personal Counselor"** (Consejero Personal) of the ads system. It replaces legacy heuristic-based filtering with a **GPU-accelerated retrieval engine**. It knows your tastes so well it predicts the exact "version" of a product you want (e.g., Red Flip-flops vs. generic sandals).

## The "Why": The Inventory Explosion
In 2020, Meta managed ~50k active ads per auction request. By 2026, this exceeded 10 million. Legacy systems (CPU-based) couldn't scale without sacrificing "Relevance Quality". Andromeda solves this by:
- **10,000x Model Capacity**: Modeling more complex interactions between user behavior and ad features.
- **Sub-linear Scaling**: Using hierarchical indexing O(log n) to scan millions of ads at constant speed.
- **GPU-Accelerated Inference**: Moving feature extraction from CPU to GPU (100x speed increase).

## Hardware-Software Synergy
Andromeda runs on Meta's specialized AI hardware:
- **NVIDIA Grace Hopper Superchip**: 900GB/s CPU-GPU bandwidth for ultra-fast embedding transfers.
- **Unified Coherent Memory**: Shared memory space for real-time retrieval scoring.
- **Meta MTIA v2**: Specialized inference accelerators that reduce dependency on external GPUs and enhance efficiency by 10x.

## Technical Deep Dive: 4-Layer Hierarchical Indexing
Retrieval is optimized via a multi-layer organizational structure:

1. **Layer 1: Super-categories** (e.g., E-commerce vs. Services).
2. **Layer 2: Categories** (e.g., Luxury Real Estate).
3. **Layer 3: Sub-categories** (e.g., Pre-construction condos).
4. **Layer 4: Ad Clusters** (Visually/conceptually similar ads).

**Mechanism**: The system navigates this tree in O(log n) time, selecting the clusters most relevant to the user's **Sequence Embedding** (provided by GEM).

## Performance Metrics (Global Rollout Data)
| Metric | Improvement (vs. Legacy) |
| :--- | :--- |
| **Recall Accuracy** | +6% |
| **Ads Quality Score** | +8% |
| **Feature Extraction Speed** | 100x Faster |
| **Inference Efficiency** | 10x Higher (Model Elasticity) |
| **ROAS (Advantage+Users)** | +22% |

> [!IMPORTANT]
> **The Diversification Unlock**: Results with Andromeda drop exponentially if creatives are repetitive. The engine requires "Creative Diversification" to navigate the 4-layer Hierarchical Index effectively.

## Strategic Playbook: Scaling with Andromeda
1. **Maximize Entity ID Diversity**: This is the #1 lever for Andromeda. Since the system scans millions of ads, having 8-15+ unique concepts (different hooks/visuals) provides the engine a wider **"Field of Action"**.
2. **The Creative Matrix**: Use the **16 Human Desires** and **5 Levels of Awareness** to ensure your ads are distributed across different clusters in the Hierarchical Index.
3. **Broad Targeting is Mandatory**: Manual targeting limits Andromeda's ability to explore the index.
4. **GPU-Friendly Content**: High-resolution, vertically-optimized video content (9:16) has higher feature density for the neural networks to process.
5. **Model Elasticity Awareness**: High-value/High-bid segments receive more "Inference effort" from Andromeda. Premium brands should use high-quality assets to match this allocation.

## Ecosystem Integration
- **GEM (The Intelligence)**: Provides the Sequence Learning embeddings that serve as the "Input Query" for Andromeda's retrieval.
- **MTIA Inference**: The underlying chip-level execution layer for all retrieval operations.
