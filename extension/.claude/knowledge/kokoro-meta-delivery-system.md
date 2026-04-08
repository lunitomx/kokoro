# Sistema de Delivery de Meta Ads — Referencia para /kokoro-ads

> "El algoritmo no es tu enemigo — es un aprendiz que necesita tiempo.
> Apagar un ad en exploracion es como arrancar una semilla el segundo dia
> porque todavia no da frutos."
> — Eduardo Munoz Luna

## Filosofia del Sistema

El emprendedor que entiende como Meta entrega sus ads tiene una ventaja
competitiva invisible: paciencia estrategica. Mientras otros apagan campanas
al tercer dia porque "no funcionan", el emprendedor informado sabe que el
sistema todavia esta aprendiendo — y que apagar en ese momento es lo peor
que puede hacer.

Meta no muestra tu ad a personas aleatorias. Cuatro sistemas de inteligencia
artificial trabajan simultaneamente para encontrar a las personas correctas
(ver `kokoro-meta-ai-ecosystem.md` para descripcion completa de cada sistema).
Pero esos sistemas necesitan datos para aprender. Y los datos requieren
tiempo e inversion.

La metafora agricola aplica con precision: sembrar no es lo mismo que
cosechar. El emprendedor que invierte $500 MXN y espera conversiones en
48 horas esta confundiendo exploracion con optimizacion. Son fases
fundamentalmente diferentes — y cada una tiene sus propias reglas.

**Principio central:** Nunca tomes decisiones de on/off basandote en datos
de exploracion. Es como juzgar la cosecha mirando la tierra recien sembrada.

---

## Las 3 Fases del Ad Delivery

Cada ad set que lanzas atraviesa tres fases secuenciales. La fase en la que
te encuentras determina que acciones son validas y cuales son destructivas.

---

### Fase 1 — Exploracion (Dias 1-3)

**Que esta pasando dentro de Meta:**

El sistema esta mapeando tu creativo a clusters de audiencia. Andromeda
escanea 10+ millones de ads por subasta para encontrar donde encaja el tuyo
dentro de su indice jerarquico de 4 niveles. GEM tiene cero signal de
conversion — literalmente no sabe quien va a responder a tu ad. Lattice
esta probando superficies (Feed, Reels, Stories) sin datos historicos.

Los dias 1-2 son "ruido caro" — el sistema esta invirtiendo inference
computacional para mapear tu creativo a los clusters correctos. Los CPAs
de estos dias NO son indicativos de rendimiento futuro.

**Lo que ves en el dashboard:**

- CPAs erraticos (pueden ser 5x o 10x tu target)
- Impresiones bajas (<500)
- CTR inestable
- Posiblemente cero conversiones

**Lo que debes hacer:** NADA. Absolutamente nada. No toques presupuesto,
no cambies copy, no pauses. Cada cambio reinicia el proceso.

**Lo que nunca debes hacer:** Tomar decisiones basadas en estos numeros.
Son ruido estadistico, no signal.

---

### Fase 2 — Learning (Dias 3-14)

**Que esta pasando dentro de Meta:**

GEM esta construyendo modelos de probabilidad de conversion basados en las
primeras interacciones. Andromeda tiene clusters iniciales pero necesita
volumen para refinar. Lattice esta identificando que superficies funcionan
mejor para tu creativo especifico. Sequence Learning esta comenzando a
mapear el journey temporal de tus visitantes.

El target de Meta es claro: **50 eventos de optimizacion en 7 dias** para
salir de learning phase. Para campanas de Purchase o Mobile App Install,
el threshold reducido es **10 conversiones en 3 dias**.

**Lo que ves en el dashboard:**

- CPAs comenzando a estabilizarse (pero aun con variacion)
- Impresiones creciendo (500-2000+)
- Patrones emergentes en horarios y placements
- Posiblemente algunas conversiones

**Lo que debes hacer:** Monitorear sin intervenir. La unica excepcion es
el hard kill threshold (ver Matriz de Decision). Si despues de invertir
3x tu CPA target no tienes una sola conversion, hay un reto fundamental
que el algoritmo no va a resolver.

**Lo que nunca debes hacer:** Cambios de presupuesto >20%, cambios de
targeting, cambios de evento de optimizacion. Cualquiera de estos reinicia
el learning completo.

---

### Fase 3 — Optimizacion (Dia 14+)

**Que esta pasando dentro de Meta:**

GEM tiene predicciones calibradas. Andromeda tiene asignaciones estables de
clusters. Lattice sabe exactamente que superficie funciona para cada
segmento de tu audiencia. Sequence Learning tiene suficiente historia
temporal para predecir el siguiente paso logico del journey.

Para campanas de alto volumen (>50 conversiones/semana), la optimizacion
es efectiva desde el dia 14. Para volumen medio (10-50 conversiones/semana),
el sistema necesita hasta el dia 21 para calibrarse completamente.

**Lo que ves en el dashboard:**

- CPAs estables y predecibles
- Patrones claros de rendimiento por placement
- Conversion rate consistente
- Datos suficientes para decisiones informadas

**Lo que debes hacer:** AHORA si puedes evaluar con justicia. Compara
contra tu CPA target. Optimiza lo que funciona, pausa lo que no. Pero
hazlo con datos de optimizacion, no con datos de exploracion.

**Lo que nunca debes hacer:** Relajarte. Creative fatigue llega cuando
la frecuencia supera 3.0. Monitorea el diversity score — el target es
60%+ de diversidad dentro de las primeras 4 semanas.
