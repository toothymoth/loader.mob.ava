from flask import Flask, redirect
import os

app = Flask(__name__, static_folder='content')

HOST = "192.168.1.2"
PORT = 8881


@app.route('/compressed/<path:file>')
def load(file):
    realCdn = "https://live.ru.mob.avataria.cdn.101xp.com/2023_11/UR224-23_3.50.1_copmressed/"#"https://live.ru.mob.avataria.cdn.101xp.com/2023_10/UR210-387_3.50.0/"
    if os.path.isfile(fr"content/{file}"):
        print("Config is changing...")
        path = fr"http://{HOST}:{PORT}/content/{file}"
    else:
        path = fr"{realCdn}/{file}"
    return redirect(path)

@app.route('/pub/<path:file>')
def load_manifest(file):
    path = fr"http://{HOST}:{PORT}/content/pub/{file}"
    return redirect(path)

# https://live.ru.mob.avataria.cdn.101xp.com/2023_11/UR224-23_3.50.1_copmressed/
if __name__ == "__main__":
    app.secret_key = 'qwikks'
    app.run(host=HOST, port=PORT)
