# Problem Brief: Kokoro MCP Server para Claude Desktop

## Problem Statement

Kokoro actualmente requiere instalación técnica: `pip install kokoro` + `kokoro init`
en un directorio de proyecto. Esto limita el acceso a personas con conocimiento
técnico (developers, DevOps). Los emprendedores y estudiantes que más necesitan
la herramienta no pueden acceder a ella sin ayuda técnica.

Claude Desktop soporta MCP (Model Context Protocol) servers que permiten conectar
herramientas externas sin instalación de paquetes. Un estudiante o emprendedor
podría conectarse a Kokoro desde Claude Desktop con solo agregar una línea en su
configuración — sin terminal, sin pip, sin git.

## Who Has This Problem

- **Estudiantes de Eduardo** — quieren usar la metodología pero no son técnicos
- **Emprendedores no-técnicos** — su fuerte es el negocio, no la terminal
- **Eduardo como educador** — quiere distribuir Kokoro a 100+ estudiantes sin
  soporte técnico individual
- **El proyecto Kokoro** — sin distribución masiva, el impacto queda limitado
  a un puñado de developers

## Evidence

1. Claude Desktop MCP es el canal de distribución más accesible para herramientas
   AI — configuración de 1 línea vs proceso de instalación de 5 pasos
2. La metodología completa ya existe como markdown — convertir skills a MCP tools
   es un ejercicio de wrapping, no de reescritura
3. La ontología (E3) ya define persistencia vía JSON — MCP resources pueden
   exponer el estado del coaching como contexto legible

## What This Is NOT

- **No es una reescritura de Kokoro** — los skills siguen siendo markdown, el MCP
  server los expone como tools
- **No es un backend web** — es un proceso local que corre en la máquina del
  emprendedor, servido por Claude Desktop
- **No es un SaaS** — no hay autenticación, multi-tenancy, ni cloud. Local-first
- **No requiere Claude Code** — el emprendedor usa Claude Desktop, no la CLI

## Success Criteria

1. Un emprendedor agrega Kokoro MCP a su Claude Desktop config y tiene acceso a
   los 10 skills (8 coaching + 2 meta) sin instalar nada más
2. El estado de coaching persiste en `.kokoro/state.json` igual que con la
   extensión CLI
3. Los skills funcionan idéntico en MCP que en Claude Code — misma voz, mismos
   ejercicios, misma persistencia
4. Eduardo puede distribuir la configuración a sus estudiantes con instrucciones
   de 3 pasos o menos

## Risks & Unknowns

- **MCP tool vs MCP resource**: ¿los skills son tools (ejecutables) o resources
  (contexto legible)? Probablemente tools para coaching interactivo
- **State persistence path**: ¿dónde guarda state.json si no hay "proyecto"?
  Opción: `~/Documents/kokoro/` o configurable
- **Knowledge files**: ¿cómo se sirven los archivos .md de conocimiento?
  Como resources MCP o embebidos en el tool
- **Package distribution**: ¿uvx, npx, o docker? uvx es el estándar RaiSE
- **Claude Desktop limitations**: verificar qué version de MCP soporta,
  límites de context, tool calling

## Estimated Complexity

**M (Medium)** — Rationale:
- Los skills ya existen como markdown (no hay contenido nuevo)
- La ontología/store ya existe (E3)
- El trabajo es wrapping: exponer lo que existe como MCP tools/resources
- Requiere MCP SDK knowledge (Python) pero el pattern es conocido en RaiSE
- Estimado 4-6 stories
