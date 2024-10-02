<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QR de Plaza Principal</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f7f7f7;
            background-image: url('f3.jpg');
            background-attachment: fixed;
            background-size: cover;
            background-position: center;
        }

        .content-wrapper {
            background-color: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .logo-container {
            position: absolute;
            top: 20px;
            right: 20px;
            width: 100px;
            height: auto;
        }

        .logo-container img {
            width: 100%;
            height: auto;
        }

        @media (max-width: 600px) {
            .logo-container {
                width: 60px;
            }
        }
        h1, h2, h3 {
            text-align: center;
            color: #2c3e50;
        }

        h1 {
            font-size: 2.5em;
            margin-bottom: 20px;
        }

        h3 {
            font-size: 1.1em;
            font-weight: normal;
            margin-bottom: 20px;
        }

        .image-container {
            text-align: center;
            margin: 20px 0;
            max-width: 100%;
            overflow: hidden;
        }

        .image-container img {
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }

        @media (min-width: 768px) {
            .image-container {
                max-width: 80%;
                margin: 20px auto;
            }
        }

        @media (min-width: 1024px) {
            .image-container {
                max-width: 70%;
            }
        }

        .image-container:hover img {
            transform: scale(1.05);
        }

        .cta-button {
            display: block;
            width: 80%;
            max-width: 300px;
            margin: 30px auto;
            padding: 15px;
            background-color: #3498db;
            color: white;
            text-align: center;
            text-decoration: none;
            font-size: 1.2em;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }

        .cta-button:hover {
            background-color: #2980b9;
        }
        
        #visitas-info {
            background-color: rgba(255, 255, 255, 0.8);
            padding: 10px;
            border-radius: 5px;
            position: fixed;
            bottom: 10px;
            left: 10px;
            font-size: 0.9em;
        }
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

        <a href="https://www.google.com/maps/dir/?api=1&destination=-29.164980, -67.495267" class="cta-button">¿Cómo llegar a la Plaza Principal?</a>

        <!--div id="visitas-info"></div>

        <script>
            function actualizarVisitas() {
                let visitas = localStorage.getItem('visitas') || 0;
                visitas = parseInt(visitas) + 1;
                localStorage.setItem('visitas', visitas);

                const ahora = new Date();
                const fechaHora = ahora.toLocaleString('es-AR');

                const visitasInfo = document.getElementById('visitas-info');
                visitasInfo.innerHTML = `
                    <p>Cantidad de visitas: ${visitas}</p>
                    <p>Fecha y hora: ${fechaHora}</p>
                `;
            }

            window.onload = actualizarVisitas;
        </script>
    </div-->
</body>

</html>
