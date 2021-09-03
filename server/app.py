from splendor.app import app


if __name__ == "__main__":
    import splendor.database
    splendor.database.setup_sample_data()

    app.run(host="0.0.0.0", debug=True)
