# from flask_sqlalchemy import SQLAlchemy
 
# db = SQLAlchemy()
 
# class InfoModel(db.Model):
#     __tablename__ = 'info_table'
 
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String())
#     age = db.Column(db.Integer())
 
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
 
#     def __repr__(self):
#         return f"{self.name}:{self.age}"



# # from flask_sqlalchemy import SQLAlchemy
 
# # db = SQLAlchemy()
 
# # class Model_name(db.Model):
# #     __tablename__ = 'table_name'
 
# #     field1_name = db.Column(db.Field1Type, primary_key...)
# #     field2_name = db.Column(db.Field2Type)
# #     field3_name = db.Column(db.Field3Type)
 
# #     def __init__(self, Field1_name,Field1_name,Field1_name):
# #         self.field1_name = field1_name
# #         self.field2_name = field2_name
# #         self.field3_name = field3_name
 
# #     def __repr__(self):
# #         return f"<statement>"