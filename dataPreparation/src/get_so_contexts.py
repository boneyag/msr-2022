import json
import csv
import os
import string
from datetime import datetime

from nltk import bigrams, trigrams
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import pos_tag

from corenlp_helper import *
from so_helper import get_paragraphs

eng_stopwords = stopwords.words('english')
lemmatizer = WordNetLemmatizer()

def read_witt_tags():
    with open('../software-technologies-tags.txt') as tagfile:
        tags = tagfile.readlines()
        
        for i in range(len(tags)):
            pattern = re.compile(r'\b([a-z]+)(\d+(\.\d+)*)([a-z]+)?\b')
            tags[i] = re.sub('-', ' ', tags[i]).strip()
            tags[i] = re.sub(pattern, r'\1 \2 \4', tags[i].strip())

    return tags


def get_so_tags(sentence, so_tags):
    matching_tags = []
    
    sentence = re.sub(r'[+,]','', sentence)
    sentence = re.sub(r'[-]',' ', sentence)
    sentence = re.sub('(\d+(\.\d+)?)', r' \1', sentence).strip() # if a space missing before version number add one
    
    words = sentence.lower().split()
    words = [w for w in words if w not in eng_stopwords]
     
    bigram_words = bigrams(words)
    trigram_words = trigrams(words)
     
    for item in words:
        if item in so_tags:
            matching_tags.append(item)
            
    for item in bigram_words:
        if re.search(r'^(\d+\.?)+', item[1]):
            if item[0]+' '+item[1] in so_tags:
                matching_tags.append(item[0]+' '+item[1])
            elif item[0] in so_tags and item[0] not in matching_tags:
                matching_tags.append(item[0])
        else:
            if item[0]+' '+item[1] in so_tags:
                matching_tags.append(item[0]+' '+item[1])
    
    for item in trigram_words:
        if re.search(r'^(\d+\.?)+', item[2]):
            if item[0]+' '+item[1]+' '+item[2] in so_tags:
                matching_tags.append(item[0]+' '+item[1]+' '+item[2])
            elif item[0]+' '+item[1] in so_tags and item[0]+' '+item[1] not in matching_tags:
                matching_tags.append(item[0]+' '+item[1])
        else:
            if item[0]+' '+item[1]+' '+item[2] in so_tags:
                matching_tags.append(item[0]+' '+item[1]+' '+item[2])
           
    return matching_tags


def get_nonfunctional_words(sentence, non_func):
    matching_words = []
    
    lemmatized_words = []

    sentence = sentence.translate(str.maketrans('', '', string.punctuation))

    for token, pos in pos_tag([i for i in sentence.strip().split(' ') if i]):
        lemmatized_words.append(lemmatizer.lemmatize(token, get_wordnet_pos(pos)))
    
    words = [word for word in lemmatized_words if word not in eng_stopwords]
    
    for w in words:
        if w in non_func:
            matching_words.append(w) 
         
    return matching_words


