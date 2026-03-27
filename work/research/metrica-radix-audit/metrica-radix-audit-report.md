# Research Report: MétricaRadix MCP Audit for E11 Kokoro Analytics

**Date:** 2026-03-26
**Depth:** Quick scan (primary source = code)
**Decision:** Inform E11 scope and stories
**Confidence:** HIGH (all findings from primary source code)

---

## Hallazgo Principal

**Los MCP servers de MétricaRadix ya son multi-cuenta.** No hay account IDs hardcodeados. La limitación real es a nivel de credenciales, no de código:

- Las credenciales en `.env` determinan qué cuentas son visibles
- Cada servidor expone herramientas de descubrimiento (`list_ad_accounts`, `list_customers`, `get_account_summaries`, `list_properties`)
- Las queries requieren un parámetro de cuenta/propiedad — el usuario elige cuál consultar

Esto simplifica E11: **no necesitamos modificar MétricaRadix**. Kokoro Analytics necesita una capa de mapeo Cliente → Cuentas.

---

## Inventario de Servidores

| Servidor | Tools | Auth | Multi-cuenta |
|----------|:-----:|------|:------------:|
| **mcpfbads** (Facebook Ads) | 8 | System user token | Si — via Business Manager |
| **mcpgoogleads** (Google Ads) | 10 | OAuth 2.0 + dev token | Si — via MCC |
| **google-analytics-mcp** (GA4) | 7 | Application Default Credentials | Si — via ADC scope |
| **mcp-gsc** (Google Search Console) | 19 | OAuth + service account | Si — via permisos |

**Total: 44 herramientas disponibles.**

---

## Herramientas por Categoría (para Kokoro)

### Descubrimiento (listar cuentas)
| Tool | Servidor | Retorna |
|------|----------|---------|
| `list_ad_accounts()` | FB Ads | Todas las cuentas accesibles |
| `list_customers()` | Google Ads | Todos los clientes accesibles |
| `get_account_summaries()` | GA4 | Cuentas + propiedades + streams |
| `list_properties()` | GSC | Todos los sitios verificados |

### Performance (métricas de campañas)
| Tool | Servidor | Uso |
|------|----------|-----|
| `get_campaign_performance()` | FB Ads | Impressions, clicks, spend, CTR, CPC, conversions |
| `get_campaign_performance()` | Google Ads | Similar + search impression share |
| `run_report()` | GA4 | Reporting flexible (dims + metrics custom) |
| `get_search_analytics()` | GSC | Clicks, impressions, CTR, position |

### Audiencias (quién ve los anuncios)
| Tool | Servidor | Uso |
|------|----------|-----|
| `get_demographic_breakdown()` | FB Ads | Age, gender, country, device, placement |
| `get_demographic_breakdown()` | Google Ads | Age OR gender (no combinados) |
| `get_geographic_breakdown()` | Google Ads | País/región |

### Creativos y Keywords
| Tool | Servidor | Uso |
|------|----------|-----|
| `get_ad_creative_details()` | FB Ads | Título, body, imagen, CTA |
| `get_ad_details()` | Google Ads | Ad type, URLs, display URL |
| `get_keywords_performance()` | Google Ads | Quality score, match type |
| `get_search_terms()` | Google Ads | Términos de búsqueda reales |

### SEO / Indexación
| Tool | Servidor | Uso |
|------|----------|-----|
| `inspect_url_enhanced()` | GSC | Estado de indexación, canonicals, rich results |
| `batch_url_inspection()` | GSC | Inspección masiva de URLs |
| `compare_search_periods()` | GSC | Comparar periodos |

---

## Modelo de Autenticación

```
Credenciales (1 set por plataforma)
  └── Determina universo de cuentas accesibles
        └── Tool de descubrimiento lista las cuentas
              └── Usuario selecciona cuenta
                    └── Query con account_id/property_id/site_url
```

**Para multi-cliente en Kokoro:**
- Las credenciales de Eduardo ya dan acceso a todas las cuentas que administra
- Solo necesitamos un mapeo: `ClientProfile.account_ids = {fb: "act_123", gads: "456", ga4: "789", gsc: "https://..."}`
- NO necesitamos múltiples sets de credenciales (Eduardo es el admin de todas)

---

## Qué necesita E11 Kokoro Analytics

### MUST (mínimo viable)
1. **Mapeo Cliente → Cuentas** — extender `ClientProfile` con IDs de plataformas
2. **Onboarding guiado** — skill que liste cuentas disponibles y mapee al cliente
3. **`/kokoro-analytics` skill** — consultas en lenguaje natural, traducción a herramientas MCP
4. **Traducción de métricas** — CTR, CPC, ROAS explicados para no técnicos

### SHOULD (valor alto)
5. **Queries cross-platform** — "¿cómo le va a Konecta Park?" consulta FB + GA4 + GSC
6. **Scorecard semanal** — métricas clave del cliente en formato ejecutivo
7. **Detección de anomalías** — alertas simples (spend > budget, CTR drop)

### NO-GO
- No modificar código de MétricaRadix (es repositorio separado)
- No almacenar credenciales en Kokoro (usar las del entorno)
- No crear dashboards (Kokoro es conversacional, no visual)
- No automatizar cambios en campañas (solo lectura)

---

## Limitaciones Relevantes

| Limitación | Impacto en Kokoro | Mitigación |
|------------|-------------------|------------|
| Google Ads: age+gender no combinables | Reportes demográficos parciales | Dos queries separadas, combinar en presentación |
| GA4: single property per query | No agregación cross-property | Query secuencial por propiedad |
| GSC: data lag 24-48h | Métricas no son real-time | Documentar en output del skill |
| FB Ads: no paginación nativa | Límite en volumen de datos | Date bucketing para datasets grandes |
| Google Ads: 15K ops/día (Basic) | Límite de queries diarios | Caché de resultados frecuentes |

---

## Recomendación

**Confidence: HIGH**

E11 es más simple de lo que asumíamos. Los servidores MCP ya soportan multi-cuenta. El trabajo principal es:

1. Extender el modelo de cliente (`ClientProfile`) con account IDs por plataforma
2. Crear un skill `/kokoro-analytics` que traduzca consultas de negocio a llamadas MCP
3. Crear un onboarding que mapee cuentas a clientes

No se requiere research adicional. Se puede proceder directamente a `/rai-epic-design` para E11.

---

## Evidence

See `sources/evidence-catalog.md` for full source catalog with confidence ratings.
