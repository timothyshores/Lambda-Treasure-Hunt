# Lambda-Treasure-Hunt

##Steps
1. Create a `api.txt` file in the root directory with just the API key. E.g. if your API key is 123 then the file should only contain 123
2. CD into the directory 
3. Run `python3 map.py` 
4. This should return a response from the server similiar to the response below

```
{   'cooldown': 1.0,
    'coordinates': '(60,60)',
    'description': 'You are standing in the center of a brightly lit room. You '
                   'notice a shop to the west and exits to the north, south '
                   'and east.',
    'elevation': 0,
    'errors': [],
    'exits': ['n', 's', 'e', 'w'],
    'items': [],
    'messages': [],
    'players': [   'player401', 'player402', 'player403', 'player404',
                   'player405', 'player406', 'player407', 'player408',
                   'player409', 'player410', 'player413', 'player414',
                   'player415', 'player416', 'player417', 'player418',
                   'player419', 'player420', 'player421', 'player422',
                   'player423', 'player426', 'player427', 'player428',
                   'player429', 'player430', 'player431', 'player432',
                   'player435', 'player437', 'player438', 'player439',
                   'player441', 'player443', 'player444', 'player445',
                   'player446', 'player447', 'player448', 'player449',
                   'player450', 'player451', 'player453', 'player454',
                   'player455', 'player456', 'player411', 'player457',
                   'player458', 'player459', 'player460', 'player461',
                   'player462', 'player465', 'player466', 'player467',
                   'player468', 'player469', 'player470', 'player471',
                   'player472', 'player473', 'player474', 'player475',
                   'player476', 'player477', 'player478', 'player479',
                   'player480', 'player481', 'player482', 'player483',
                   'player484', 'player485', 'player486', 'player487',
                   'player488', 'player489', 'player490', 'player491',
                   'player492', 'player493', 'player494', 'player495',
                   'player496', 'player497', 'player498', 'player499',
                   'player500'],
    'room_id': 0,
    'terrain': 'NORMAL',
    'title': 'A brightly lit room'}
```