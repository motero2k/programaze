from app import get_roles_from_authenticated
from flask import Flask, redirect, flash, request, url_for


class Role_access_manager:
    #Roles at app/auth/models.py  VALID_ROLES = ['STUDENT', 'COORDINATOR', 'SECRETARY', 'REVIEWER', 'EVENT_MANAGER', 'LECTURER', 'DEVELOPER','PRESIDENT']
    token_request = {"public": ["ANY_ROLE"],"accept":['COORDINATOR']}
    proposal = {"public": ["ANY_ROLE"], "accept": ["ddd"]}
    votation = {"public": ["ANY_ROLE"], "accept": ["ddd"]}
       
    @staticmethod
    def get_allowed_roles(module_name,access_level):
        module = getattr(Role_access_manager, module_name) #ex module= proposal
        return (module_name,access_level,module,module.get(access_level,[])) #ex proposal/accept
    
    @staticmethod
    def user_not_allowed(module_name,access_level):
        user_roles = get_roles_from_authenticated()  # Asegúrate de que get_roles_from_authenticated() devuelva el rol del usuario
        user_not_allowed = True
        allowed_roles_in_action = Role_access_manager.get_allowed_roles(module_name,access_level)
        if "ANY_ROLE" in allowed_roles_in_action:
            return True
        for role in user_roles:
            if role in allowed_roles_in_action:
                user_not_allowed = False

        return user_not_allowed
    

    
    @staticmethod
    def not_allowed_return_to_previous_page(module_name,access_level):
        allowed_roles_in_action = Role_access_manager.get_allowed_roles(module_name,access_level)
        flash(f"No tienes acceso a esta pagina. Roles permitidos: {allowed_roles_in_action}", 'error')
        return redirect(request.referrer or url_for('index'))