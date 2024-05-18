Note : A colab file is attached below

## 2D Grid 
* Hausdorff Distance measures the maximum distance between any point on one path and the closest point on the other path. This captures the overall similarity of the paths, considering their shape and relative positions.
  
Why Hausdorff Distance is better:
* Intuitive and meaningful: It directly measures the "distance" between paths, considering their shapes and positions.
* Constant to minor variations: It can handle small variations in path shapes without drastically increasing the distance.
* Independent of path parametrization: The distance is calculated based on the points themselves, not on the order in which they are traversed.
  
Drawbacks of ther metrics:
* Euclidean distance between start/end points: Ignores the path's shape entirely, potentially leading to misleading comparisons.
* Manhattan distance between start/end points: Similar to Euclidean distance, ignores the shape of the paths.
* Path length difference: Only considers the total path length, not their relative positions.

## Transformers
Fortunately this entire topic was covered by 3Blue1brown in his video :) :)
### Word embedding basics:
* embeddings take words from our natural language and represent them as points in a high-dimensional space. Each dimension and direction of this space captures some aspect of the word's meaning.
*  Embeddings are often learned by training a neural network on a massive amount of text data. The network learns to predict the context of a word (the words around it) based on its embedding. This process implicitly captures semantic relationships.

### Measuring Likeliness: Cosine Similarity
* Euclidean Distance vs. Cosine Similarity: In high-dimensional spaces, Euclidean distance (straight-line distance) becomes less meaningful. This is because the "curse of dimensionality" makes all points appear equally distant. Cosine similarity focuses on the angle between vectors instead.
* cosine_similarity(v1, v2) = (v1 . v2) / (||v1|| ||v2||)

## visualisation 

  * Self-Trained
  
  * ![image](https://github.com/Devanoper/23B1540_AIC/assets/158256909/a7910d47-cd3c-4956-813d-2908d1ac1919)      

  
  * Pre-Trained model

  
  * ![image](https://github.com/Devanoper/23B1540_AIC/assets/158256909/3cf83b66-9e87-4c2a-939a-1b6644654570)


  * Colab File corresponding to it : https://colab.research.google.com/drive/1CUg91TMJEXr_hqT-vG4J1ngJoo9gtg_0?usp=sharing

  
