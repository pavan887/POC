# app.py
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/print', methods=['GET'])
def print_message():
    message = request.args.get('message', 'Printing Service 1')
    
    # Create a .txt file and write the message to it
    with open('output.txt', 'w') as file:
        file.write(message)

    # Create a response with the file content for download
    response = make_response(message)
    response.headers["Content-Disposition"] = "attachment; filename=output.txt"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
