# Reducción de cancelaciones y optimización de promociones: Proyecto Halcón Viajes

### Habilidades demostradas en este proyecto

- **Conciencia del impacto en negocio**: foco constante en la mejora de la eficiencia operativa y aumento de la retención de clientes

- **Conocimiento profundo del negocio** y enfoque estratégico: **formulación de preguntas clave** alineadas con los objetivos empresariales para transformar datos en decisiones

- **Buenas prácticas en calidad, validación y gobernanza del dato**: validación de consistencia, tratamiento de nulos y outliers, normalización y limpieza con enfoque en la integridad de la información

- **Automatización con inteligencia artificial**: uso de IA para documentar procesos, asistir en tareas repetitivas y generar código, lo que permite centrar el esfuerzo en el análisis de valor

- Mentalidad orientada a la **optimización** y al **rendimiento**: uso de funciones en python (optimización del tiempo), buenas prácticas en PowerBI y SQL (mejora del rendimiento).

- **Análisis exploratorio** de datos (EDA)

- Aplicación de **clustering (segmentación de clientes) con sklearn** para el ajuste de estrategias de marketing y personalización de ofertas

- **Diseño e implementación de una base de datos relacional en PostgreSQL**

- **Consultas SQL** orientadas al negocio

- **Visualización** y **storytelling** con Power BI

- **ETL básico y modelado de datos**

de datos a acciones de negocio: tabla acciones de negocio

Si se implementan las acciones de negocio propuestas, Halcón Viajes podría **reducir su tasa de cancelación hasta en un 10%**, gracias a la optimización de las promociones, la incentivación de la compra anticipada y la migración de clientes hacia paquetes más completos.

Además, la mejora de la experiencia en los canales de reserva, como la app móvil y los agentes de viajes, podría **aumentar la satisfacción del cliente en un 20%**, reduciendo los comentarios negativos asociados a problemas de reserva y mal servicio.
Como resultado, se espera una mejora significativa en la retención de clientes, y un fortalecimiento de la fidelización y experiencia de los viajeros.

---

## Historia del Proyecto Halcón Viajes: Cancelaciones que cuestan caro

Imagina que diriges Halcón Viajes, una empresa con una plataforma de reservas moderna y funcional. Todo parece ir bien: miles de usuarios reservan vuelos, hoteles y paquetes turísticos cada mes. Pero entonces, empiezas a notar algo inquietante… Demasiadas cancelaciones.

Y no hablamos de unas pocas. Hablamos de tasas de cancelación tan altas que afectan directamente los ingresos, la planificación y la confianza en la marca. Lo más preocupante es que nadie sabe exactamente por qué están ocurriendo, y sin esa respuesta, cualquier solución es como disparar al aire.

Ahí es donde entra este proyecto.

### ¿Qué problema real tenía Halcón Viajes?

Aunque la plataforma funcionaba correctamente, los datos mostraban que la mitad de las reservas terminaban cancelándose.
Esto no solo era una pérdida directa de ingresos, sino también un síntoma de algo más profundo: desconexión con las necesidades reales del cliente y promociones que no estaban funcionando.

### ¿Por qué estaba sucediendo esto?

Gracias a un análisis profundo, salieron a la luz patrones muy claros y valiosos:

- Las promociones no estaban sirviendo para retener clientes: la gente cancelaba igual, con o sin descuento.

- Los jóvenes y turistas eran los que más cancelaban.

- Las reservas de clase económica y de corta duración tenían una tasa de cancelación muy superior.

- Los paquetes de “solo vuelo” eran los más populares… pero también los que más se cancelaban.

- Los comentarios negativos se repetían constantemente, con quejas como “problemas con la reserva” o “no me gustó el servicio”, especialmente en la app móvil y con los agentes de viaje.

### ¿Qué soluciones propusimos?

- Optimizar la estrategia de promociones, dejando de aplicarlas en segmentos donde no funcionan y enfocándolas en reservas de alto valor y clientes más comprometidos.

- Segmentar mejor a los clientes y personalizar las ofertas según su perfil y comportamiento.

- Fomentar la conversión a paquetes más completos, como vuelo + hotel + tour, que no solo tienen menor tasa de cancelación, sino que también generan mayor valor por cliente.

- Transformar el canal de reservas, mejorando la experiencia del usuario en la app móvil y en la atención por agentes, donde se concentra el mayor número de comentarios negativos y cancelaciones.

La primera opción es la más recomendada porque es la que ofrece un impacto más inmediato, directo y medible: mejora la rentabilidad al reducir el gasto promocional en segmentos que no responden, y potencia las ventas en aquellos donde sí hay un retorno real.

### ¿Y si no implementamos estas soluciones?

Si no se aplican estas soluciones, la empresa seguirá perdiendo una parte significativa de sus ingresos potenciales. Las cancelaciones continuarán afectando la estabilidad financiera y operativa del negocio, y las promociones mal dirigidas seguirán generando costes sin retorno.

En un mercado tan competitivo como el del turismo, no actuar a tiempo significa quedarse atrás, perder clientes y desaprovechar oportunidades reales de crecimiento.

### ¿Y los beneficios si adoptamos la solución recomendada?

Ahora viene lo importante: el valor de negocio.

Si Halcón Viajes aplica estas recomendaciones, podría reducir la tasa de cancelación hasta un 10%, lo que supone proteger más de 640.000 € anuales en ingresos que ahora se están perdiendo.

