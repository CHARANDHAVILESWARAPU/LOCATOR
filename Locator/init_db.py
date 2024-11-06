from app import app, db, User
from werkzeug.security import generate_password_hash

# Create the application context and initialize the database
with app.app_context():
    db.create_all()
    print("Database tables created successfully.")
    
    # Check if the user with email "charan7093@gmail.com" already exists
    user1 = User.query.filter_by(email="charan7093@gmail.com").first()
    if user1:
        # Update password with a hashed version
        user1.password = generate_password_hash("7093789314", method='pbkdf2:sha256')
        print("Updated password for charan7093@gmail.com")
    else:
        # Add user if not existing
        user1 = User(
            name="charan", 
            email="charan7093@gmail.com", 
            password=generate_password_hash("7093789314", method='pbkdf2:sha256')
        )
        db.session.add(user1)
        print("Test user added successfully.")

    # Check if the user with email "test@example.com" already exists
    user2 = User.query.filter_by(email="test@example.com").first()
    if user2:
        # Update password with a hashed version
        user2.password = generate_password_hash("test123", method='pbkdf2:sha256')
        print("Updated password for test@example.com")
    else:
        # Add user if not existing
        user2 = User(
            name="Test User", 
            email="test@example.com", 
            password=generate_password_hash("test123", method='pbkdf2:sha256')
        )
        db.session.add(user2)

    db.session.commit()
    print("Database updated with hashed passwords.")
