# sierpinski-polygons
A look at chaos theory, applied with the Turtle Graphics library in Python.

## Installation
Sierpinski_Polygons uses the math, random, and Turtle graphics libraries. All of these are installed with Python, so they should already be on your machine.

## Usage
In a command prompt, run
```
python sierpinski_polygons.py
```

## About the Code
Each shape, other than the base triangle, is broken up into an amount of sectors determined by that shape's number of sides. 

For example: a hexagon will have six sectors.

All sectors are of equal area and are determined by connecting the two closest vertices with the center of the polygon. As the code runs, it will fill in each sector with the Sierpinski pattern, eventually creating a mosiac of fractals.

The level of detail specifies how many points will be plotted on the shape. The more points, the more detail is visible. Level of detail is measured on a scale from 1 to 10. The specified level of detail is multiplied by 1000 to get the total number of points that will be plotted. Lower-end PCs will begin to slow down when there are more than 5000 points present. 

Larger shapes require higher levels of detail to be seen clerly due to the high number of sectors.

## About the Math
This program functions off of a very simple idea to create fractals. When given three verticies on a triangle, the midpoint of a random vertex and a random point will be plotted. Then, the midpoint of the previous point and a random vertex will be plotted, and so and so forth. 

After hundreds of dots have been placed, the distinct Sierpinski pattern emerges. This pattern only becomes more refined as more points are placed.'

## Contributing
This is my first public project, but pull requests are welcome. I am open to discussion, advice, etc.

## License
[MIT](https://choosealicense.com/licenses/mit/)
