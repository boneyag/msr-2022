## Preparing data for annotation (Methodology - Phase 1)

When preparing the data for annotation, you may want to ease the burden on annotators. Therefore, we use a script to remove sentences that do not contain potential additional contexts.

### Prerequisites

* This code uses `python3`. Make sure you have python > 3.0 installed
* The list of python packages used can be found in `requirements.txt`. You can individually install them or do `pip3 install -r requirements.txt`

### How to Run

1. Create a StackExchange application key to be able to use the higher query limit at [https://stackapps.com/apps/oauth/register](StackExchange). 
2. In the project root directory (dataPreparation), create a file `.env`. Add the line `so-api = 'ADD_YOUR_KEY'` to the file with your key.
3. The data directory contains two sub-directories: json_files, question_ids.
    3.1. question_ids contains three text files (json.txt, django.txt, and regex.txt). 
    3.2. json_files contains JSON dumps of questions used in our study.  
    3.3. question_ids.txt contains all the IDs used in our study. To replicate the study, use this file when running get_so_context.py instead of collecting own random question IDs.
4. The src directory contains four scripts. `so_helper.py` and `corenlp_helper.py` contain supporing functions to process natural language text. 
    4.1. Running the get_so_post.py, randomly collect question IDs from the text files (mentioned in 3.1). It extracts data from the StackExchange API. The process creates json dumps for each question in json_file directory. To avoid conflicts with existing files, when running the script to create your own dataset, clean the json_file directory first.
    4.2. Running the get_so_context.py, process sentences to fetch candidate sentences. The process creates a csv file which can be used to generate an spreadsheet to collect annotations.

### Stanford CoreNLP support
We use Stanfod CoreNLP to process text. [Download](https://stanfordnlp.github.io/CoreNLP/download.html) the server and extract it in the project root. Run the following command in the Stanford CoreNLP server directory to start the server, `java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000`. Without this get_so_context.py cannot run.
