from app import app, db

# separate command to create database tables
app.config.from_object('env_settings')


# Create all database tables
def create_database_tables():
    db.create_all()                             # creates database table according to models

# Start development web server
if __name__=='__main__':
    create_database_tables()