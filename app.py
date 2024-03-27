from flask import Flask,session
import os
import swim_club

SWIM_FOLDER = 'swimdata/'
swimmers= {}

app = Flask( __name__ )
app.secret_key = "secret_key"

def populated_data():
    if "swimmers" not in session:
        swim_files = os.listdir(SWIM_FOLDER)
        swim_files.remove(".DS_Store")
        session["swimmers"] = {}
        for file in swim_files:
            name,*_ = swim_club.read_swim_data(SWIM_FOLDER,file)
            if name not in session["swimmers"]:
                session["swimmers"][name] = []
            session["swimmers"][name].append(file)

@app.get("/swimmers")
def display_swimmers():
    populated_data()
    return str(sorted(session["swimmers"]))
    # swim_files = os.listdir(SWIM_FOLDER)
    # swim_files.remove('.DS_Store') # Remove hidden file
    # session["swimmers"] = {}
    # for file in swim_files:
    #     name,*_ = swim_club.read_swim_data(SWIM_FOLDER,file)
    #     if name not in session["swimmers"]:
    #         session["swimmers"][name] =[]
    #     session["swimmers"][name].append(file)
    # return str(sorted(session["swimmers"]))

@app.get("/files/<swimmer>")
def get_swimmer_file(swimmer):
    populated_data()
    return str(session["swimmers"][swimmer])

if __name__ == "__main__":
    app.run(debug=True) 