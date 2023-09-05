import os
import shutil


def create_module_module(module):
    # Directories and file paths
    module_path = os.path.join('app', module)
    templates_path = os.path.join(module_path, 'templates')
    templates_module_path = os.path.join(templates_path, module)
    init_path = os.path.join('app', '__init__.py')

    # Check module name
    if os.path.exists(module_path):
        raise Exception(f"Error: A folder named '{module}' already exists in 'app'!")

    # 1. Create the module's subdirectory and its nested directories
    os.makedirs(templates_module_path, exist_ok=True)

    # 2. Create HTML templates (index.html, list.html, view.html, edit.html)
    template_names = ['index', 'list', 'view', 'edit']
    for template_name in template_names:
        with open(os.path.join(templates_module_path, f'{template_name}.html'), 'w') as f:
            f.write('{% extends "base_template.html" %}\n\n')
            f.write('{% block title %}' + module + '{% endblock %}\n\n')
            f.write('{% block content %}\n\n{% endblock %}\n')

    # 3. Create __init__.py
    with open(os.path.join(module_path, '__init__.py'), 'w') as f:
        f.write('from flask import Blueprint\n\n')
        f.write(f'{module}_bp = Blueprint(\'{module}\', __name__, template_folder=\'templates\')\n')
        f.write(f'\nfrom . import routes\n')

    module_title = module.capitalize()

    # 4. Create routes.py
    with open(os.path.join(module_path, 'routes.py'), 'w') as f:
        f.write('import logging\n')
        f.write('from flask import render_template, request, jsonify\n')
        f.write('from flask_login import login_required\n')
        f.write(f'from . import {module}_bp\n')
        f.write(f'from .models import {module_title}\n')
        f.write(f'from ..services import delete_entity, delete_entity_bulk\n')
        f.write('logger = logging.getLogger(__name__)\n\n\n')

        f.write(f'@{module}_bp.route("/{module}")\n')
        f.write('@login_required\n')
        f.write(f'def index():\n')
        f.write(f'    logger.info(\'Access {module} index\')\n\n')
        f.write(f'    return render_template("{module}/index.html")\n\n\n')

        f.write(f'@{module}_bp.route("/{module}/all")\n')
        f.write('def all():\n')
        f.write(f'    all_items = {module_title}.query.all()\n')
        f.write(f'    return render_template("{module}/list.html", all_items=all_items)\n\n\n')

        f.write(f'@{module}_bp.route("/{module}/view/<int:id>")\n')
        f.write('def view(id):\n')
        f.write(f'    {module} = {module_title}.query.get_or_404(id)\n')
        f.write(f'    return render_template("{module}/view.html", {module}={module})\n\n\n')

        f.write(f'@{module}_bp.route("/{module}/edit/<int:id>")\n')
        f.write('def edit(id):\n')
        f.write(f'    {module} = {module_title}.query.get_or_404(id)\n')
        f.write(f'    return render_template("{module}/edit.html", {module}={module})\n\n\n')

        f.write(f'@{module}_bp.route("/{module}/delete", methods=["POST"])\n')
        f.write('def delete():\n')
        f.write(f'    {module}_id = request.form.get("id")\n\n')
        f.write(f'    if not {module}_id:\n')
        f.write('        return jsonify({"message": "ID is required"}), 400\n\n')
        f.write(f'    result, status_code = delete_entity({module_title}, {module}_id)\n\n')
        f.write('    return jsonify(result), status_code\n\n\n')

        f.write(f'@{module}_bp.route("/{module}/delete/bulk", methods=["POST"])\n')
        f.write('def delete_bulk():\n')
        f.write('    data = request.get_json()\n')
        f.write('    bulk_ids = data.get("bulkIds", "").split(",")\n\n')
        f.write('    if not bulk_ids:\n')
        f.write('        return jsonify({"message": "No IDs provided"}), 400\n\n')
        f.write(f'    result, status_code = delete_entity_bulk({module_title}, bulk_ids)\n\n')
        f.write('    if status_code == 404:\n')
        f.write('        return jsonify({{"message": "No {}s found with provided IDs"}}), status_code\n\n'.format(module))
        f.write('    return jsonify(result), status_code\n')

    # 5. Create forms.py
    with open(os.path.join(module_path, 'forms.py'), 'w') as f:
        # Add content for forms.py as needed
        pass

    # 6. Create services.py (or any other additional files)
    with open(os.path.join(module_path, 'services.py'), 'w') as f:
        # Add content for forms.py as needed
        pass

    # 7. Create models.py
    with open(os.path.join(module_path, 'models.py'), 'w') as f:
        f.write('from datetime import datetime\n')
        f.write('from sqlalchemy import DateTime\n')
        f.write('from app import db\n\n\n')
        f.write('class {}(db.Model):\n'.format(module_title))
        f.write('    id = db.Column(db.Integer, primary_key=True)\n')
        f.write('    created_at = db.Column(DateTime, default=datetime.utcnow)\n')
        f.write('    updated_at = db.Column(DateTime, default=datetime.utcnow)\n')

    # Update app/__init__.py to include blueprint import and registration
    with open(init_path, 'r') as f:
        lines = f.readlines()

    import_idx = None
    register_idx = None

    # Find the location for blueprint import and registration
    for idx, line in enumerate(lines):
        if "# Import blueprints" in line:
            import_idx = idx
        elif "# Register blueprints" in line:
            register_idx = idx

    # Add lines at the found positions, ensuring proper indentation
    if import_idx is not None:
        while not lines[import_idx + 1].strip() == "":
            import_idx += 1
        lines.insert(import_idx + 1, f"    from .{module} import {module}_bp\n")

    if register_idx is not None:
        while not lines[register_idx + 1].strip() == "":
            register_idx += 1
        lines.insert(register_idx + 1, f"    app.register_blueprint({module}_bp)\n")

    if import_idx is None or register_idx is None:
        cleanup_module_directory(module)
        raise Exception(
            f"Error: Insertion point not found in {init_path}. Please check the file and ensure you have the comments '# Import blueprints' and '# Register blueprints' in app/__init__.py.")
    else:
        with open(init_path, 'w') as f:
            f.writelines(lines)

    import subprocess

    subprocess.run(["docker", "exec", "-it", "web_container", "flask", "db", "migrate"])
    subprocess.run(["docker", "exec", "-it", "web_container", "flask", "db", "upgrade"])

    print(f"Module '{module}' successfully created!")


def cleanup_module_directory(module_name):
    """
    Removes the created module directory.
    """
    module_dir = os.path.join('app', module_name)
    if os.path.exists(module_dir):
        shutil.rmtree(module_dir)


if __name__ == '__main__':
    module = input("Please enter the name of the module: ")
    create_module_module(module)
