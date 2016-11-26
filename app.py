from flask import Flask, jsonify
from mc66 import MC66

app = Flask(__name__)

@app.route('/')
def index():
  return "index"

@app.route('/controls/all_on')
def all_on():
  mc = MC66()
  mc.all_on()
  out = {'msg': "Success"}
  return jsonify(out)

@app.route('/controls/all_off')
def all_off():
  mc = MC66()
  mc.all_off()
  out = {'msg': "Success"}
  return jsonify(out)

@app.route('/controls/<zone>/on')
def power_on(zone):
  zone = int(zone)
  mc = MC66()
  mc.power_on(zone)
  out = {'msg': zone}
  return jsonify(out)

@app.route('/controls/<zone>/off')
def power_off(zone):
  zone = int(zone)
  mc = MC66()
  mc.power_off(zone)
  out = {'msg': zone}
  return jsonify(out)

@app.route('/controls/<zone>/volume_up')
def volume_up(zone):
  zone = int(zone)
  mc = MC66()
  mc.volume_up(zone)
  out = {'msg': zone}
  return jsonify(out)

@app.route('/controls/<zone>/volume_down')
def volume_down(zone):
  zone = int(zone)
  mc = MC66()
  mc.volume_down(zone)
  out = {'msg': zone}
  return jsonify(out)

@app.route('/controls/<zone>/input/<channel>')
def set_input(zone, channel):
  zone = int(zone)
  channel = int(channel)
  mc = MC66()
  mc.set_input(zone, channel)
  out = {'msg': (str(zone)+str(channel))}
  return jsonify(out)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5001)

