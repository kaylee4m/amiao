from info import db

class Camera(db.Model):
    __tablename__ = "camera"
    id = db.Column(db.Integer, primary_key = True,autoincrement=True)
    url = db.Column(db.String(512), nullable=False)
    location = db.Column(db.String(512), nullable=False)
    telnet_status = db.Column(db.String(128))
    opencv_status = db.Column(db.String(128))
    is_delete = db.Column(db.Integer,default=0)
    remarks = db.Column(db.String(512))
    is_service = db.Column(db.Integer, db.ForeignKey("service.id"))
    service = db.relationship("Service", lazy="dynamic")


class Service(db.Model):
    __tablename__ = "service"
    id = db.Column(db.Integer, primary_key = True,autoincreament=True)
    url = db.Column(db.String(512), nullable=False)
    description = db.Column(db.String(512), nullable=False)
    is_delete = db.Column(db.Integer,default=0)
    remarks = db.Column(db.String(512))
    camera = db.relationship("Camera", backref="service",lazy="dynamic")