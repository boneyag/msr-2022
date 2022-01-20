## Extracting Essential Sentences from Stack Overflow Answers

When preparing the data for annotation, you may want to ease the burden on annotators. Therefore, we use a script to remove sentences that do not contain potential additional contexts.

### Prerequisites

* This code uses `python3`. Make sure you have python > 3.0 installed
* The list of python packages used can be found in `requirements.txt`. You can individually install them or do `pip3 install -r requirements.txt`

### How to Run

1. Create a StackExchange application key to be able to use the higher query limit at [https://stackapps.com/apps/oauth/register](StackExchange). 
2. In the project root directory (dataPreparation), create a file `.env`. Add the line `so-api = 'ADD_YOUR_KEY'` to the file with your key.
3. The data directory contains two sub-directories: json_files, question_ids.
    3.1. question_ids contains three text files (json.txt, django.txt, and regex.txt). You can run the get_so_post.py to randomly pick question IDs from the files and extract data from the StackExchange API. The process create json dumps for each question in json_file directory. Since we kept a copy of our data, you may want to keep a copy of them when creating a new file. This process also create a text file that logs all the question IDs that extracted.
    4.2. To prepare data, run the get_so_context.py file. This script uses the current_so_post.txt file that created by get_so_post.py to identify the question ID process in each round. This way, you can have multiple rounds of annotations without conflicting with already collected data. The process generates a csv file. Which can be used to create a proper spreadsheet.  

