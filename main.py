from src import initiate_app

server = initiate_app()

if __name__ == '__main__':
    server.run(threaded=True)

