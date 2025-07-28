from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import uuid

# Simulación de base de datos local en memoria
data_list = []

# Añadiendo algunos datos de ejemplo para probar el GET
data_list.append({'id': str(uuid.uuid4()), 'name': 'User01', 'email': 'user01@example.com', 'is_active': True})
data_list.append({'id': str(uuid.uuid4()), 'name': 'User02', 'email': 'user02@example.com', 'is_active': True})
data_list.append({'id': str(uuid.uuid4()), 'name': 'User03', 'email': 'user03@example.com', 'is_active': False}) # Ejemplo de item inactivo

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import uuid

data_list = []  # Lista en memoria

class DemoRestApi(APIView):
    name = "Demo REST API"
    
    def get(self, request):
        # Filtra solo los activos
        active_items = [item for item in data_list if item.get('is_active', False)]
        return Response(active_items, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data

        # Validación mínima
        if 'name' not in data or 'email' not in data:
            return Response({'error': 'Faltan campos requeridos.'}, status=status.HTTP_400_BAD_REQUEST)

        data['id'] = str(uuid.uuid4())
        data['is_active'] = True
        data_list.append(data)

        return Response({'message': 'Dato guardado exitosamente.', 'data': data}, status=status.HTTP_201_CREATED)

    def put(self, request):
        """
        Reemplaza completamente los datos de un elemento excepto el ID.
        El ID es obligatorio en el cuerpo de la solicitud.
        """
        data = request.data
        item_id = data.get('id')

        if not item_id:
            return Response({'error': 'El campo "id" es obligatorio.'}, status=status.HTTP_400_BAD_REQUEST)

        # Buscar el elemento
        for idx, item in enumerate(data_list):
            if item['id'] == item_id:
                # Mantener ID y estado actual si existe
                data['id'] = item_id
                data['is_active'] = item.get('is_active', True)
                data_list[idx] = data
                return Response({'message': 'Elemento reemplazado exitosamente.', 'data': data}, status=status.HTTP_200_OK)

        return Response({'error': 'Elemento no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request):
        """
        Actualiza parcialmente los campos de un elemento por su ID.
        """
        data = request.data
        item_id = data.get('id')

        if not item_id:
            return Response({'error': 'El campo "id" es obligatorio.'}, status=status.HTTP_400_BAD_REQUEST)

        # Buscar el elemento
        for item in data_list:
            if item['id'] == item_id:
                # Actualizar solo los campos enviados
                for key, value in data.items():
                    if key != 'id':  # No permitir cambiar el ID
                        item[key] = value
                return Response({'message': 'Elemento actualizado parcialmente.', 'data': item}, status=status.HTTP_200_OK)

        return Response({'error': 'Elemento no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        """
        Elimina lógicamente un elemento (is_active=False) por su ID.
        """
        item_id = request.data.get('id')

        if not item_id:
            return Response({'error': 'El campo "id" es obligatorio.'}, status=status.HTTP_400_BAD_REQUEST)

        for item in data_list:
            if item['id'] == item_id:
                item['is_active'] = False
                return Response({'message': 'Elemento eliminado lógicamente.'}, status=status.HTTP_200_OK)

        return Response({'error': 'Elemento no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
