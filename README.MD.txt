## Product (storage) ##
const linkProduct = http://127.0.0.1:8000/api/storage/
1) для получение продуктов нужно перейти по get ссылке linkProduct
2) для создание продуктов нужно перейти по post linkProduct и передать json как :
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
3) для изменение длстаточно перейти по put linkProduct добавить айди продукта и передать json 
```javascript
   {
        "Product":
            {
                "name": "888888",
            }
        }
```
4) для удаления переходим по delete linkProduct добовляем айди и продукт будет удален 


## Category (Category) ##
const linkCategoty = http://127.0.0.1:8000/api/category/
1) для получение категории переходим по get ссылке linkCategoty
2) для создание категории нужно перейти по post linkCategoty и передать json как :
```javascript
   {
            "Category": {
                "name": "1010",
                "parent_id":1
            }
        }
```
3) для изменение длстаточно перейти по put linkCategoty добавить айди продукта и передать json 
```javascript
   {
        "Category": {
                "name": "8888",
        }
```
4) для удаления переходим по delete linkCategoty добовляем айди и категория будет удалена
