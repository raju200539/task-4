from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        "message": "Hello from DevOps Git Project!",
        "status": "success"
    })

@app.route('/health')
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "devops-git-project"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
