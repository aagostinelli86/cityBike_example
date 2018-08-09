Please find the cluster analysis of CityBikes, ran by Andrea Agostinelli (andr.agostinelli@gmail.com)

In order to produce the html files stored in the results folder, please make sure to 
use the same Python3 environment as summarised in cityBike_clustering/python/requirements.txt

Once the same environment and package config is guaranteed, please move to:

$ cd cityBike_clustering/python/scripts

and run from the command line, the following line:

$ python runBikeClustering.py arg1

where arg1 is an integer parameter representing the minimum number of desired components in the HDBscan clustering.
The script will output an html file in  
 
$ cd cityBike_clustering/results 

Its output file name contains an integer label referring to the free parameter used when running the script. 


---- Notes on the analysis ----- 

1) In the notebook folder, there is a test notebook in which I implemented the analysis flow 

3) Instead of using a standard kmeans with  the euclidean distance I applied an HDBscan with the Harvesine metrics. The Haversine metric as implemented supports coordinates in radians. That means I needed to convert latitude and longitude data into radians before passing it in to HDBSCAN. Conceptually, it would be wrong to apply an euclidean metrics to data on a sphere (Long, Lat). Of course, for the purpose of this exercises and when comparing the size of a city with respect to the earth surface, there is no significance difference in the evaluation of these distances. Nevertheless, in this way we obtained a more general approach for bigger distances. 

4) In order to run the HDBscan, training & test sets are required, as I recalled with the Warning message. Due to the purpose of this exercise, with clear results, I decided to overfit the observation by running hdbscan.fit_predict() on the same data 

5) A different minimum number of cluster components causes a different clustering. At this level I did not implemented the performance metrics (silhouette score, compactness) since the results are pretty stable by eyes. 

