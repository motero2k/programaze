def delete_entity(model, entity_id):
    try:
        entity = model.query.get(entity_id)

        if not entity:
            return {"message": f"{model.__name__} not found"}, 404

        from app import db
        db.session.delete(entity)
        db.session.commit()

        return {"message": f"{model.__name__} deleted successfully"}, 200

    except Exception as e:
        return {"message": f"Error: {str(e)}"}, 500


def delete_entity_bulk(model, entity_ids):
    from app import db
    try:
        entities_to_delete = model.query.filter(model.id.in_(entity_ids)).all()

        if not entities_to_delete:
            return {"message": f"No {model.__name__}s found with provided IDs"}, 404

        for entity in entities_to_delete:
            db.session.delete(entity)

        db.session.commit()

        return {"message": f"{model.__name__}s deleted successfully"}, 200

    except Exception as e:
        return {"message": f"Error: {str(e)}"}, 500
