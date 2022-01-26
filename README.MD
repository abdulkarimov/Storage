## Product (storage) ##
const linkProduct = http://127.0.0.1:8000/api/storage/
1) ��� ��������� ��������� ����� ������� �� get ������ linkProduct
2) ��� �������� ��������� ����� ������� �� post linkProduct � �������� json ��� :
```javascript
   {
        "Product":
            {
                "image": "88025",
                "name": "88025",
                "price": 1,
                "count": 1,
                "category_id": 1,
            }
        }
```
3) ��� ��������� ���������� ������� �� put linkProduct �������� ���� �������� � �������� json 
```javascript
   {
        "Product":
            {
                "name": "888888",
            }
        }
```
4) ��� �������� ��������� �� delete linkProduct ��������� ���� � ������� ����� ������ 


## Category (Category) ##
const linkCategoty = http://127.0.0.1:8000/api/category/
1) ��� ��������� ��������� ��������� �� get ������ linkCategoty
2) ��� �������� ��������� ����� ������� �� post linkCategoty � �������� json ��� :
```javascript
   {
            "Category": {
                "name": "1010",
                "parent_id":1
            }
        }
```
3) ��� ��������� ���������� ������� �� put linkCategoty �������� ���� �������� � �������� json 
```javascript
   {
        "Category": {
                "name": "8888",
        }
```
4) ��� �������� ��������� �� delete linkCategoty ��������� ���� � ��������� ����� �������
