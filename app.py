from app import app

# just a more simple way to run the app
# use only without debugging mode
if __name__ == '__main__':
    app.run(
        host = '127.0.0.1',
        port = 5000,
        debug = False
    )