import base64

with open('D:/ai魔法/紹元超跑/car.glb', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode('ascii')

with open('D:/ai魔法/紹元超跑/car_model_data.js', 'w', encoding='utf-8') as f:
    f.write('window.CAR_GLB_DATA = "data:model/gltf-binary;base64,' + b64 + '";\n')

print("SUCCESS: car_model_data.js created!")
