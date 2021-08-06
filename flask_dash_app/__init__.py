from flask import Flask

def init_app():
    app = Flask(__name__,instance_relative_config = False)
    #app.config.from_object('config.Config')


    with app.app_context():
        from . import routers
        from .plotlydash.dashboard_temp import init_dashboard_temp
        from .plotlydash.dashboard import init_dashboard
        from .plotlydash.dashboard_lite import init_dashboard_lite
        from .plotlydash.dashboard_security import init_dashboard_security


        app = init_dashboard(app)
        app = init_dashboard_temp(app)
        app = init_dashboard_lite(app)
        app = init_dashboard_security(app)
        return app