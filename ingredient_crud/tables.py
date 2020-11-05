from flask_table import Table, Col, LinkCol

class Results(Table):
    ingredient_id = Col('Id', show=False)
    ingredient_name = Col('Name')
    ingredient_image = Col('Image')
    ingredient_calories = Col('Calories')

    edit = LinkCol('Edit', 'edit_view', url_kwargs=dict(id='ingredient_id'))
    edit = LinkCol('Delete', 'delete_ingredient', url_kwargs=dict(id='ingredient_id'))