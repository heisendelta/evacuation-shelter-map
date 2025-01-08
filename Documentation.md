## Notebook Documentation

| Notebook | Description |
|-|-|
| `Other.ipynb` | Visualization for images of neural network architecture (see Slide 12).<br> **(deprecated)** Uses a Voronoi diagram to segregate areas where the closest shelter to any point in the area is the only shelter in the area. |
| `Models_CNN.ipynb` | CNN to predict the number of shelters in each mesh.<br>Definition of evaluation metric “Rounded accuracy” |
| `Models_BinaryClassification.ipynb` | **(deprecated)** Classifying whether public facilities should act as evacuation shelters or not. See “Data_Imbalance_Amendment.ipynb” for newer models.<br>Uses graph neural networks (*node-level simple GCN, ChebConv, GAT, ArmaConv, graph-level GCN*) and compares it to a dense neural network and RF, XGBoost to not significant improvement. |
| `Models_Pycaret.ipynb` | Uses Pycaret to compare binary classification for different types of ensemble models. *Extra trees classifier* performs the best. |
| `Demonstration.ipynb` | Performs the demonstration of the model on unknown test data in Northern Chiba (see Slides 17-19). |
| `Data_Visualization.ipynb` | **(unsused)** Visualize features across the Tokyo.<br>**(unused)** Visualize how RGB channels appear as a 3D matrix. |
| `Data_Preprocessing3.ipynb` | Takes in data from the script for the Nominatim server.<br>Generates features (x), labels (y) and the adjacency matrix (a).<br>Generates DataFrame of shelters, facilities and the physical features of the mesh it is located in (X_df, df1). |
| `Data_Preprocessing2.ipynb` | Preprocesses mesh data into tabular format (contains mesh features as well as shelter count, shelter capacity). |
| `Data_Preprocessing1.ipynb` | **(deprecated)** same as “Data_Preprocessing1.ipynb” but without preprocessing labels (shelter count). |
| `Data_Imbalance_Amendment.ipynb` | Dimensionality reduction (PCA, t-SNE) for visualization features of positive (shelter) and negative (facility not shelter) classes. Conclusion drawn: there are not any defining mesh features that sets the classes apart.<br><br>Binary classification using dense neural network, RF, XGBoost with SMOTE, Boruta feature selection, Grid search (see Slide 11-12).<br><br>Confusion matrices generated for RF, XGBoost (see Slide 15-16)<br><br>Test on unknown test (specifically Chiba and Ibaraki) to test generalizability. Conclusion drawn: after training model on recall, the model biases toward generating false negative (majority class), see Slide 16.
| `Community_Detection.ipynb` | **(unused)** Uses Cosine similarity for mesh features to create communities of meshes with similar features. |
