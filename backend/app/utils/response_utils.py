from flask import jsonify

def error_response(message, status=400):
    return jsonify({'error': message}), status
