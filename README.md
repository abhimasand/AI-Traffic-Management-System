# AI-Traffic-Control-System

## Summary 
This project aims to bring AI to the Traffic controlling network. 

In metropolitan cities, where Traffic is one of the biggest contributing factors of daily commute, traffic network of most countries isn't upto par. This project aims to showcase a proof-of-concept to optimize the traffic network based on the amount of traffic using nothing but cameras. 

Setup: 
1. Cameras are placed at every red light which are overlooking the road(can be captured using existing speed cameras placed at red lights). 
2. Run script, as simple as that. 

Working: 
This script captures realtime video streams from all the cameras, and then predicts the amount of traffic at the each part segment of the intersection. Using this data, the traffic network can be optimized to allow more time to the segments with higher traffic, and less time to the ones with lower traffic, without the need of any kind of traffic police to be present in order to change the timing of the lights.

This can help in reducing the amount of delay commuters have to face, even when some segments of the intersection are empty. Secondly, it can help in managing traffic dynamically, even in high density timing, reducing the chance of gridlock, and subsequently human intervention being needed. 

Model Predictions: 

High Traffic 

![Image of High Traffic](https://github.com/Mashex/AI-Traffic-Control-System/blob/master/images/images_235.jpg)

Low Traffic 

![Image of Low Traffic](https://github.com/Mashex/AI-Traffic-Control-System/blob/master/images/images_699.jpg)

## Getting Started

```python 
python main.py
```
