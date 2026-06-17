# Dashboard de Monitorización de Terremotos con AWS Serverless

## Descripción

Este proyecto implementa una solución serverless en AWS para monitorizar terremotos en tiempo real utilizando datos públicos del servicio USGS (United States Geological Survey).

La aplicación obtiene automáticamente información de terremotos, la almacena en DynamoDB, genera un fichero JSON actualizado y lo publica mediante un sitio web estático alojado en Amazon S3.

## Arquitectura

USGS API

↓

AWS Lambda (IngestEarthquakes)

↓

Amazon DynamoDB (Earthquakes)

↓

AWS Lambda (ExportEarthquakes)

↓

Amazon S3 (earthquakes.json)

↓

Dashboard Web

## Servicios AWS utilizados

- AWS Lambda
- Amazon DynamoDB
- Amazon S3
- Amazon EventBridge
- AWS IAM

## Funcionalidades

### Backend

- Obtención automática de datos desde la API de USGS.
- Ejecución programada mediante EventBridge.
- Almacenamiento de terremotos en DynamoDB.
- Exportación automática de datos a formato JSON.
- Actualización automática del dashboard.

### Frontend

- Mapa interactivo mundial mediante Leaflet.
- Estadísticas en tiempo real.
- Gráfico de magnitudes por ubicación.
- Gráfico temporal de actividad sísmica.
- Búsqueda y filtrado de resultados.
- Enlaces directos a USGS.
- Apertura de ubicaciones en Google Maps.
- Actualización automática cada 60 segundos.

## Fuente de datos

https://earthquake.usgs.gov

## Estructura del proyecto

### AWS Lambda

- IngestEarthquakes
- ExportEarthquakes

### DynamoDB

- Earthquakes

### Amazon S3

- index.html
- earthquakes.json

## Métricas mostradas

- Número total de terremotos
- Magnitud máxima detectada
- Profundidad media
- Eventos con magnitud superior a 2
- Último terremoto detectado
- Evolución temporal de magnitudes

## Posibles mejoras futuras

- CloudFront y HTTPS
- Alertas SNS por correo electrónico
- Terraform
- Dominio personalizado
- Histórico avanzado de terremotos

## Autor

Jon Gorritxo

Proyecto AWS Serverless de monitorización de terremotos en tiempo real.
