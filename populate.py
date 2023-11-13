import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.auth.models import Role, User, Lecturer, user_roles, Student
from app.innosoft_day.models import Innosoft_day
from app.proposal.models import Proposal,ProposalType,State
from app.profile.models import UserProfile
from app.token_request.models import Token_request,TokenState
from datetime import datetime

DATABASE_URI = (
    f"mysql+pymysql://{os.getenv('MYSQL_USER', 'default_user')}"
    f":{os.getenv('MYSQL_PASSWORD', 'default_password')}"
    f"@{os.getenv('MYSQL_HOSTNAME', 'localhost')}:3306/{os.getenv('MYSQL_DATABASE', 'default_db')}"
)

engine = create_engine(DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)

def add_roles_and_lecturers_and_students():
    session = Session()

    # Borrar las tablas en el orden correcto para evitar conflictos de clave externa
    session.query(Lecturer).delete()
    session.query(Student).delete()
    session.query(user_roles).delete()
    session.query(UserProfile).delete()
    session.query(Token_request).delete()
    session.query(User).delete()
    session.query(Role).delete()
    
    
    
    session.commit()

    # Crear roles
    for role_name in Role.VALID_ROLES:
        role = Role(name=role_name)
        session.add(role)

    session.commit()

    lecturer_role = session.query(Role).filter_by(name="LECTURER").first()
    student_role = session.query(Role).filter_by(name="STUDENT").first()
    program_coordinator_role = session.query(Role).filter_by(name="STUDENT").first()

    # Crear usuarios y perfiles de usuario
    user1 = User(username="profesor1", email="profesor1@profesor1.com", password="profesor1", token=0)
    profile1 = UserProfile(user_id=user1.id, name="Profesor", surname="Uno", dni="12345678X")
    user1.profile = profile1
    user1.roles.append(lecturer_role)
    lecturer1 = Lecturer(user=user1)

    user2 = User(username="profesor2", email="profesor2@profesor2.com", password="profesor2", token=0)
    profile2 = UserProfile(user_id=user2.id, name="Profesor", surname="Dos", dni="87654321Z")
    user2.profile = profile2
    user2.roles.append(lecturer_role)
    lecturer2 = Lecturer(user=user2)

    user3 = User(username="profesor3", email="profesor3@profesor3.com", password="profesor3", token=0)
    profile3 = UserProfile(user_id=user3.id, name="Profesor", surname="Tres", dni="12345778C")
    user3.profile = profile3
    user3.roles.append(lecturer_role)
    lecturer3 = Lecturer(user=user3)

    alumno1 = User(username="alumno1", email="alumno1@alumno1.com", password="alumno1", token=0)
    profile_alumno1 = UserProfile(user_id=alumno1.id, name="Alumno", surname="Uno", dni="11112222A")
    alumno1.profile = profile_alumno1
    alumno1.roles.append(student_role)

    alumno2 = User(username="alumno2", email="alumno2@alumno2.com", password="alumno2", token=0)
    profile_alumno2 = UserProfile(user_id=alumno2.id, name="Alumno", surname="Dos", dni="22221111B")
    alumno2.profile = profile_alumno2
    alumno2.roles.append(student_role)

    program_coordinator1 = User(username="programcoordinator1", email="pc1@pc1.com", password="pc1", token=0)
    profile_program_coordinator1 = UserProfile(user_id=program_coordinator1.id, name="ProgramCoordinator", surname="Uno", dni="11113333C")
    program_coordinator1.profile = profile_program_coordinator1
    program_coordinator1.roles.append(program_coordinator_role)

    program_coordinator2 = User(username="programcoordinator2", email="pc2@pc2.com", password="pc2", token=0)
    profile_program_coordinator2 = UserProfile(user_id=program_coordinator2.id, name="ProgramCoordinator", surname="Dos", dni="22223333F")
    program_coordinator2.profile = profile_program_coordinator2
    program_coordinator2.roles.append(program_coordinator_role)



    # Agregar usuarios y perfiles a la sesión
    session.add(user1)
    session.add(user2)
    session.add(user3)
    session.add(alumno1)
    session.add(alumno2)
    session.add(program_coordinator1)
    session.add(program_coordinator2)

    # Commit para insertar los registros en la base de datos
    session.commit()

    token_request1 = Token_request(user_id = user1.id,description="Quiero hacer algodon de azucar en el despacho de M.Toro", token_state=TokenState.ACCEPTED)
    token_request2 = Token_request(user_id = user2.id, description="Torneo de ajedrez", token_state=TokenState.PENDING_OF_ACEPTATION)

    session.add(token_request1)
    session.add(token_request2)

    session.commit()

    session.close()

def add_proposals_and_innosoft_days():
    session = Session()
    
    session.query(Proposal).delete()
    session.query(Innosoft_day).delete()
    
    session.commit()

    innosoft_day1 = Innosoft_day(description="Jornada 2020/2021", subject="CiberSeguridad ", year=2020)
    innosoft_day2 = Innosoft_day(description="Jornada 2023/2024", subject="Inteligencia Artificial", year=2023)
    session.add(innosoft_day1)
    session.add(innosoft_day2)
    session.commit()
    proposal1 = Proposal(description="esta es la propuesta 1", subject="Charla medioambiente", proposal_type=ProposalType.TALK, state=State.PENDING_OF_ADMISION, innosoft_day_id=innosoft_day2.id)
    proposal2 = Proposal(description="esta es la propuesta 2", subject="Charla IA en la medicina", proposal_type=ProposalType.TALK, state=State.PENDING_OF_ACEPTATION, innosoft_day_id=innosoft_day2.id)
    proposal3 = Proposal(description="esta es la propuesta 3", subject="Concurso Imagenes Ia", proposal_type=ProposalType.ACTIVITY, state=State.ON_PREPARATION, innosoft_day_id=innosoft_day2.id)
    proposal4 = Proposal(description="esta es la propuesta 4", subject="Stand de Sostenibilidad", proposal_type=ProposalType.STAND, state=State.CONFIRMATED, innosoft_day_id=innosoft_day2.id)

    session.add(proposal1)
    session.add(proposal2)
    session.add(proposal3)
    session.add(proposal4)
    
    session.commit()

    session.close()
    
if __name__ == "__main__":
    add_roles_and_lecturers_and_students()
    add_proposals_and_innosoft_days()
    print("WELL DONE")