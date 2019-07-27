from .flask_fff import FFF


def fff(app: object = None):
        if app:
              return FFF(app)
        return FFF()
