# Epic Brief — E34 Kokoro Skill Diet

## Hypothesis

Si reducimos el peso cognitivo de los skills de Kokoro moviendo instrucciones
repetidas a un knowledge compartido y reorganizando la estructura de cada skill,
Claude dejará de saltarse pasos y ejecutará los flujos con mayor confiabilidad.

## Success Metrics

1. **Tamaño promedio de skill reducido en >20%** — de 1,157 palabras a <925
2. **Cero instrucciones duplicadas** — vocabulario, voz, persistencia, resolución
   de invitado aparecen en UN solo lugar
3. **Calidad preservada** — todas las instrucciones siguen accesibles, ningún
   skill pierde capacidad. La poda mueve, no elimina.
4. **Skills más grandes bajo 1,500 palabras** — hoy el mayor tiene 2,234

## Appetite

**Tamaño:** Medium (4 stories)
**Tiempo estimado:** 2-3 sesiones

## Rabbit Holes

- NO cambiar la lógica de ningún skill — solo mover texto repetido
- NO crear abstracciones nuevas (MCP, pipeline engine) — eso es E35/E36
- NO podar instrucciones específicas del dominio del skill (ej: los pasos
  de kokoro-ads son únicos y se quedan)
- Cuidado con podar instrucciones que parecen repetidas pero tienen matices
  por skill — verificar antes de mover
- El knowledge compartido NO debe ser tan grande que inflé el contexto por
  sí mismo — debe ser más chico que la suma de lo que reemplaza

## Constraint

**Regla de oro:** Podar peso, no poder. Cada instrucción que se mueve tiene
que seguir siendo accesible al skill que la necesita. Si un skill pierde
calidad de output después de la poda, revertir.
