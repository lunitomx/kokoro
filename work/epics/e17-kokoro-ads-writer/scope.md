---
epic_id: "E17"
title: "Kokoro Ads Writer — Subir creativos a Meta Ads"
status: "designed"
---

# Scope: E17 — Kokoro Ads Writer

## Objective

Permitir que Kokoro suba creativos (imagenes, titulos, textos) directamente
a una campana especifica de Meta Ads. No toca presupuestos, no pausa/activa
campanas, no modifica targeting. Solo sube contenido creativo.

## Value

- Eduardo deja de copiar/pegar manualmente entre Kokoro y Meta Ads Manager
- El flujo /kokoro-creative → /kokoro-ads → /kokoro-publish es end-to-end
- Reduce errores de copy/paste (acentos, caracteres especiales)

## Architecture Decisions

### AD-1: Solo escritura de creativos (NUNCA presupuesto)

El scope de escritura esta HARDCODEADO en el skill: solo crea/actualiza
ad creatives y ad copies. Las operaciones de budget, status, y targeting
estan explicitamente prohibidas en el codigo.

Rationale: Proteccion contra errores costosos. Cambiar un presupuesto de
$50 a $5,000 es irreversible. Subir un copy mal escrito se corrige en
segundos.

### AD-2: Confirmacion obligatoria antes de publicar

Cada operacion de escritura muestra EXACTAMENTE que se va a publicar y
requiere confirmacion explicita del usuario antes de ejecutar.

Rationale: Meta Ads es dinero real. Doble confirmacion es el minimo.

### AD-3: Usar el MCP de Facebook Ads existente (extender, no reemplazar)

Agregar tools de escritura al MCP server de facebook-ads que ya existe
en MetricaRadix. No crear un MCP server nuevo.

Rationale: El server ya tiene la autenticacion, la conexion, y los
permisos. Solo falta agregar @mcp.tool() para las operaciones de
escritura.

### AD-4: Verificar permisos de API antes de escribir

El token actual puede tener solo `ads_read`. Verificar scope del token
y pedir reautorizacion si falta `ads_management`.

## Stories

- [ ] S17.1 — Verificar y obtener permisos de escritura en Facebook API (S)
- [ ] S17.2 — Tools de escritura en MCP facebook-ads: create_ad_creative, update_ad_text (M)
- [ ] S17.3 — /kokoro-publish: skill que toma output de kokoro-ads/creative y lo sube a Meta (S)
- [ ] S17.4 — Gate de confirmacion: preview + doble confirmacion antes de publicar (S)

## Story Details

### S17.1 — Permisos de escritura (S)

Verificar que el token de Facebook tiene scope `ads_management`.
Si solo tiene `ads_read`:
1. Documentar como re-autorizar con el scope correcto
2. Actualizar el .env de MetricaRadix

**Dependencies:** None
**Size:** S

### S17.2 — Tools de escritura en MCP (M)

Agregar al server `mcpfbads/src/server.py` de MetricaRadix:

1. `create_ad_creative(account_id, name, image_url, title, body, link_url)`
   — Crea un AdCreative nuevo
2. `update_ad_creative_text(creative_id, title, body)`
   — Actualiza titulo y texto de un creativo existente
3. `upload_ad_image(account_id, image_path)`
   — Sube una imagen y retorna el image_hash

NO agregar:
- update_budget (PROHIBIDO)
- update_campaign_status (PROHIBIDO)
- create_campaign (PROHIBIDO)
- update_targeting (PROHIBIDO)

Cada tool debe tener un docstring que diga "WRITE OPERATION" para
que sea visible en la lista de tools.

**Dependencies:** S17.1
**Size:** M (requiere trabajo en MetricaRadix, no en RaizAncestral)

### S17.3 — /kokoro-publish (S)

Skill que:
1. Lee el ultimo creativo generado por /kokoro-ads o /kokoro-creative
2. Pregunta a que campana/ad set publicar
3. Muestra preview de lo que se va a publicar
4. Con confirmacion, llama a los MCP tools de escritura
5. Confirma que se publico correctamente

**Dependencies:** S17.2
**Size:** S

### S17.4 — Gate de confirmacion (S)

Antes de cualquier operacion de escritura:
1. Mostrar preview exacto: imagen, titulo, texto, CTA
2. Mostrar destino: cuenta, campana, ad set
3. Pedir confirmacion explicita: "¿Publico esto? (si/no)"
4. Solo ejecutar con "si" explicito

**Dependencies:** S17.3
**Size:** S

## Dependency Graph

```
S17.1 (permisos) ──> S17.2 (MCP tools) ──> S17.3 (/kokoro-publish) ──> S17.4 (gate)
```

Lineal.

## Scope Boundaries

### In (MUST)
- Subir imagenes a Meta Ads
- Crear/actualizar titulos y textos de anuncios
- Gate de confirmacion obligatorio
- Preview antes de publicar

### In (SHOULD)
- Subir multiples variantes de un creativo (A/B test)

### No-Gos (HARDCODED — no negociable)
- NUNCA tocar presupuesto (daily_budget, lifetime_budget)
- NUNCA pausar/activar campanas o ad sets
- NUNCA modificar targeting o audiencias
- NUNCA crear campanas nuevas (solo creativos dentro de existentes)
- NUNCA eliminar anuncios

### Rabbit Holes
- Dashboard de rendimiento post-publicacion (ya existe en E11)
- Automatizar A/B testing (prematuro)
- Programar publicacion en horarios especificos (Meta ya lo hace)

## Done Criteria

- [ ] Token con permisos de escritura configurado
- [ ] MCP tools crean/actualizan creativos correctamente
- [ ] /kokoro-publish sube imagen + copy a una campana especifica
- [ ] Gate de confirmacion funcional (preview + doble check)
- [ ] Prohibiciones de budget/status hardcodeadas y verificadas

## Risks

1. **Error en publicacion** — Mitigation: gate de confirmacion + preview obligatorio
2. **Token sin permisos** — Mitigation: S17.1 verifica primero
3. **Meta API cambia** — Mitigation: usar SDK oficial (facebook_business) que se mantiene actualizado
