from flask import Flask, Response

app = Flask(__name__)

@app.route('/wadl', methods=['GET'])
def wadl():
    contenido = """<?xml version="1.0" encoding="UTF-8"?>
<application xmlns="http://wadl.dev.java.net/2009/02">
    <resources base="http://localhost:5005/">
        <resource path="datos">
            <method name="GET">
                <response>
                    <representation mediaType="application/json"/>
                </response>
            </method>
        </resource>
    </resources>
</application>"""
    return Response(contenido, mimetype='application/xml')

if __name__ == '__main__':
    app.run(port=5006)
