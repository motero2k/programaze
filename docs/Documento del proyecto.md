# Documento del proyecto
## Indicadores del proyecto

| Miembro del equipo                | Horas | Commits | LoC Github | LoC Git fame | Test | Issues | Incremento          |
|-----------------------------------|-------|---------|------------|------------|------|--------|---------------------|
| Casal Ferrero, Rubén              | HH    | XX      | YY         | YY         | ZZ   | II     | Descripción breve  |
| Domínguez Ruiz, Andrés            | HH    | XX      | YY         | YY         | ZZ   | II     | Descripción breve  |
| Fernández Castillo, Javier        | HH    | XX      | YY         | YY         | ZZ   | II     | Descripción breve  |
| Montero Martínez, Francisco Jesús | HH    | XX      | YY         | YY         | ZZ   | II     | Descripción breve  |
| Otero Barbasán, Manuel            | HH    | XX      | YY         | YY         | ZZ   | II     | Descripción breve  |
| **TOTAL**                         | tHH   | tXX     | tYY        | YY         | tZZ  | tII    | Descripción breve  |

- Horas: número de horas empleadas en el proyecto
- Commits: Commits realizados
- LoC Github (líneas de código): Líneas de código en Insights de Github
- LoC Git fame (líneas de código): Líneas de código proporcioandas por Git fame
- Test: Tests realizados durante el proyecto
- Issues: issues gestionadas dentro del proyecto y que hayan sido gestionadas por el equipo
- Incremento: principal incremento funcional del que se ha hecho cargo el miembro del proyecto
---

## Integración con otros equipos

