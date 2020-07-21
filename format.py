import json

# json structure
# [
#     {
#         'type' : 'read/write',
#         'code' : 'number' - for read
#     },
#     {
#         'name': 'Minsk',
#         'info' : 'text',
#         'image' : 'url'
#     }
# ]

def input_check(js):
    with open(js) as file:
        try:
            result = json.loads(file)[0]['type']
            if(result == 'read'):
                return json.loads(file)[0]['code']
            elif(result == 'write'):
                return json.loads(file)[1]
            else: 
                raise Exception('Bad json config!')
        except Exception as e:
            return e