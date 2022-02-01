from website import create_app
import os
# import create_app will make it like an object as website is now an package
# Now after we build an instance of the create_app function, and run it main to work as the server

app = create_app()
if __name__ == '__main__':
    port = int(os.getenv('PORT'))
    app.run(host='0.0.0.0', port=port)