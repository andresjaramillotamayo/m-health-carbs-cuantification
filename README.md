## m-health-carbs-cuantification
Sistema para cuantificar carbohidratos a partir de imágenes usando segmentación y modelos de ML.

---

## 📁 Estructura del repositorio

📁 m-health-carbs-cuantification/
├── Construcción_Sistema_Archivos.py
│   # Script para crear la estructura de carpetas para entrenamiento
│   # (train, test, validation)
│
├── UperNet_ConvNeX_Model.ipynb
│   # Segmentación semántica con UperNet + ConvNeXt (config + evaluación)
│
├── mL_Model.ipynb
│   # Modelos clásicos (Naive Bayes, SVM) para estimación/posprocesado
│
├── UNET_Model.ipynb
│   # Segmentación con U-Net (backbone BEIT) y pipeline de entrenamiento
│
└── EstimacionGramos/
    ├── _annotations.dataset.coco.json
    │   # Anotaciones COCO del ATLAS (masks/bboxes/clases)
    ├── coberturas_exportadas.xlsx
    │   # Referencias del ATLAS (porción, equivalencias)
    ├── Dataset_LookUpTable/
    │   # Imágenes etiquetadas usadas para construir la LUT
    ├── LookUpTable.csv
    │   # Tabla de consulta (LUT) derivada de las referencias del ATLAS
    ├── Test pipeline/
    │   # Artefactos/ejecuciones del pipeline sobre el conjunto de test
    ├── Utility_LUT.ipynb
    │   # Notebook para generar/actualizar la LUT desde las fuentes
    └── Validación/
        # Notebook + resultados de validación del pipeline (última versión)


Nota / Note: La carpeta EstimacionGramos/Validación/ contiene la versión completa más
reciente del pipeline (⏫).