import requests
import json

ENDPOINTS = "https://fakestoreapi.com"


def test_get_all_cart_products():
    response = requests.get(ENDPOINTS + "/products")
    assert response.status_code == 200
    assert response.ok is True
    assert len(response.json()) == 20

    response_body = response.json()

    #assert response contents
    assert response_body[0]["id"] == 1
    assert response_body[0]["title"] is not None
    assert response_body[0]['price'] is not None


def test_get_single_cart_item():
    response = requests.get(ENDPOINTS + "/products/5")
    assert response.status_code == 200
    assert response.ok is True
    assert len(response.json()) == 7

    #assert response content
    response_body = response.json()
    assert response_body["id"] == 5
    assert response_body["title"] is not None
    assert response_body["price"] is not None
    assert response_body["rating"]["count"] is not None
    

def test_filter_with_limit():
    response = requests.get(ENDPOINTS + "/carts?limit=5")
    assert response.status_code == 200
    assert response.ok is True
    assert len(response.json()) == 5

    #assert response content
    response_body = response.json()
    assert response_body[0]["id"] == 1
    assert response_body[0]["date"] is not None
    assert response_body[0]["products"] is not None



def test_sort_products():
    response = requests.get(ENDPOINTS +"/carts?sort=desc")
    assert response.status_code == 200
    assert response.ok == True
    assert len(response.json()) == 7

    #assert response content
    response_body = response.json()
    assert response_body[0]["id"] == 7
    assert response_body[0]["products"] is not None
    assert response_body[0]["date"] is not None

    
def test_filter_products_by_date_range():
    start_date = "2020-10-10"
    end_date = "2019-12-10"
    response = requests.get(ENDPOINTS + '/carts?start_date=' + start_date + '&end_date=' + end_date)
    assert response.status_code == 200
    assert response.ok is True
    assert len(response.json()) == 7
    
    response_body = response.json()
    
    #assert body content
    assert response_body[0]["date"] is not None
    assert response_body[0]["products"] is not None
    
    
def test_get_user_cart():
     response = requests.get(ENDPOINTS + "/carts/user/2")
     assert response.status_code == 200
     assert response.ok is True
     assert len(response.json()) == 1
     
     response_body = response.json()
     
     #assert body content
     assert response_body[0]["date"] is not None
     assert response_body[0]["products"] is not None
     assert response_body[0]["id"] is not None
   
   
def test_add_new_product():
    post_data =  {
                    "userId":5,
                    "date":'2020-02-03',
                    "products":[{"product":5,"quantity":1},{"productId":1,"quantity":5}]
                }
    response = requests.post(ENDPOINTS + "/carts",data=json.dumps(post_data))
    assert response.status_code == 200
    assert response.ok is True
    print(response)