def find_tag_occurences_in_sentences():
    """Collecting sentences in questions, answers, and comments from JSON dumps"""
    init_corenlp()
    
    so_tags = read_witt_tags()
    
    current_so_posts = []

    # collect statistics
    number_of_answer_sentences = 0
    number_of_answer_comment_sentences = 0
    number_of_answer_sentences_with_context = 0
    number_of_answer_comment_sentences_with_context = 0
    number_of_question_comment_sentences = 0
    number_of_question_comment_sentences_with_context = 0

    with open('../data/current_so_posts.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            current_so_posts.append(line.strip())
  
    with open('../data/RandomThread9.csv', 'w', newline='') as csvfile:
        so_sentence_writer = csv.writer(csvfile, delimiter=',')
        header = ["QuestionId", "AnswerId", "AnswerScore", "AnswerLastActivity", "CommentId", "CommentScore",
                  "CommentDate", "ParagraphIndex", "SentenceIndex", "Sentence", "AugQuestionTags", "SentenceTags"]
        so_sentence_writer.writerow(header)
  
        for root, dirs, files in os.walk('../data/json_files'):
            for name in files:
                if name.split('.')[0] in current_so_posts: # ignore files from previous iterations
                    print(os.path.join(root, name))
                    with open(os.path.join(root, name), 'r') as f:
                        so_post = json.load(f)
                        # so_post = content['items'][0]

                        question_tags = so_post['tags']
                        
                        # Aug 25, 2021 meeting: interested in answers and comments
                        # Aug 25, 2021 meeting: sentence is interesting if sentence tag does not overlap with question tags

                        paragraphs = get_paragraphs(so_post['body'])
                        if paragraphs is not None:
                            for paragraph_index, paragraph in enumerate(paragraphs):
                                sentences = get_all_paragraph_sentences2(paragraph)
                                for sentence_index, sentence in enumerate(sentences):
                                    st = get_so_tags(sentence, so_tags)

                                    # add only new tags
                                    for t in st:
                                        if t not in question_tags:
                                            question_tags.append(t)

                        tags = ' ,'.join(list(set(question_tags))).strip()


                        if 'answers' in so_post.keys():
                            for answer in so_post['answers']:
                                paragraphs = get_paragraphs(answer['body'])
                                if paragraphs is not None:
                                    for paragraph_index, paragraph in enumerate(paragraphs):
                                        sentences = get_all_paragraph_sentences2(paragraph)
                                        for sentence_index, sentence in enumerate(sentences):
                                            number_of_answer_sentences += 1

                                            st = get_so_tags(sentence, so_tags)

                                            # non-overlapping tags with question tags
                                            no_tags = list(set(st) - (set(question_tags)))
                                            answer_last_edited_date = datetime.fromtimestamp(answer['last_activity_date']).\
                                                strftime('%d-%m-%y')

                                            if len(no_tags) > 0:
                                                number_of_answer_sentences_with_context += 1

                                            if len(no_tags) > 0:
                                                for i in range(len(no_tags)):
                                                    if i == 0:
                                                        line = [so_post['question_id'], answer['answer_id'],
                                                                answer['score'], answer_last_edited_date, '', '', '',
                                                                paragraph_index, sentence_index, sentence, tags,
                                                                no_tags[i]]
                                                    else:
                                                        line = ['', '', '', '', '', '', '', '', '', sentence, '',
                                                                no_tags[i]]
                                                        
                                                    so_sentence_writer.writerow(line)


                                # process the comments of the answer
                                if 'comments' in answer.keys():
                                    for comment in answer['comments']:
                                        paragraphs = get_paragraphs(comment['body'])
                                        if paragraphs is not None:
                                            for paragraph_index, paragraph in enumerate(paragraphs):
                                                sentences = get_all_paragraph_sentences2(paragraph)
                                                for sentence_index, sentence in enumerate(sentences):
                                                    number_of_answer_comment_sentences += 1

                                                    st = get_so_tags(sentence, so_tags)

                                                    # non-overlapping tags with question tags
                                                    no_tags = list(set(st) - (set(question_tags)))
                                                    comment_creation_date = datetime.fromtimestamp(
                                                        comment['creation_date']). strftime('%d-%m-%y')

                                                    if len(no_tags) > 0:
                                                        number_of_answer_comment_sentences_with_context += 1

                                                    if comment['post_id'] == answer['answer_id']:
                                                        if len(no_tags) > 0:
                                                            for i in range(len(no_tags)):
                                                                if i == 0:
                                                                    line = [so_post['question_id'], answer['answer_id'],
                                                                            '', '', comment['comment_id'],
                                                                            comment['score'], comment_creation_date,
                                                                            paragraph_index, sentence_index, sentence,
                                                                            tags, no_tags[i]]
                                                                else:
                                                                    line = ['', '', '', '', '','', '', '', '', sentence,
                                                                            '', no_tags[i]]

                                                                so_sentence_writer.writerow(line)

                        if 'comments' in so_post.keys():
                            for comment in so_post['comments']:
                                paragraphs = get_paragraphs(comment['body'])
                                if paragraphs is not None:
                                    for paragraph_index, paragraph in enumerate(paragraphs):
                                        sentences = get_all_paragraph_sentences2(paragraph)
                                        for sentence_index, sentence in enumerate(sentences):
                                            number_of_question_comment_sentences += 1

                                            st = get_so_tags(sentence, so_tags)

                                            # non-overlapping tags with question tags
                                            no_tags = list(set(st) - (set(question_tags)))
                                            comment_creation_date = datetime.fromtimestamp(
                                                        comment['creation_date']). strftime('%d-%m-%y')

                                            if len(no_tags) > 0:
                                                number_of_question_comment_sentences_with_context += 1

                                            if comment['post_id'] == so_post['question_id']:
                                                if len(no_tags) > 0:
                                                    for i in range(len(no_tags)):
                                                        if i == 0:
                                                            line = [comment['post_id'], '', '', '',
                                                                    comment['comment_id'], comment['score'],
                                                                    comment_creation_date, paragraph_index,
                                                                    sentence_index, sentence, tags, no_tags[i]]
                                                        else:
                                                            line = ['', '', '', '', '', '', '', '', '', sentence, '',
                                                                    no_tags[i]]
                                                            
                                                        so_sentence_writer.writerow(line)

    with open('../data/current_so_stats_x.txt', 'w') as f:
        f.write("Annotation round - VII\n\n")
        f.write("Total number of answer sentences processed: {}\n".format(number_of_answer_sentences))
        f.write("Total number of answer comments processed: {}\n".format(number_of_answer_comment_sentences))
        f.write("Total number of question comments processed: {}\n".format(number_of_question_comment_sentences))
        f.write("Total number of candidate answer sentences extracted: {}\n".format(
            number_of_answer_sentences_with_context))
        f.write("Total number of candidate answer comment sentences extracted: {}\n".format(
            number_of_answer_comment_sentences_with_context))
        f.write("Total number of candidate question comment sentences extracted: {}\n".format(
            number_of_question_comment_sentences_with_context))


def main():
    find_tag_occurences_in_sentences()
    

if __name__ == '__main__':
    main()
