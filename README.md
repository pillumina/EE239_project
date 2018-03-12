# EE239_project

http://www.fki.inf.unibe.ch/databases/iam-handwriting-database  download the sentences dataste here, create a folder named dataset and unzip .tgz file into that folder!!

  First off, I just tried the CNN architecture described in that article to implement writers indentification based on IAM handwriting sentences dataset. You may need to download that and create a folder named 'dataset' in this repository and unzip that .tgz file into dataset folder. Or you can check out the code in data_processing.py to re-locate the path of the data you unzip into.
  
  For a better illustration I visualized the data in Recognition_writers.ipynb(check path of data if you want to run the cells). As to input data, I resized each pic to 113 pixels height and created patches of 113 x 113 pics are randomly cropped from each pic, by which the CNN may yield better solution according to that paper.
  
  I used Keras to simplify the building process of the NN model and visualized its architecture in that notebook.
  
  Used checkpoints to save the model so we could use the model later without training it again(a waste of time)
  
  So if we're gonna do some work either on writers identification or word-base/char-base recognition, at least we could find a easier way to load data or try out different models :).
  
  
  
  
  
  
  
  PS: You can create your braches so we can work on that together. For Web Cloud Service like AWS, I was charged $13 by launching instance that exceeds the Free Tie Limits! FeelsBadMan!
