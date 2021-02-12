from src import initiate_app

app_instance = initiate_app()

if __name__ == '__main__':
    app_instance.run(threaded=True)