Este apartado no aplica para este proyecto. Se trata de un proyecto de innosoft. Debido a ser el único grupo que escogió esta modalidad no se ha tenido la oportunidad de hacerlo.  Aún así, hemos tenido que adaptarnos al planteamiento propuesto por el tutor (David Romero Organvídez), ya que partimos desde el planteamiento de su estructura 
de datos y el estado en el que se encontraba su [repositorio](https://github.com/drorganvidez/evidentia.io) del cual realizamos un fork

---
## Resumen ejecutivo

La aplicación programaze constituye una solución informática cuyo propósito pretende mejorar y facilitar la gestión y organización de la jornadas universitarias InnoSoft, la cuales consisten en una serie de actividades, stands y charlas impartidas por expertos que se realizan durante una semana del curso lectivo y están organizadas por los alumnos de 4 curso de la asignatura de Evaluación y Gestión de la Configuración. Para la organización de las jornadas se consideran 4 tipos de roles que ordenados de mayor a menor son: profesores, presidentes, coordinadores y estudiantes.

La aplicación se ha desarrollado a partir de un fork del repositorio de [evidentia.io](https://github.com/drorganvidez/evidentia.io), el cual consiste en una migración de Evidentia(el que se utiliza actualmente en la jornadas) que estaba desarrollado en php con el framework laravel, a python y con el framework flask. El contenido inicial del fork consistía en una plantilla básica de la aplicación, que únicamente contenía la gestión de usuario y su autentificación y la gestión de sus roles en las jornadas Innosoft.

La aplicación programaze cuenta con la siguientes funcionalidades clave:

- Roles y permisos: Implementada ya de la plantilla tomada de evidentia, únicamente se ha añadido un nuevo rol llamada “Coordinador de Programa”
- Sistema de tokens: Es un mecanismo de créditos que permiten a los estudiantes proponer actividades a los coordinadores, presidentes y profesores
- Sistema de propuestas: El sistema permite crear propuestas con objetivo de completar el horario de las jornadas.
- Votaciones: Plataforma que permite aceptar o rechazar las diferentes propuestas de forma democrática entre los coordinadores, presidentes y profesores responsables de la jornada actual de InnoSoft.
- Seguimientos de Actividades: El sistema permite realizar un seguimiento del estado de las distinta tareas de las jornadas.

Por tanto el flujo de actividades desde que un alumno tiene una idea de una actividad para realizar en la jornadas hasta que sea aceptada sería el siguiente:

1. Alumno pide solicitud token.
2. Coordinador de programa acepta la solicitud de token.
3. Alumno crear propuesta de actividad para la jornada.
4. La propuesta es aceptada por los coordinadores, presidentes y profesores.
5. La propuesta pasa a estar aceptada.

Como se ha mencionado anteriormente para el desarrollo del proyecto se ha utilizado el lenguaje de programación python y el framework flask que permite construir una aplicación web robusta y escalable, gestionando las peticiones HTTP, las sesiones de usuarios, y las interacciones con la base de datos. Para el despliegue de la aplicación se ha utilizado docker siguiendo la siguiente arquitectura:

- Servidor Web (Nginx): Maneja las solicitudes entrantes y sirve el contenido estático.
- Contenedor de Base de Datos (MySQL): Almacena todos los datos de la aplicación.
- Contenedor de Aplicación (Flask): Contiene la lógica de negocio.

Durante la ejecución del proyecto Innosoft también se han adoptado prácticas para el desarrollo del código y la gestión del mismo. Estas prácticas incluyen el uso de Conventional Commits, la implementación de una estructura de ramificación Git Flow y la colaboración mediante Pair Programming.

**Conventional Commits**

La adopción de Conventional Commits ha permitido estandarizar los mensajes de commit dentro del repositorio del proyecto. Cada commit transmite claramente el propósito del cambio, haciendo que la revisión del código y la colaboración sean más eficientes.

**Git Flow**

La estructura de ramificación Git Flow se ha utilizado para organizar el desarrollo del proyecto de manera que separe claramente las nuevas características, las correcciones y las versiones. Esta estrategia ha permitido mantener un desarrollo continuo sin interrumpir el entorno de producción. Las ramas de características, lanzamiento y corrección de errores se manejan en un flujo de trabajo que garantiza la estabilidad del código y la facilidad para realizar despliegues regulares.

**Pair Programming**

El enfoque de Pair Programming ha sido fundamental en la colaboración del equipo de desarrollo. Esta técnica ha mejorado la calidad del código y ha acelerado el proceso de desarrollo, al mismo tiempo que ha servido como una herramienta eficaz para la formación y el aprendizaje entre pares. Para el trabajo en parejas se ha utilizado la extensión de Visual Studio Code “Live Share” que permite que varios desarrolladores trabajen sobre el mismo proyecto de forma colaborativa facilitando así el pair programming, esta herramienta también permite que cuando se realizan los commits, todos los colaboradores de la sesión de trabajo estén como coautores del commit. 

Para las pruebas del sistema se han realizado 3 tipos de tests.

- Test Unitarios para validar la lógica de negocio y comprobar que los componentes de la aplicación funcionan correctamente.
- Pruebas de Interfaz con Selenium, que permite automatizar las acciones de navegadores y verificar el correcto funcionamiento de la aplicación en un entorno similar al del usuario final.
- Pruebas de carga con Locust, que evalúan el rendimiento de la aplicación bajo condiciones de uso extensivo.


Se ha configurado el GitHub Actions para automatizar el flujo de trabajo de integración y entrega continua. El cual sigue los siguientes pasos:

- Verificación de Conventional Commits: En cada commit, se ejecuta una verificación para asegurar que los mensajes sigan la convención establecida, lo cual facilita la legibilidad y el seguimiento de cambios.
- Ejecución de Pruebas: Con cada commit y pull request, se ejecutan automáticamente las pruebas unitarias para detectar problemas de forma temprana.
- Workflow sobre main:
  - Ejecución de pruebas: Al realizar merge a la rama principal (main), se ejecutan automáticamente las pruebas unitarias para detectar problemas de forma temprana.
  - Generación de Tags y Versionado: Si se pasan los tests, se genera un tag basado en la política de versionado de Conventional Commits, lo cual ayuda a mantener un historial claro de versiones.
  - Actualización en Docker Hub: Si el tag se genera correctamente, se sube la nueva imagen al Docker Hub, asegurando que la versión más reciente esté disponible para su despliegue.
  - Despliegue en Render: Finalmente, se actualiza el despliegue en Render, lo que permite que la aplicación en producción refleje los últimos cambios aprobados y probados.

---
## Descripción del sistema

Para la descripción del sistema de la aplicación Innosoft, enfocaremos el análisis en dos dimensiones: funcional y arquitectónico. Cabe destacar que nuestro sistema usa como base el código de [evidentia.io](https://github.com/drorganvidez/evidentia.io)

**Descripción Funcional:**

La aplicación programaze está diseñada para automatizar y facilitar la gestión de las jornadas innosoft. Funcionalmente, el sistema permite a los estudiantes de cuarto curso, dentro de la asignatura de Evaluación y Gestión de la Configuración, organizar propuestas durante las jornadas. Estas propuestas incluyen actividades y charlas impartidas por expertos en diversas áreas. 

Los usuarios del sistema se clasifican jerárquicamente en presidentes, coordinador de programa, coordinadores, estudiantes y profesores. Los estudiantes podrán iniciar sesión o registrarse en el sistema. Al acceder a la aplicación podremos acceder al apartado innosoft days en la sección programaze. Donde podremos visualizar todas las jornadas del sistema, pudiendo acceder en cada una de ellas a sus propuestas y votaciones.  Al acceder a las propuestas, los estudiantes pueden solicitar tokens, limitados a tres por cada solicitud de token, que se utilizan para proponer actividades para las jornadas. El coordinador podrá acceder a las solicitudes de token desde la sección programaze, y podrá aceptar o rechazar dichas solicitudes. Cuando un usuario tiene un token podrá realizar una propuesta. Al publicarla, dicha propuesta tendrá que ser aceptada por el coordinador para que se someta a una votación por presidentes, coordinadores y profesores. Una vez que el coordinador de programa acepta una propuesta se genera una votación para la propuesta que será visible dentro del apartado votaciones de la jornada correspondiente. Desde ese momento, los roles nombrados anteriormente podrán realizar votos de aceptación o rechazo sobre la votación. Cada vez que se realice un voto, el sistema detectará si la votación ha llegado al índice de aceptación establecido para que una propuesta se valide. Si aún se puede llegar al porcentaje de aceptación el sistema seguirá esperando votos. Si no se puede llegar, la votación y la propuesta pasarán a estado rechazadas. Y si el sistema detecta que se cumple el índice de aceptación, la votación cambiará a Aceptada y la propuesta a En preparación. Una vez la propuesta llega a este estado, se realizarán todas las acciones pertinentes que conlleven a la preparación de la propuesta. Una vez todo esté listo el coordinador de programa deberá acceder a los detalles de la propuesta para Confirmar. Todas las propuestas podrán ser rechazadas en todos sus estados por lo inconvenientes que puedan surgir. Si una propuesta es rechazada mientras está siendo sometida a una votación, dicha votación también se rechazará. Desde todos los listados se podrán hacer filtros personalizados por estados para hacer un seguimiento.


| Nombre del requisito            | Roles                             | Descripción                                                                         |
|---------------------------------|-----------------------------------|-------------------------------------------------------------------------------------|
| Registrarse o iniciar sesión    | -                                 | El sistema debe permitir autenticarte o registrarte.                                  |
| Acceder a las jornadas          | Usuario autenticado               | El sistema debe permitir acceder a las jornadas publicadas.                          |
| Visualizar propuestas           | Usuario autenticado               | El sistema debe permitir visualizar las propuestas publicadas.                       |
| Solicitar token de propuesta    | Usuario autenticado               | El sistema debe permitir solicitar un token de propuesta.                              |
| Aceptar y generar token de propuesta | Coordinador de programa         | El sistema debe permitir aceptar una solicitud de token de propuesta y generar el token para que un usuario del sistema pueda publicar una propuesta. |
| Publicar propuestas             | Usuario autenticado con un token de propuesta | El sistema debe permitir publicar una propuesta a cambio de su token de propuesta.  |
| Aceptar propuesta               | Coordinador de programa           | El sistema debe permitir aceptar una propuesta publicada.                             |
| Creación de votación            | Coordinador de programa           | Al aceptar una propuesta publicada, se creará una votación de aceptación entre presidencia y coordinadores, para dicha propuesta. |
| Votar en una votación           | Presidencia y coordinadores        | El sistema debe permitir votar en una votación abierta. Al alcanzar un porcentaje de aceptación la propuesta se considerará válida, y pasará a estar pendiente de comunicación (charla) o pendiente de asignación de horario (actividad). |
| Rechazar propuesta              | Coordinador de programa           | El sistema debe permitir rechazar una propuesta en cualquiera de sus estados.        |
| Gestionar estados              | Coordinador de programa           | El sistema debe permitir gestionar los estados de las propuestas en todos sus posibles estados.        |

El modelo de datos propuesto para desarrollar la aplicación es el siguiente:
![Modelo conceptual drawio](https://github.com/motero2k/programaze/assets/100673872/5b634cb5-4d87-4e52-87fe-df403f0c94b5)

Ejecución de pruebas para verificar la funcionalidad (app/tests):

- Tests unitarios: se han realizado tests unitarios que permiten comprobar el correcto funcionamiento de los modelos
- Tests de interfaz (Selenium): se han realizado tests de interfaz para asegurar el correcto funcionamiento de la aplicación desde un navegador web.
- Tests de carga (Locust): se han realizado tests de carga para analizar el rendimiento del sistema.

Se ha configurado el GitHub Actions para automatizar el flujo de trabajo de integración y entrega continua. El cual sigue los siguientes pasos:

- Verificación de Conventional Commits: En cada commit, se ejecuta una verificación para asegurar que los mensajes sigan la convención establecida, lo cual facilita la legibilidad y el seguimiento de cambios.
- Ejecución de Pruebas: Con cada commit y pull request, se ejecutan automáticamente las pruebas unitarias para detectar problemas de forma temprana.
- Workflow sobre main:
  - Ejecución de pruebas: Al realizar merge a la rama principal (main), se ejecutan automáticamente las pruebas unitarias para detectar problemas de forma temprana.
  - Generación de Tags y Versionado: Si se pasan los tests, se genera un tag basado en la política de versionado de Conventional Commits, lo cual ayuda a mantener un historial claro de versiones.
  - Actualización en Docker Hub: Si el tag se genera correctamente, se sube la nueva imagen al Docker Hub, asegurando que la versión más reciente esté disponible para su despliegue.
  - Despliegue en Render: Finalmente, se actualiza el despliegue en Render, lo que permite que la aplicación en producción refleje los últimos cambios aprobados y probados.
 
**Arquitectura del Sistema:**

Arquitectónicamente, la aplicación está construida sobre el lenguaje de programación Python, utilizando el framework web Flask. Flask proporciona las herramientas necesarias para construir una aplicación web robusta y escalable, gestionando las peticiones HTTP, las sesiones de usuarios, y las interacciones con la base de datos.

La aplicación está contenida y desplegada utilizando Docker, lo cual garantiza la portabilidad y la consistencia del entorno de ejecución en diferentes máquinas.

Componentes y Subsistemas:
- Servidor Web (Nginx): Maneja las solicitudes entrantes y sirve el contenido estático, actuando como un proxy inverso para las peticiones dinámicas hacia el servidor de la aplicación Flask.
- Contenedor de Base de Datos (MySQL): Almacena todos los datos relacionados con los usuarios, tokens, propuestas, votaciones, votos, etc.
- Contenedor de Aplicación (Flask): Contiene la lógica de la web proporcionando todas las funcionalidades del sistema.

Contenedor adicional para ejecución de tests en Selenium:
- Contenedor selenium/standalone-chrome: Permite crear un contenedor en el cual se ejecuten los tests de selenium desde un navegador Chrome.

```bash
docker run -d -p 4444:4444 --name selenium-container selenium/standalone-chrome
```

### Cambios desarrollados
Cambios Desarrollados:

- En el desarrollo del proyecto, se han realizado las siguientes adiciones y mejoras: Autenticación como Coordinador de programa: Creación de un nuevo rol para administrar el acceso a diversos apartados del sistema.
- Módulo de jornadas: creación de la entidad jornada que permite crear nuevas jornadas en el sistema.
- Sistema de Tokens: Implementación de un sistema de crédito basado en tokens que limita el número de propuestas que un estudiante puede hacer.
- Sistema de solicitudes de tokens: Los usuarios pueden realizar solicitudes de tokens que podrán ser aceptadas o rechazadas por el coordinador de programa desde su panel de solicitudes.
- Módulo de propuesta: el sistema permite realizar propuestas si tenemos tokens. Estas propuestas pueden ser aceptadas o rechazadas por el coordinador de programa.
- Gestión de estado de las propuestas: el sistema permite realizar una gestión continua sobre el estado de las propuestas, pudiendo aceptarlas y rechazarlas en los estados convenientes y desencadenando las acciones oportunas sobre el resto de entidades que dependen de dicho estado. (Votación)
- Módulo de Votación: Desarrollo de una funcionalidad que permite crear votaciones al aceptar propuestas con el fin de llegar a un censo entre coordinadores, presidentes y profesores.
- Gestión de votos e índice de aceptación: los roles mencionados en el anterior punto podrán realizar 1 voto sobre cada votación. Al llegar a un índice de aceptación establecido, el sistema aceptará automáticamente la votación y cambiará el estado de la propuesta correspondiente a la votación. También se rechazará si el sistema detecta que no es posible llegar al índice de aceptación.

La aplicación programaze, con su enfoque en la gestión de propuestas y su implementación técnica avanzada, representa una solución que mejora significativamente la experiencia de organización de jornadas.

---
## Visión global del proceso de desarrollo

El proceso de desarrollo del proyecto Innosoft ha seguido una metodología ágil y estructurada, aprovechando diversas herramientas de desarrollo, gestión y comunicación para maximizar la eficiencia y la calidad del producto final. A continuación, se presenta una visión global del proceso, integrando las herramientas utilizadas y ejemplificando cómo se aborda un cambio propuesto en el sistema hasta su despliegue en producción.

### Propuesta de Cambio:
Supongamos que se identifica la necesidad de agregar una nueva funcionalidad al sistema que permite a los usuarios filtrar las actividades de las jornadas por categorías. El proceso sería el siguiente:

**Creación de Issue:**

Un miembro del equipo o un stakeholder propone el cambio.
Se crea una 'issue' en el sistema de seguimiento (GitHub Projects). Toda issue deberá indicar lo siguiente:

- El identificador de la issue
- La descripción de la tarea a realizar: Debe indicar de forma resumida lo que hay que hacer
- El tipo de incidencia: Indica a qué apartado del proyecto afecta la incidencia.
- La prioridad de la incidencia: Indica la prioridad, y debe estimarse según la importancia e impacto del mismo sobre el avance del proyecto.
- Rol/es encargados de la incidencia: Indica quién o quiénes son las personas que se van a encargar de solventar la incidencia. Normalmente esas personas serán las mismas que originaron la incidencia.
- El estado de la incidencia: Indica el estado actual de la incidencia. Todo, In Progress, In Review, Done.

La clasificación de las issues pueden seguir los siguientes tipos:

- Calidad: Cuando la incidencia afecta a un aspecto de calidad del proyecto. En general, si una incidencia es de calidad, la prioridad no debe llegar a ser Alta
- Código: Cuando la incidencia afecta a una funcionalidad del proyecto.
- Integración: Cuando la incidencia afecta a la integración continua de la aplicación.
- Pruebas: Cuando la incidencia afecta a una o varias pruebas sobre la aplicación.
- Despliegue: Cuando la incidencia afecta al comportamiento del despliegue de la aplicación.
- Documentación: Cuando la incidencia ha aparecido en la documentación del proyecto.
- Construcción: Cuando la incidencia afecta a los script de construcción de la aplicación.

También se debe asignar a cada issue una prioridad que dependerá de dos factores: el impacto y la importancia. Teniendo en cuenta esto se asigna la prioridad a las issue de la siguiente forma:

- Critical: incidencia que hay que abordar instantáneamente al ser encontrada
- Very High: incidencia muy importante que afecta gravemente al proyecto
- High: incidencia importante que afecta gravemente al proyecto
- Medium: incidencia que se puede gestionar con mayor flexibilidad pero tiene importancia
- Low: incidencia con poca importancia
- Minimal: incidencia que prácticamente no tiene impacto en el desarrollo del proyecto


Asignación de Tareas:

Durante las reuniones de progreso el Scrum Master asigna a cada miembro del equipo una tarea por afinidad y se establecen plazos claros para su finalización.
En caso de indiferencia se realiza asignación por parte del Scrum Master según habilidad o por asignación aleatoria.

Cada tarea desarrollada se dará por completada cuando se realice una revisión de la misma por miembros que no hayan participado directamente en la tarea.
Se realizan reuniones regulares de control para evaluar el progreso y ajustar la gestión de tareas según sea necesario.


**Las políticas de la interacción interna del equipo durante el desarrollo del proyecto han sido las siguientes:**

- Comunicación:

Para las discusiones cotidianas y actualizaciones rápidas, la comunicación del equipo se llevará a cabo a través de los  grupos de whatsapp o discord pertinentes.
Las reuniones de control de equipo se programan semanalmente para discutir el progreso del proyecto, los desafíos y la planificación.
Se fomentará la comunicación abierta y la colaboración, y los miembros del equipo deberán responder a las solicitudes de comunicación en un plazo razonable (máx 1 semana).
En caso de faltas de respeto o falta de implicación se aplicará la política P-CTRL-Sancionadora.

- Reuniones:

Se distinguen las reuniones semanales de control de las técnicas:

En las reuniones semanales de control se procura ser lo más conciso posible, dando un estado actual del proyecto y la necesidad de reuniones técnicas. Se toman decisiones de alto nivel o rápidas de resolver. Para esto es imperante el uso de un orden del día preparado previamente. Las reuniones técnicas tienen una duración mayor y sirven para trabajar en grupo o discutir ciertas decisiones. Se fomentará la participación de todos los miembros del equipo de trabajo y al final de la reunión se debe guardar el diario de sesión.

- Resolución de conflictos:

Es deber de todos los miembros resolver los conflictos de forma pacífica, pudiéndose aplicar medidas sancionadoras en caso contrario. Para resolver un conflicto se hablará entre los interesados presentando argumentación que respalde su punto de vista, en caso de no llegar a una resolución el Scrum Master hará de mediador, quien podrá apoyarse de quien considere para resolver el conflicto.

**Desarrollo:**

El equipo asignado comienza a trabajar en la 'issue', cambiando su estado a 'In Progress'. Se utiliza Git Flow para manejar las ramas del repositorio. Se crea una rama de 'feature' específica para este cambio. Durante el desarrollo, se siguen las convenciones de Conventional Commits para los mensajes de commit, lo que facilita la trazabilidad y el seguimiento de cambios.

Las políticas de desarrollo del equipo son:

- Control de versiones: Se debe utilizar un sistema de control de versiones, en este caso Git, para gestionar el repositorio del proyecto. Se usará GitHub para almacenarlo en la nube. Todos los cambios en el código deben registrarse en el repositorio con comentarios significativos siguiendo la política de commits y la política de ramas.

- Commits: Los commits se mantendrán atómicos, lo que significa que cada commit debe abordar un solo cambio o una única funcionalidad. Se seguirá el estándar de "Conventional Commits" en el proceso de commits, lo que significa que cada commit debe tener un mensaje que seguirá el formato "tipo: mensaje":

  - tipo = "feat" para una nueva característica.
  - tipo ="fix" para una corrección.
  - tipo ="docs" para documentación, etc.).

Los mensajes de commit deben ser claros y descriptivos para que cualquier miembro del equipo pueda entender el propósito del commit sin necesidad de revisar el código.

- Ramas: Se emplea una aproximación a Git Flow. Debe existir una rama principal  “main” que refleje la versión estable y desplegable del software. Además, una rama “develop” que contenga los cambios de desarrollo. Cada característica, corrección de error o mejora importante debe tener su propia rama de desarrollo que nace de develop y se une a develop al finalizar. Para hacer merge de una rama se debe haber pasado una revisión por al menos un miembro del equipo. Este principio está sujeto a excepciones por máxima urgencia o por la minimalidad del cambio (Ejemplo: una errata en un texto).

- Revisión de Código: Una vez que la funcionalidad está completa y todas las pruebas pasan localmente, el estado de la 'issue' cambia a 'In Review'. Se crea un Pull Request (PR) hacia la rama 'develop'. El equipo comunica al resto del grupo sobre la petición de revisión. Otros miembros del equipo revisan el PR, asegurándose de que cumple con los estándares de calidad y no introduce errores.

**Las políticas del equipo del aseguramiento de la calidad y la revisión del código son las siguientes:**

- Integración Continua: Se realizarán pruebas de integración continua como se especifica en la asignatura Evolución y Gestión de la Configuración. Cada vez que se hace un cambio en una de las ramas main o develop deben ejecutarse.
- Buenas Prácticas: Se debe desarrollar usando las buenas prácticas en la ingeniería del Software. Para ello:
  - Refactorizar habitualmente, todo código que esté creando deuda técnica debe tenerse en cuenta y decidir ignorar el problema (en casos pequeños) o fijar una fecha para arreglarlo.
  - Dejar comentarios en las funciones que se creen, ser consistente en la estructura de directorios del sistema y pedir una segunda opinión del trabajo realizado (Política de revisión de código). 
  - En general, sea código o no, pedir una segunda opinión para que revise el trabajo.
- Revisión de código: Para que una petición de cambio se apruebe se debe realizar una Pull Request indicando claramente qué cambios se han realizado. La PR no puede dar conflictos, si los diera es el miembro que realizó la petición hacer un nuevo commit en la PR resolviendo los conflictos. Los test de integración continua deben pasar sin errores. El revisor debe proporcionar comentarios constructivos y, si es necesario, solicitar correcciones antes de aprobar la fusión. Una vez se haya cumplido todo el flujo descrito, se podrá mergear la pull request asegurando la calidad del código.

**Flujo de la tarea propuesta (el sistema permite a los usuarios filtrar las actividades de las jornadas por categorías)**
- Se crea la issue (o conjunto de issues) y se le asignan los estados correspondientes según lo descrito anteriormente.
  - Clasificación: Código
  - Prioridad: High
  - Estado: Todo
  - Encargado: @JaviFdez7 y @motero2k
- Una vez la issue entra a 'In progress', se crea una rama desde develop para resolver dicha issue.
- Se resuelve la issue en la rama creada siguiendo la política de commits de conventional Commits
- Al finalizar la implementación, se ejecutan los tests comprobando que la calidad del producto siga igual que en develop
- Se crea una pull request para pasar los cambios a develop
- Si la integración continua se pasa, esperaremos a que un compañero que no ha participado en la issue apruebe los cambios. Si la integración continua no se pasa o el compañero revisor no aprueba la pull request, tendremos que realizar los cambios pertinentes para solucionar los problemas.
- Una vez la pull request cumpla los requisitos de aceptación, se merge la rama y tendremos todos los cambios en develop.


  

---
## Entorno de desarrollo
---
## Ejercicio de propuesta de cambio
---
## Conclusiones y trabajo futuro
