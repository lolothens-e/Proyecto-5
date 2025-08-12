from django.test import TestCase
from django.urls import reverse
import json


class Guide20DemoRestApiTests(TestCase):
    def test_collection_get_returns_active_items(self):
        # GET on root collection
        resp = self.client.get('/demo/rest/api/')
        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.json(), list)

    def test_post_validates_and_creates(self):
        # Missing fields -> 400
        resp = self.client.post(
            '/demo/rest/api/',
            data=json.dumps({'name': 'UserX'}),
            content_type='application/json',
        )
        self.assertEqual(resp.status_code, 400)

        # Valid create -> 201
        resp = self.client.post(
            '/demo/rest/api/',
            data=json.dumps({'name': 'User04', 'email': 'user04@example.com'}),
            content_type='application/json',
        )
        self.assertEqual(resp.status_code, 201)
        body = resp.json()
        self.assertIn('data', body)
        self.assertIn('id', body['data'])
        return body['data']['id']

    def test_item_put_patch_delete_flow(self):
        # Create first
        create = self.client.post(
            '/demo/rest/api/',
            data=json.dumps({'name': 'User05', 'email': 'user05@example.com'}),
            content_type='application/json',
        )
        self.assertEqual(create.status_code, 201)
        item_id = create.json()['data']['id']

        # PUT replace
        put = self.client.put(
            f'/demo/rest/api/{item_id}/',
            data=json.dumps({'name': 'User05R', 'email': 'user05r@example.com'}),
            content_type='application/json',
        )
        self.assertEqual(put.status_code, 200)
        self.assertEqual(put.json()['data']['name'], 'User05R')

        # PATCH partial
        patch = self.client.patch(
            f'/demo/rest/api/{item_id}/',
            data=json.dumps({'email': 'user05+patch@example.com'}),
            content_type='application/json',
        )
        self.assertEqual(patch.status_code, 200)
        self.assertEqual(patch.json()['data']['email'], 'user05+patch@example.com')

        # DELETE logical
        delete = self.client.delete(f'/demo/rest/api/{item_id}/')
        self.assertEqual(delete.status_code, 200)

        # PUT not found for bogus id
        not_found = self.client.put(
            '/demo/rest/api/00000000-0000-0000-0000-000000000000/',
            data=json.dumps({'name': 'X', 'email': 'x@example.com'}),
            content_type='application/json',
        )
        self.assertEqual(not_found.status_code, 404)
