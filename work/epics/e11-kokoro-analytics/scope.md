---
epic_id: "E11"
title: "Kokoro Analytics — MCP multi-cuenta"
status: "designed"
---

# Scope: E11 — Kokoro Analytics

## Objective

Conectar los 4 MCP servers de MétricaRadix (Meta Ads, Google Ads, GA4,
Search Console) con Kokoro para que Eduardo consulte métricas de cualquier
cliente en lenguaje natural, sin conocimiento técnico.

## Research Findings (2026-03-26)

Los MCP servers ya son multi-cuenta — 44 herramientas, sin IDs hardcodeados.
La limitación es de credenciales, no de código. No hay que modificar MétricaRadix.
Reporte completo: `work/research/metrica-radix-audit/metrica-radix-audit-report.md`

## Architecture Decision

Mapeo Cliente → Cuentas via `ClientProfile.metadata["platform_accounts"]`.
Sin nuevo modelo — el campo `metadata: dict[str, Any]` ya existe para extensiones.

```python
metadata = {
    "platform_accounts": {
        "meta_ads": "act_123456",
        "google_ads": "1234567890",
        "ga4": "properties/123456",
        "gsc": "https://example.com"
    }
}
```

## Stories

- [ ] S11.1 — MCP registration: registrar mcpfbads y mcpgoogleads en Claude Code (XS)
- [ ] S11.2 — /kokoro-connect: onboarding guiado para mapear cuentas a clientes (S, dep: S11.1)
- [ ] S11.3 — /kokoro-analytics: consultas de métricas en lenguaje natural (M, dep: S11.1)
- [ ] S11.4 — Traducción de métricas: knowledge file técnico → negocio (S, dep: S11.3)
- [ ] S11.5 — Scorecard cross-platform: vista unificada por cliente (S, dep: S11.3)

## Scope Boundaries

### In (MUST)
- Los 4 MCP servers accesibles desde Kokoro
- /kokoro-connect para mapear cuentas a clientes
- /kokoro-analytics para consultar métricas en lenguaje natural
- Métricas traducidas a lenguaje de emprendedor
- Integración con client graph (E9)

### In (SHOULD)
- Scorecard cross-platform
- Comparación entre períodos
- Detección simple de anomalías

### No-Gos
- No modificar código de MétricaRadix
- No almacenar credenciales en el repo
- No dashboards web — todo conversacional
- No automatizar cambios en campañas (solo lectura)

### Rabbit Holes
- Construir un Data Studio — solo consultas puntuales
- Real-time streaming — batch queries son suficientes
- Campaign optimization automática — otro nivel

## Done Criteria
- [ ] 4 MCP servers accesibles desde Claude Code
- [ ] /kokoro-connect mapea cuentas a clientes
- [ ] /kokoro-analytics responde "¿cómo le va a [cliente]?"
- [ ] Métricas en lenguaje de emprendedor
- [ ] Tests pasan

## Risks
1. MCP servers no arrancando → S11.1 valida conectividad primero
2. Credenciales expiradas → documentar renovación en onboarding
3. 44 tools demasiado para un skill → filtrar a ~10 más útiles

## Implementation Plan

### Sequence

| # | Story | Size | Rationale | Enables |
|:-:|-------|:----:|-----------|---------|
| 1 | S11.1 — MCP registration | XS | Risk-first: valida que servers arrancan | Todo lo demás |
| 2 | S11.2 — /kokoro-connect | S | Walking skeleton: onboarding → mapeo | E14 (Konecta Park) |
| 3 | S11.3 — /kokoro-analytics | M | Core value: consultas en lenguaje natural | S11.4, S11.5 |
| 4 | S11.4 — Traducción métricas | S | Usabilidad: CTR → "de cada 100 personas..." | S11.5 |
| 5 | S11.5 — Scorecard cross-platform | S | Vista unificada: todas las plataformas | E14 |

### Parallel Opportunities

S11.2 y S11.3 pueden ejecutarse en paralelo después de S11.1:
- S11.2 toca: skill file + client graph (models.py, store.py)
- S11.3 toca: skill file + knowledge file (MCP tools reference)
- Sin colisión de archivos

### Milestones

- [ ] **M1: MCP Live** (S11.1) — Los 4 servers responden desde Claude Code
- [ ] **M2: Core MVP** (S11.2 + S11.3) — Conectar cliente + consultar métricas
- [ ] **M3: Epic Complete** (S11.4 + S11.5) — Traducción + scorecard → `/rai-epic-close`

### Progress Tracking

| Story | Status | Tests |
|-------|:------:|:-----:|
| S11.1 — MCP registration | pending | — |
| S11.2 — /kokoro-connect | pending | — |
| S11.3 — /kokoro-analytics | pending | — |
| S11.4 — Traducción métricas | pending | — |
| S11.5 — Scorecard cross-platform | pending | — |

### Sequencing Risks

1. MCP servers no instalados/configurados → S11.1 falla early, blocker visible
2. S11.2 y S11.3 en paralelo podrían tocar test_output_structure.py → resolver en merge
3. Credenciales de MétricaRadix expiradas → documentar en S11.2 onboarding

## External Dependencies
- MétricaRadix: /Users/soyahuehuetedigital/Documents/MétricaRadix
- MCP servers ya registrados: google-analytics, google-search-console
- MCP servers por registrar: mcpfbads, mcpgoogleads
