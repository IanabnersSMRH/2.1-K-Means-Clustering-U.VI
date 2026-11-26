import boto3
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Generación de datos sintéticos: [Monto total gastado, Frecuencia de compra anual]
np.random.seed(42)
grupo1 = np.random.normal(loc=[200, 5], scale=[30, 2], size=(50, 2))
grupo2 = np.random.normal(loc=[1500, 25], scale=[150, 4], size=(50, 2))
grupo3 = np.random.normal(loc=[800, 12], scale=[80, 3], size=(50, 2))

X_clientes = np.vstack([grupo1, grupo2, grupo3])

# 1. Configurar y entrenar K-Means con K=3
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
labels_kmeans = kmeans.fit_predict(X_clientes)

# 2. Cálculo de métricas e inspección de centroides
inercia = kmeans.inertia_
silueta = silhouette_score(X_clientes, labels_kmeans)
centroides = kmeans.cluster_centers_

print("=== CLUSTERIZACIÓN K-MEANS ===")
print(f"Inercia Intracluster (WCSS):     {inercia:.2f}")
print(f"Coeficiente de Silueta:          {silueta:.4f}")
print("\nCentroides de los Grupos (Monto Promedio, Frecuencia Promedio):")
for i, c in enumerate(centroides):
    print(f" Cluster {i}: Gastos de ${c[0]:.2f} USD | Frecuencia: {c[1]:.1f} compras/año")

# 3. Guardar CSV y subir a Amazon S3 (AWS Academy)
df_resultados = pd.DataFrame(
    X_clientes, columns=["monto_total_usd", "frecuencia_anual"]
)
df_resultados["cluster"] = labels_kmeans

archivo_local = "clientes_kmeans.csv"
df_resultados.to_csv(archivo_local, index=False)

s3_client = boto3.client(
    "s3",
    aws_access_key_id = "My-Key-ID",
    aws_secret_access_key = "My-Secret-Key",
    aws_session_token = "My-Session-Token",
    region_name="us-east-1",
)

bucket_name = "my-academy-bucket"
s3_key = "resultados/clientes_kmeans.csv"

s3_client.upload_file(archivo_local, bucket_name, s3_key)
print(f"\nArchivo subido correctamente a s3://{bucket_name}/{s3_key}")