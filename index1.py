from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.generar_html().encode())
        else:
            self.send_response(404)
            self.end_headers()

    def generar_html(self):
        return """
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Plaza Principal</title>
            <style>
                body { font-family: Arial, sans-serif; }
                .content-wrapper { max-width: 800px; margin: auto; padding: 20px; }
                .logo-container img { width: 100%; }
                .image-container img { width: 100%; }
                .cta-button { display: inline-block; padding: 10px 20px; background-color: #007BFF; color: white; text-decoration: none; border-radius: 5px; }
            </style>
        </head>
        <body>
            <div class="content-wrapper">
                <div class="logo-container">
                    <img src="UndecLOGO.png" alt="Logo de Universidad Nacional de Chilecito">
                </div>
                <h1>Plaza Principal</h1>
                <h3>Fue fundada el 19 de febrero de 1715 por el español Domingo de Castro y Bazán,
                    inicialmente bajo el nombre de Villa Santa Rita, luego cambió a Villa Argentina y finalmente a Chilecito.
                </h3>
                <div class="image-container">
                    <img src="plaza1.jpg" alt="Vista de la Plaza Principal">
                </div>
                <h3>
                    Particularmente, se destaca la plaza principal, llamada Caudillos Federales, con una frondosa arboleda y el
                    centro despejado. Esta es además, un sitio tradicional para la Bendición de Frutos que inaugura La Chaya en el
                    popular carnaval riojano, los febrero de cada año.
                </h3>
                <h3>
                    La ciudad se encuentra emplazada sobre un gran valle, al pie de la Sierra de Famatina, entre dicha Sierra y las
                    de Velasco. Dicha zona es una importante región turística y productiva, rodeada de extensos viñedos y olivares.
                </h3>
                <div class="image-container">
                    <img src="plaza2.jpg" alt="Otra vista de la Plaza Principal">
                </div>
                <a href="https://www.google.com/maps/dir/?api=1&destination=-29.164980,-67.495267" class="cta-button">¿Cómo llegar a la Plaza Principal?</a>
            </div>
        </body>
        </html>
        """

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Servidor corriendo en el puerto {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()