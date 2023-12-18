# Documento del proyecto
## Indicadores del proyecto

| Miembro del equipo                | Horas | Commits | LoC Github | LoC Git fame | Test | Issues | Incremento          | Enlace      |
|-----------------------------------|-------|---------|------------|------------|------|--------|---------------------|------------------|
| Casal Ferrero, Rubén              | 61    | 26      | 2400       | 777         | 5   | 23     | Se crean una propuesta si el usuario tiene token y se filtran por todos sus posibles estados   | https://github.com/motero2k/programaze/commit/de7bb2f244791f1c8ee2171fc614e74033ad4a07 |
| Domínguez Ruiz, Andrés            | 65    | 19      | 2167       | 1385         | 13   | 18     | Una vez creada una propuesta, se podrá actualizar el estado de la propuesta. En caso de aceptarse una propuesta, se crea una votación, y si se cancela la propuesta pero tenía creada una votación, se borra la votación.  | https://github.com/motero2k/programaze/commit/de7bb2f244791f1c8ee2171fc614e74033ad4a07 |
| Fernández Castillo, Javier        | 62    | 118     | 2403       | 1895         | 10   | 15     | Se pueden realizar solicitudes de token y el coordinador de programa puede gestionarlas, aceptandolas o rechazandolas.  | https://github.com/motero2k/programaze/commit/6834a724323eed5fe33bb1b6faf6653731cd75d1 |
| Montero Martínez, Francisco Jesús | 53    | 14      | 1078       | 335         | 12   | 21     | Creación del rol de coordinador, adición de algunos usuarios de prueba en el script de inicialización y creación de jornadas.  | https://github.com/motero2k/programaze/commit/92cc097eb893f2fcbdac06966387b038747eb56e |
| Otero Barbasán, Manuel            | 60    | 35      | 1702       | 833         | 8   | 18     | Una vez admitida una propuesta se pasa a hacer una votación (votación en progreso), si más de la mitad de los coordinadores aceptan, la votación pasa a Aceptada y la propuesta a En preparacion. En caso contrario queda Rechazada la votacion y la propuesta Rechazada.  | https://github.com/motero2k/programaze/commit/b1872e7bc85fa3f3b5ac1a7a6d6117abb2063f0c |
| **TOTAL**                         | 301   | 212     | 9750       | 5225         | 48  | 41    | -  | - |

- Horas: número de horas empleadas en el proyecto
- Commits: Commits realizados
- LoC Github (líneas de código): Líneas de código en Insights de Github
- LoC Git fame (líneas de código): Líneas de código proporcioandas por Git fame
- Test: Tests realizados durante el proyecto
- Issues: issues gestionadas dentro del proyecto y que hayan sido gestionadas por el equipo -> conteo del número de issues en las que ha participado cada personas. El total es el número total de issues gestionadas durante el proyecto (41)
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

Hemos utilizado Visual Studio Code como entorno de desarrollo integrado (IDE), ya que tenemos experiencia en proyectos anteriores con este IDE y nos resulta muy cómodo trabajar con él. Para configurar VS Code, seguimos estos pasos:

Descargamos e instalamos Visual Studio Code desde el sitio web oficial (https://code.visualstudio.com/), siguiendo las instrucciones proporcionadas para nuestro sistema operativo específico. Es importante mencionar que la mayoría de los miembros del equipo utilizan Windows, aunque uno de los integrantes ha optado por trabajar en Linux.

Instalamos las extensiones pertinentes. Este paso es opcional y cada miembro ha instalado las que ha creído convenientes para sentirse cómodo en el desarrollo. Entre las extensiones más relevantes que se han utilizado, se destaca "Docker", la cual ha sido de gran utilidad para gestionar contenedores directamente desde el propio IDE. Esta extensión simplifica la administración de contenedores Docker, lo que es particularmente importante en un entorno de desarrollo basado en contenedores como el nuestro.

Configuramos Git en VS Code proporcionando nuestros nombres de usuario y direcciones de correo electrónico asociadas a nuestras cuentas de Git y lo asociamos al repositorio remoto que utilizamos en el proyecto, ya que VS Code ofrece una integración nativa con Git, lo que facilita la gestión del control de versiones de nuestro proyecto, al poder utilizar la interfaz gráfica para realizar las acciones típicas de Git.

Además de Visual Studio, hemos utilizado Docker Desktop para desplegar la aplicación. Al heredar el proyecto, notamos que los contenedores necesarios para nuestra aplicación ya estaban creados. Estos contenedores estaban configurados y listos para ser utilizados, lo que agilizó significativamente el proceso de despliegue. Tan solo tuvimos que seguir las instrucciones del archivo README:

Creamos un archivo .env en la raíz del proyecto y agregamos la siguiente información:
```
FLASK_APP_NAME=flask_base
MYSQL_HOSTNAME=db
MYSQL_DATABASE=flask_base_db
MYSQL_USER=flask_base_user
MYSQL_PASSWORD=flask_base_pass
MYSQL_ROOT_PASSWORD=flask_base_root_pass
```

Desplegamos la aplicación en el entorno de desarrollo, ejecutando el siguiente comando:
```
docker-compose -f docker-compose.dev.yml up -d
```

Una vez que los contenedores están en funcionamiento, ingresamos al contenedor "web_container". Dentro de este contenedor, ejecutamos comandos específicos para aplicar migraciones y actualizar la base de datos. Esto garantiza que la estructura de la base de datos esté alineada con la última versión de nuestra aplicación:
```
flask db migrate
flask db upgrade
python populate.py
```

Iniciamos un contenedor que aloja el servicio Selenium, con el objetivo de poder realizar las pruebas de interfaz, ejecutando el siguiente comando:
```
docker run -d -p 4444:4444 --name selenium-container selenium/standalone-chrome
```

En caso de que deseemos implementar nuestra aplicación en un entorno de producción, utilizamos un archivo de configuración separado llamado "docker-compose.prod.yml". Ejecutamos el siguiente comando para iniciar los contenedores en un entorno de producción:
```
docker-compose -f docker-compose.prod.yml up -d
```

Siguiendo estos pasos, nuestra aplicación Flask se despliega en el puerto predeterminado y se pone en funcionamiento en el entorno deseado, ya sea en desarrollo o producción.

Como hemos comentado, se han utilizado varios contenedores de Docker. Cada uno de estos desempeña un papel específico en el entorno de nuestra aplicación. A continuación, describiremos cada uno de estos contenedores:

- **web_container**: Es el núcleo de nuestra aplicación. Aquí reside la implementación de nuestra aplicación web principal, basada en el marco de desarrollo Flask. Este componente es responsable de servir las páginas web y gestionar las solicitudes de los usuarios que interactúan con nuestra aplicación. Se comunica con el contenedor de la base de datos (db_container) para realizar operaciones de lectura y escritura en la base de datos.

- **db_container**: Desempeña un papel esencial como servidor de la base de datos. Dentro de este contenedor, se encuentra un sistema de gestión de bases de datos que se utiliza para almacenar y administrar los datos de nuestra aplicación.

- **nginx_container**: Se desempeña como un servidor web y un equilibrador de carga inversa en nuestra arquitectura. Su función principal es dirigir y gestionar las solicitudes entrantes de los clientes hacia el contenedor de nuestra aplicación web. Nginx se encarga de gestionar el tráfico HTTP, proporcionando una capa adicional de rendimiento y seguridad para nuestra aplicación.

- **selenium-container**: Aloja el servicio Selenium, que es esencial para realizar pruebas automatizadas de la interfaz de usuario de nuestra aplicación. Selenium se utiliza para automatizar la interacción con nuestra aplicación a través de un navegador web. Esto permite realizar pruebas simulando la interacción real de los usuarios con la aplicación.

Estos contenedores trabajan en conjunto para proporcionar un entorno completo de desarrollo y despliegue de nuestra aplicación. El contenedor web (web_container) es la pieza central que ejecuta nuestra aplicación, mientras que el contenedor de la base de datos (db_container) almacena y gestiona los datos. El contenedor Nginx (nginx_container) actúa como un intermediario que maneja el tráfico web y el contenedor Selenium (selenium-container) se utiliza para pruebas automatizadas de la interfaz de usuario. Es importante destacar que los tres primeros contenedores (web_container, db_container y nginx_container) ya venían incluidos como parte de la aplicación que heredamos.

En cuanto a las versiones, hemos utilizado Visual Studio Code 1.85 y Docker Desktop 4.24.2.


---
## Ejercicio de propuesta de cambio

Propuesta: añadir un nuevo test unitario que compruebe el borrado de una propuesta.

1º La persona que solicita ese cambio primero deberá añadir esta nueva tarea al proyecto del repositorio, siguiendo la plantilla establecida para la documentación de issues.

<img width="417" alt="foto1" src="https://github.com/motero2k/programaze/assets/100673872/cc237945-06d0-44cd-989c-14257b43a4a9">

Una vez creado la issue, el responsable deberá actualizar su estado a In Progress.

<img width="422" alt="foto-1000000" src="https://github.com/motero2k/programaze/assets/100673872/43969290-c8a2-4fad-b358-2a9b66c030ee">

2º Tras crear esta issue, el responsable se encargará de realizar dicha tarea en una nueva rama. Si fuese una propuesta para arreglar algo, hay que utilizar una rama de fix, pero como estamos añadiendo algo nuevo es necesario crear una nueva rama.

<img width="300" alt="foto-2" src="https://github.com/motero2k/programaze/assets/100673872/34070d69-a80a-4636-a307-bd132f5a5b49">

3ºTras haber creado la nueva rama, el responsable utilizará un IDE cualquiera y clonará el repositorio para empezar a trabajar. 

En caso de que el responsable no tuviese clonado el repositorio con anterioridad , debe realizar git clone url del repo. En caso de no haber actualizado las claves SSH, será necesario actualizarlas

4º En caso de que el responsable ya tuviese clonado el repositorio, será necesario que realice el comando git fetch.

5ºUna vez abierto el repositorio local, cambia a la nueva rama haciendo git checkout “nueva rama”. También se podría haber creado la rama en local aplicando el comando git branch “nombre de la rama”

6º Ahora, el responsable diseñará el caso de prueba solicitado.

<img width="298" alt="foto-3" src="https://github.com/motero2k/programaze/assets/100673872/fbfc1001-1e95-4625-aa69-3757ac0b459b">

7º Para validar el correcto funcionamiento, el responsable debe hacer 3 cosas:

- Desplegar el contenedor de la aplicación aplicando: docker compose -f docker-compose.dev.yml up -d
- Desde Docker o desde una extensión de Docker sobre el IDE que esté utilizando el responsable, haremos Attach Shell sobre “programaze-web”.

<img width="107" alt="foto-4" src="https://github.com/motero2k/programaze/assets/100673872/1a7dfdd0-02ba-41d1-93dc-e7a5f58f9e32">

- Ahora, el responsable deberá hacer: flask db migrate,flask db upgrade y python populate.py (en ese mismo orden). Si todo ha salido bien, no debería haber salido ningún error durante el migrate y el update, y el mensaje final del populate deberá ser WELL DONE.
- Después, el responsable deberá ejecutar :pytest app/tests/nombre del archivo.py en donde se encuentre el test.
- Una vez ejecutado el comando, si todo ha salido bien, los tests deberán haber funcionado.

<img width="413" alt="foto-5" src="https://github.com/motero2k/programaze/assets/100673872/34b118a0-0eb1-4441-8241-a70f59d6a725">

8º Una vez verificado el funcionamiento del test implementado, el responsable deberá commitear los cambios a la rama remota. Para eso, deberá ejecutar:
- git add . (para añadir los cambios al commit)
- git commit -m “título” -m “descripción”. El formato de los commits deberán seguir las políticas establecidas por el equipo.

<img width="362" alt="foto-6" src="https://github.com/motero2k/programaze/assets/100673872/c5ab805c-6b87-488d-96ce-d6330904d36b">

- git push origin. para enviar los cambios a la rama remota.

9º Una vez finalizado la tarea, el responsable deberá actualizar el estado de la issue a Done, pero no debe cerrar la issue.

<img width="410" alt="foto-7" src="https://github.com/motero2k/programaze/assets/100673872/5a5acfbf-fb8b-4977-ac37-c093e6dfbcfd">

10º El responsable deberá crear una pull request desde la rama creada hasta develop, y en la descripción deberá enlazar la issue a la que hace referencia.

<img width="348" alt="foto-8" src="https://github.com/motero2k/programaze/assets/100673872/1e1f5734-bacf-4f5e-81ce-20be1bc59aa9">

11º Después de crear la pull request, una persona que NO ha participado en el desarrollo de esa issue deberá validar la pull request.

<img width="242" alt="foto-9" src="https://github.com/motero2k/programaze/assets/100673872/7f2ec342-99f2-4fdb-9b87-1d2eda10459f">

12º Una vez validado el pull request, el responsable realizará el merge de la rama, y al hacerlo, la issue se cerrará automáticamente.

<img width="469" alt="Captura de pantalla 2023-12-18 200946" src="https://github.com/motero2k/programaze/assets/100673872/07f2faa3-7de0-48bc-9762-9cdf03bd8c40">

Este será el proceso que todo responsable deberá hacer para proponer un cambio.

---
## Conclusiones y trabajo futuro

En general, estamos muy contentos con el trabajo realizado. Nos hemos entendido bien como equipo y hemos cumplido con creces con los mínimos del proyecto. Ha sido, para varios de los integrantes, el contacto más serio con conceptos tan importantes como la integración continua o el despliegue a través de contenedores. Creemos que el código es fácilmente escalable y puede ser una interesante adición a las jornadas de los próximos años, ya que la gestión de propuestas se hace actualmente de forma manual, lo que es bastante incómodo para la gente de Programa y las personas interesadas en lanzar propuestas.

Planteamos varias mejoras al desarrollo, que no han sido posibles por falta de tiempo:

- Pasar Evidentia a Django, ya que es un framework más fácil de utilizar y que agilizaría mucho el desarrollo de elementos comunes dentro del desarrollo web, pudiendo dedicar más tiempo a cuestiones específicas de la aplicación y posibilitando, desde nuestro punto de vista, un mejor resultado final. Aún no hay un gran desarrollo detrás, por lo que el coste de cambiar de tecnología en este punto aún no sería muy grande, más aún teniendo en cuenta que varias de las cosas implementadas vienen por defecto con Django.
- Añadir una entidad que represente los sucesos de una propuesta y programar la lógica necesaria para que las propuestas estén compuestas por sucesos. Generalmente, en las jornadas, las propuestas no son únicamente una charla, si no que pueden venir acompañadas de sorteos, torneos y diferentes actividades. Por lo tanto, sería conveniente que a una propuesta se le pudieran añadir sucesos.
- Mostrar un calendario con todos los eventos de las jornadas. Actualmente las propuestas se pueden aceptar pero no se genera un calendario con todas las propuestas aceptadas, por lo que construirlo continuaría siendo una tarea manual que deberían realizar desde Programa.