Además, al optimizar la experiencia en los canales de reserva más problemáticos, la empresa podría mejorar la satisfacción del cliente en un 20%, y con ello, retener más viajeros, fidelizar más, y vender mejor.

### La oportunidad está sobre la mesa

Lo que empezó como un problema difuso de cancelaciones terminó revelando una oportunidad clara de negocio.
Y este proyecto no solo ofrece los datos que explican el problema, sino también las soluciones para resolverlo, con impacto económico directo y medible.

---

## Explicación del proceso técnico

### Herramientas utilizadas

- **Python** (Pandas, Numpy, Scikit-learn, psycopg2, matplotlib, seaborn)

- **SQL** (PostgreSQL)

- **Power BI** (Storytelling, Power Query, modelado, DAX)

- **Inteligencia artificial** (ChatGPT, algoritmos de aprendizaje)

- **GitHub** (mantenimiento en la nube)

- **Figma** (creación de plantillas para PowerBI)

- **Jupyter Notebook**

### ¿Cómo lo he hecho?

Antes de comenzar el análisis, dediqué un tiempo a **estudiar el contexto de la empresa, comprender sus necesidades reales, identificar claramente el problema y formular múltiples preguntas de negocio** orientadas a posibles soluciones. También analicé los datos disponibles para asegurarme de que respondían a esos objetivos y ofrecían el potencial necesario para extraer valor.

**Python**: Limpieza, validación, análisis exploratorio y K-means Clustering.

Para optimizar tanto el tiempo como el rendimiento del desarrollo, el código ha sido modularizado en funciones dentro de un archivo src, que se importa en los notebooks correspondientes. Esto **evita la duplicación de código y facilita su mantenimiento y reutilización.**

Comencé trabajando con Python, no solo para cargar y explorar los datos, sino para asegurarme de que todo lo que analizara fuera válido y coherente. **Validé la calidad del dataset, normalicé formatos, detecté y traté outliers según el contexto del negocio, y gestioné los valores nulos de forma inteligente**. Esto no solo garantizó integridad técnica, sino también coherencia con la realidad operativa de la empresa.

Durante el proceso de validación **detecté errores y posibles inconsistencias lógicas en la importación de datos** relacionados con las columnas temporales, por lo que realicé ajustes y correcciones justificadas para **mejorar la consistencia y calidad de los datos** para su correcto análisis.

Además, realicé un análisis exploratorio y detallado, tanto univariado como multivariado, **relacionando variables clave para detectar patrones y descubrir insights relevantes**. Estas relaciones fueron fundamentales encontrar oportunidades reales de mejora.

Por último, se implementó un **_algoritmo de aprendizaje (K-means Clustering)_**, el cual ha permitido segmentar a los clientes en grupos con características y comportamientos de compra similares, lo que ha proporcionado insights valiosos para **personalizar ofertas y ajustar estrategias de marketing basadas en el comportamiento de los clientes.**

**SQL (PostgreSQL)**:
**Diseñé un modelo relacional en PostgreSQL** que reflejara correctamente las relaciones entre las tablas del dataset. Una vez preparados y cargados los datos desde Python, comencé a realizar **consultas SQL** específicas para responder preguntas de negocio clave. Cada consulta estaba pensada para convertir información en decisiones prácticas y reproducir los principales insights del análisis exploratorio realizado previamente en Python.

**Power BI**:
En Power BI integré los datos directamente desde PostgreSQL, manteniendo la estructura relacional optimizada y evitando pasos intermedios innecesarios. **Validé los datos en Power Query, creé relaciones en el modelado y desarrollé medidas DAX personalizadas para los KPIs seleccionados, así como una tabla calendario** para el análisis temporal detallado.

Se desarrollaron cuatro dashboards principales:

- Inicio: Portada con branding corporativo y objetivos del análisis.

- Clientes: Análisis del perfil de usuario y su relación con las cancelaciones.

- Reservas: Información detallada sobre los tipos de reservas, paquetes, canales y patrones de cancelación.

- Análisis final: KPIs clave, mayores patrones de cancelación, tabla de acciones de negocio y recomendaciones estratégicas.

Se aplicó **storytelling visual** en los títulos de cada gráfico para guiar al lector, y se utilizó la paleta de colores corporativa.

Construí los dashboards con foco en:

- **Responder directamente a preguntas clave del negocio**
- **Mostrar insights claros, rápidos y accionables**
- **Aplicar principios de visualización, jerarquía visual y atributos preatentivos para destacar los puntos más críticos.**

El diseño fue previamente esbozado fuera de Power BI (Figma) para garantizar un **rendimiento óptimo y una experiencia de usuario fluida**. Incorporé **marcadores** para alternar visualizaciones y para la navegación entre páginas, **tooltips** personalizados para mostrar información contextual sin saturar el panel, y **visuales de alerta para indicadores críticos**. El resultado es un **dashboard preparado tanto para usuarios técnicos como perfiles de negocio, que facilita la toma de decisiones desde el primer vistazo.**

A lo largo de todo el proceso también integré **automatizaciones para tareas repetitivas**, desde la generación asistida de funciones en Python hasta el uso de inteligencia artificial para documentar automáticamente cada paso, lo que permitió **ahorrar tiempo y centrar los esfuerzos en descubrir oportunidades de negocio.**

Todo el desarrollo técnico de este proyecto está documentado paso a paso en mi repositorio de GitHub.
Puedes acceder al código completo aquí:
