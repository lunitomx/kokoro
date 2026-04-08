---
epic_id: "E32"
title: "Kokoro Landing — Auditoria estrategica de landing pages bajo Lean Landing Page"
status: "Scoped"
---

# Brief: E32 — Kokoro Landing

## Hypothesis

Los emprendedores construyen landing pages que "se ven bien" pero no convierten
leads calificados. Esto pasa porque disenan desde la estetica (brochure, blog,
pagina institucional) en lugar de disenar una secuencia de decision.

Eduardo creo la metodologia Lean Landing Page — un sistema de 9 bloques ordenados
como flujo de decision, gobernado por 5 principios fundamentales. Hoy esa
metodologia existe como PDF y como clase grabada, pero no existe como herramienta
ejecutable dentro de Kokoro.

Un skill que lea una landing page real (URL o HTML), la mapee contra los 9 bloques
y la evalue contra los 5 principios le dara al emprendedor un diagnostico
accionable: que tiene, que le falta, que esta en desorden, y como deberia sonar
cada seccion — en la voz de Eduardo.

La frase que gobierna todo: **"No busca convencer, busca calificar."**

## Success Metrics

- El skill recibe una URL o HTML y genera un analisis estructurado
- Mapea secciones existentes contra los 9 bloques del esqueleto Lean Landing Page
- Evalua cada bloque contra sus reglas de oro (copy especifico vs slogan, dolor
  reflejado vs explicado, filtro presente vs ausente, etc.)
- Scorecard contra los 5 principios con criterios verificables
- Sugiere rewrites concretos en voz Eduardo (vocabulario luxurizante)
- Knowledge file documenta la metodologia completa como referencia
- Se integra con /kokoro-audit para el diagnostico tecnico complementario

## Appetite

Medium — 1 skill command + 1-2 knowledge files + integracion con kokoro-audit.
Fuente primaria: PDF Lean Landing Page v2.0 + transcripcion de clase (sesion 56).
Estimado: 1-2 sesiones.

## Rabbit Holes

- No construir/generar landing pages — eso es /kokoro-launch
- No duplicar el audit tecnico — /kokoro-audit ya lo hace (SEO, performance, a11y)
- No evaluar diseno visual (colores, tipografia, layout) — el skill evalua
  estructura de decision y copy
- No pretender medir conversion real — las metricas (25% conversion, 90% ICP match)
  son benchmarks de referencia, no predicciones
- No hacer scraping complejo de SPAs — si el fetch no captura contenido, pedir HTML
