from src import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=app.config.get('DEBUG'), host='0.0.0.0')