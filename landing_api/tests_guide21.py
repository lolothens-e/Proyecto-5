from django.test import TestCase
import json

class Guide21LandingApiTests(TestCase):
    def test_get_collection(self):
        resp = self.client.get('/landing/api/index/')
        self.assertEqual(resp.status_code, 200)
        # Firebase puede retornar dict (map de ids->objeto) o None si vacío
        try:
            body = resp.json()
        except Exception:
            body = None
        self.assertTrue(resp.status_code == 200)

    def test_post_creates_resource(self):
        payload = {"nombre": "User From Test", "mensaje": "Hola desde tests"}
        resp = self.client.post(
            '/landing/api/index/',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(resp.status_code, 201)
        body = resp.json()
        self.assertIn('id', body)
