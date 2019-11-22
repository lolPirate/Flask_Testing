from flask import Blueprint, render_template

routes = Blueprint('routes', __name__, template_folder='templates',)

@routes.route('/')
def timeline():
    # Do some stuff
    return render_template()

