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

## Integración con otros equipos
Este apartado no aplica para este proyecto. Se trata de un proyecto de innosoft. Debido a ser el único grupo que escogió esta modalidad no se ha tenido la oportunidad de hacerlo. 
Aún así, hemos tenido que adaptarnos al planteamiento propuesto por el tutor (David Romero Organvídez), ya que partimos desde el planteamiento de su estructura 
de datos y el estado en el que se encontraba su [repositorio](https://github.com/drorganvidez/evidentia.io) del cual realizamos un fork

## Resumen ejecutivo

## Descripción del sistema
Para la descripción del sistema de la aplicación Innosoft, enfocaremos el análisis en dos dimensiones: funcional y arquitectónico.

**Descripción Funcional:**

La aplicación Innosoft está diseñada para automatizar y facilitar la gestión de las jornadas innosoft. Funcionalmente, el sistema permite a los estudiantes de cuarto curso, dentro de la asignatura de Evaluación y Gestión de la Configuración, organizar propuestas durante las jornadas. Estas propuestas incluyen actividades y charlas impartidas por expertos en diversas áreas. 

Los usuarios del sistema se clasifican jerárquicamente en presidentes, coordinadores de programa, estudiantes y profesores. Los estudiantes podrán iniciar sesión o registrarse en el sistema. Al acceder a la aplicación podremos acceder al apartado innosoft days en la sección programaze. Donde podremos visualizar todas las jornadas del sistema, pudiendo acceder en cada una de ellas a sus propuestas y votaciones.  Al acceder a las propuestas, los estudiantes pueden solicitar tokens, limitados a tres por cada solicitud de token, que se utilizan para proponer actividades para las jornadas. El coordinador podrá acceder a las solicitudes de token desde la sección programaze, y podrá aceptar o rechazar dichas solicitudes. Cuando un usuario tiene un token podrá realizar una propuesta. Al publicarla, dicha propuesta tendrá que ser aceptada por el coordinador para que se someta a una votación por presidentes, coordinadores y profesores. Una vez que el coordinador de programa acepta una propuesta se genera una votación para la propuesta que será visible dentro del apartado votaciones de la jornada correspondiente. Desde ese momento, los roles nombrados anteriormente podrán realizar votos de aceptación o rechazo sobre la votación. Cada vez que se realice un voto, el sistema detectará si la votación ha llegado al índice de aceptación establecido para que una propuesta se valide. Si aún se puede llegar al porcentaje de aceptación el sistema seguirá esperando votos. Si no se puede llegar, la votación y la propuesta pasarán a estado rechazadas. Y si el sistema detecta que se cumple el índice de aceptación, la votación cambiará a Aceptada y la propuesta a En preparación. Una vez la propuesta llega a este estado, se realizarán todas las acciones pertinentes que conlleven a la preparación de la propuesta. Una vez todo esté listo el coordinador de programa deberá acceder a los detalles de la propuesta para Confirmar. Todas las propuestas podrán ser rechazadas en todos sus estados por lo inconvenientes que puedan surgir. Si una propuesta es rechazada mientras está siendo sometida a una votación, dicha votación también se rechazará. Desde todos los listados se podrán hacer filtros personalizados por estados para hacer un seguimiento.

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

## Visión global del proceso de desarrollo

## Entorno de desarrollo

## Ejercicio de propuesta de cambio

## Conclusiones y trabajo futuro
