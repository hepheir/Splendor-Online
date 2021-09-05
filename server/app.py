from splendor.app import app, socketio


if __name__ == "__main__":
    import splendor.database
    splendor.database.setup_sample_data()

    socketio.run(app,
                 host="0.0.0.0",
                 debug=True)
