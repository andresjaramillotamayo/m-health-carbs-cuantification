import os
import shutil
import random

def split_dataset(general_path, train_ratio=0.7, val_ratio=0.2, test_ratio=0.1):

    # Crear carpetas para los conjuntos de entrenamiento, validación y prueba
    train_path = os.path.join(general_path, 'train')
    val_path = os.path.join(general_path, 'val')
    test_path = os.path.join(general_path, 'test')

    os.makedirs(train_path, exist_ok=True)
    os.makedirs(val_path, exist_ok=True)
    os.makedirs(test_path, exist_ok=True)

    # Obtener la lista de todas las imágenes
    images = [f for f in os.listdir(general_path) if os.path.isfile(os.path.join(general_path, f))]

    # Mezclar las imágenes aleatoriamente
    random.shuffle(images)

    # Calcular el número de imágenes para cada conjunto
    total_images = len(images)
    train_size = int(total_images * train_ratio)
    val_size = int(total_images * val_ratio)
    test_size = total_images - train_size - val_size  # El resto para el conjunto de prueba

    # Dividir las imágenes en los diferentes conjuntos
    train_images = images[:train_size]
    val_images = images[train_size:train_size + val_size]
    test_images = images[train_size + val_size:]

    # Mover las imágenes a sus respectivas carpetas
    for img in train_images:
        shutil.move(os.path.join(general_path, img), os.path.join(train_path, img))

    for img in val_images:
        shutil.move(os.path.join(general_path, img), os.path.join(val_path, img))

    for img in test_images:
        shutil.move(os.path.join(general_path, img), os.path.join(test_path, img))

    print(f"Total de imágenes: {total_images}")
    print(f"Imágenes de entrenamiento: {len(train_images)}")
    print(f"Imágenes de validación: {len(val_images)}")
    print(f"Imágenes de prueba: {len(test_images)}")

general_path = '/content/drive/MyDrive/Tesis/DatasetModelCarbs/Data'
split_dataset(general_path)
