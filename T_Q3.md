## 2D Grid 
* Hausdorff Distance measures the maximum distance between any point on one path and the closest point on the other path. This captures the overall similarity of the paths, considering their shape and relative positions.
  
Why Hausdorff Distance is better:
* Intuitive and meaningful: It directly measures the "distance" between paths, considering their shapes and positions.
* Robust to minor variations: It can handle small variations in path shapes without drastically increasing the distance.
* Independent of path parametrization: The distance is calculated based on the points themselves, not on the order in which they are traversed.
  
Drawbacks of ther metrics:
* Euclidean distance between start/end points: Ignores the path's shape entirely, potentially leading to misleading comparisons.
* Manhattan distance between start/end points: Similar to Euclidean distance, ignores the shape of the paths.
* Path length difference: Only considers the total path length, not their relative positions.

## Transformers
Fortunately this entire topic was covered by 3Blue1brown in his video :) :)

  
  
