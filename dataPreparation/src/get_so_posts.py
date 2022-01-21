from stackapi import StackAPI
from stackapi import StackAPIError
import json
from os import getenv
from os import walk
from os.path import join
import random


def create_json_dump(so_post, file_name):
    with open('../data/json_files/{}.json'.format(file_name), 'w') as jsonfile:
        json.dump(so_post, jsonfile)
    
    
def collect_posts(list_of_ids):
    SITE = StackAPI(name='stackoverflow', key=getenv('so-api'))
    SITE.page_size = 20
    SITE.max_pages = 1
    
    list_of_ids = list(map(int, list_of_ids))
    for index in range(0, len(list_of_ids), 10):
        question_ids = list_of_ids[index:index+10]
        try:
            # filter 1: no score and dates !)cBhkfq9)pz4k95L0UC_fYuErQDp7k-v2uYVTr70bNKR1
            # filter 2: with score and dates !-)hY(U*C9mr.KDUQOI49MrQGp7QBIm8Lpmf-PXr1rmB3RkxeimNiCu*Lza
            questions = SITE.fetch('questions', ids=question_ids, filter='!-)hY(U*C9mr.KDUQOI49MrQGp7QBIm8Lpmf-PXr1rmB3RkxeimNiCu*Lza')
            
            items = questions.get('items')
            
            if items is not None:
                for item in items:
                    
                    # dump the SO post to a JSON file (for reproducibility)
                    create_json_dump(item, item['question_id'])
        
        except StackAPIError as e:
            print('Error code:{}'.format(e.code))
            print('Error message:{}'.format(e.message))


def select_random_questions():
    files_already_read = []
    new_files_to_read = []
    
    for root, dir, files in walk('../data/json_files'):
        for f in files:
            files_already_read.append(f.split('.')[0]) 
        
    for root, dir, files in walk('../data/question_ids'):
        for name in files:
            count = 0
            with open(join(root, name), 'r') as f:
                lines = f.readlines()
                while count < 67:
                    random_item = random.choice(lines).strip()
                    
                    if random_item in files_already_read:
                        continue
                    else:
                        if random_item not in new_files_to_read:
                            new_files_to_read.append(random_item)
                            count += 1
    
    # print(new_files_to_read)
    return new_files_to_read


def main():

    question_ids = select_random_questions()

    with open('../data/current_so_posts.txt', 'w') as f:
        for question_id in question_ids:
            f.write("%s\n" % question_id)

    collect_posts(question_ids)
    

if __name__ == "__main__":
    main()
