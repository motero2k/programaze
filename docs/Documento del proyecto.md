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


---
## Entorno de desarrollo
---
## Ejercicio de propuesta de cambio
---
## Conclusiones y trabajo futuro
