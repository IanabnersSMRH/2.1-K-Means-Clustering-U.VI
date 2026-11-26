# 2.1 K-Means Clustering
## Práctica 2.1 — Agrupación K-Means (K-Means Clustering)

Segmentación no supervisada de 150 clientes sintéticos (`monto_total_usd` y `frecuencia_anual`) en $K = 3$ grupos utilizando `KMeans` de `scikit-learn` en un entorno Python sobre **Ubuntu EC2**, con exportación a `clientes_kmeans.csv` y carga a **Amazon S3** (`s3://aws-academy-datacenter-bucket-23-02-029/resultados/clientes_kmeans.csv`) mediante `boto3`[cite: 3, 6, 7, 8, 9].

### Resultados obtenidos
* **Inercia Intracluster (WCSS):** `1313363.06`[cite: 6]
* **Coeficiente de Silueta:** `0.8409`[cite: 6]
* **Centroides:**
  * **Cluster 0 (Alto consumo / VIP):** ~$1,485.68 USD | ~25.6 compras/año[cite: 3, 6]
  * **Cluster 1 (Consumo intermedio):** ~$810.32 USD | ~12.0 compras/año[cite: 3, 6]
  * **Cluster 2 (Bajo consumo):** ~$195.93 USD | ~4.9 compras/año[cite: 3, 6]
