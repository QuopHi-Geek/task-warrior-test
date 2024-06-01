"""
Testing the cart API endpoints task

This module contains unit tests for the various endpoints of the cart API,
including getting all cart products, getting a single cart item, filtering
products, sorting products, getting a user's cart, adding a new product,
updating product details, updating a product, and deleting a cart.
"""
import json

import requests


ENDPOINTS = "https://fakestoreapi.com"


def test_get_all_cart_products():
    """
    Tests the GET request to retrieve all cart products.
    """
    response = requests.get(ENDPOINTS + "/products",timeout=5)
    assert response.status_code == 200
    assert response.ok is True
    assert len(response.json()) == 20

    response_body = response.json()

    # assert response contents
    assert response_body[0]["id"] == 1
    assert response_body[0]["title"] is not None
    assert response_body[0]["price"] is not None


def test_get_single_cart_item():
    """
    Tests the GET request to retrieve a single cart item.
    """
    response = requests.get(ENDPOINTS + "/products/5",timeout=5)
    assert response.status_code == 200
    assert response.ok is True
    assert len(response.json()) == 7

    # assert response content
    response_body = response.json()
    assert response_body["id"] == 5
    assert response_body["title"] is not None
    assert response_body["price"] is not None
    assert response_body["rating"]["count"] is not None


def test_filter_with_limit():
    """
    Tests the GET request to filter products with a limit.
    """
    response = requests.get(ENDPOINTS + "/carts?limit=5",timeout=5)
    assert response.status_code == 200
    assert response.ok is True
    assert len(response.json()) == 5

    # assert response content
    response_body = response.json()
    assert response_body[0]["id"] == 1
    assert response_body[0]["date"] is not None
    assert response_body[0]["products"] is not None


def test_sort_products():
    """
    Tests the GET request to sort products.
    """
    response = requests.get(ENDPOINTS + "/carts?sort=desc",timeout=5)
    assert response.status_code == 200
    assert response.ok is True
    assert len(response.json()) == 7

    # assert response content
    response_body = response.json()
    assert response_body[0]["id"] == 7
    assert response_body[0]["products"] is not None
    assert response_body[0]["date"] is not None


def test_filter_products_by_date_range():
    """
    Tests the GET request to sort products by date range.
    """
    start_date = "2020-10-10"
    end_date = "2019-12-10"
    response = requests.get(
        ENDPOINTS + "/carts?start_date=" + start_date + "&end_date=" + end_date,
        timeout=5,
    )
    assert response.status_code == 200
    assert response.ok is True
    assert len(response.json()) == 7

    response_body = response.json()

    # assert body content
    assert response_body[0]["date"] is not None
    assert response_body[0]["products"] is not None


def test_get_user_cart():
    """
    Tests the GET request to retrieve a user's cart.
    """
    response = requests.get(ENDPOINTS + "/carts/user/2",timeout=5)
    assert response.status_code == 200
    assert response.ok is True
    assert len(response.json()) == 1

    response_body = response.json()

    # assert body content
    assert response_body[0]["date"] is not None
    assert response_body[0]["products"] is not None
    assert response_body[0]["id"] is not None


def test_add_new_product():
    """
    Tests the POST request to add a new product to the cart.
    """
    post_data = {
        "userId": 18,
        "date": "2024-02-03",
        "products": [{"product": 5, "quantity": 1}, {"productId": 1, "quantity": 5}],
    }
    response = requests.post(
        ENDPOINTS + "/carts",
        data=json.dumps(post_data),
        headers={"Content-Type": "application/json"},
        timeout=5
    )
    assert response.status_code == 200
    assert response.ok is True

    response_body = response.json()
    assert response_body["id"] is not None
    assert response_body["date"] is not None
    assert response_body["products"] is not None


def test_update_only_product_details():
    """
    Tests the PATCH request to update only the product details.
    """
    data = {
        "userId": 3,
        "products": [{"productId": 12, "quantity": 7}],
    }

    response = requests.patch(
        ENDPOINTS + "/carts/18",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
        timeout=5
    )
    assert response.status_code == 200
    assert response.ok is True
    assert len(response.json()) == 3

    # assert response body
    response_body = response.json()
    assert response_body["products"] is not None


def test_update_product():
    """
    Tests the PUT request to update a product.
    """
    data = {
        "userId": 3,
        "date": "2024-02-03",
        "products": [{"productId": 5, "quantity": 2}],
    }

    response = requests.put(
        ENDPOINTS + "/carts/18",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
        timeout=5
    )
    assert response.status_code == 200
    assert response.ok is True
    assert len(response.json()) == 4

    # assert response body
    response_body = response.json()
    assert response_body["date"] is not None
    assert response_body["products"] is not None


def test_delete_cart():
    """
    Tests the DELETE request to delete a cart.
    """
    response = requests.delete(ENDPOINTS +"/carts/6",timeout=5)
    assert response.status_code == 200
    assert response.ok is True
    assert len(response.json()) == 5

    # assert response body - fake cart object is returned
    response_body = response.json()
    assert response_body["id"] is not None
    assert response_body["date"] is not None
    assert response_body["products"] is not None
