from flask import Flask, render_template, request, send_file
from scripts import forms, build
import os

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/template/')
def template():
    return render_template('template.html')

@app.route('/updates/')
def updates():
    filename = os.listdir('updates')
    return render_template('updates.html', files=filename)

@app.route('/updates/latestver')
def updatesLatestVer():
    return render_template('latestver.html')

@app.route('/updates/latest')
def updatesLatest():
    path = "updates/ToolsHINCDv3.2.zip"
    return send_file(path, as_attachment=True)

@app.route('/template/interface', methods=["GET", "POST"])
def interface():
    form = forms.buildinterface_form(request.form)
    if request.method == 'POST' and form.validate():
        config = build.build_interface(**form.data)
        with open('int-builder.txt', 'w') as f:
            f.write(config)
        return(download('int-builder.txt'))
    return render_template('template/interface.html', form=form)

@app.route('/template/vlan', methods=["GET", "POST"])
def vlan():
    form = forms.buildvlan_form(request.form)
    if request.method == 'POST' and form.validate():
        config = build.build_vlan(**form.data)
        with open('vlan-builder.txt', 'w') as f:
            f.write(config)
        return(download('vlan-builder.txt'))
    return render_template('template/vlan.html', form=form)

@app.route('/download')
def download(file):
    path = file
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(port=8080, debug = True)