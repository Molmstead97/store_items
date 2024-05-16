from fastapi import FastAPI
from schemas import Item

import json

app = FastAPI()

with open('store_items.json', 'r') as f:
    store_data = json.load(f)
    
store_items = []
for item in store_data:
    store_items.append(item)
    
@app.get('/items')
async def get_items() -> list[Item]:
    
    return store_items

@app.post('/items')
async def create_item(item: Item):
    
    store_items.append(item)
    
@app.put('/items/{item_id}')
async def update_item(item_id: int, updated_item: Item) -> Item:
    
    for item in store_items:
        if item['id'] == item_id:
            item.update(updated_item)
            return updated_item
        
@app.delete('/items/{item_id}') 
async def delete_item(item_id: int):
    global store_items
    store_items = [item for item in store_items if item['id'] != item_id]
    return store_items, f'{item['name']} successfully deleted'
    

   
                
        
    