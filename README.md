## m-health-carbs-cuantification
Sistema para cuantificar carbohidratos a partir de imágenes usando segmentación y modelos de ML.


```text
📁 m-health-carbs-cuantification/
├── Construcción_Sistema_Archivos.py     # Script: crear estructura de carpetas (train/test/val)
├── UperNet_ConvNeX_Model.ipynb          # UperNet + ConvNeXt (segmentación) 
├── mL_Model.ipynb                       # ML clásico (Naive Bayes, SVM)
├── UNET_Model.ipynb                     # U-Net + BEIT (train/eval)
└── EstimacionGramos/
    ├── _annotations.dataset.coco.json   # Anotaciones COCO ATLAS (masks/bboxes/clases)
    ├── coberturas_exportadas.xlsx       # Referencias ATLAS (porciones/densidades/equivalencias)
    ├── Dataset_LookUpTable/             # Imágenes etiquetadas para construir/validar la LUT
    ├── LookUpTable.csv                  # LUT (área/volumen → gramos por clase)
    ├── Test pipeline/                   # Ejecuciones del pipeline sobre dataset de test
    ├── Utility_LUT.ipynb                # Generar/actualizar la LUT 
    └── Validación/                      # ⏫ Notebook + resultados de validación (última versión)

Nota: EstimacionGramos/Validación/ contiene la versión más reciente del pipeline (⏫).