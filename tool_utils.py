import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "summaryAnnotator.settings")

import django
django.setup()

from django.core.management import call_command

from django.contrib.auth.hashers import make_password, check_password 
from django.contrib.auth import get_user_model
from Task.models import SummaryTask
import pandas as pd
from tqdm import tqdm 
import sys 

User = get_user_model()

def make_user(username, email, password):
    user = User(email = email, username= username, password =make_password(password))
    user.save()
    return user

def make_annotation_sample(summary_id, title, gold, summary):
    task = SummaryTask()
    task.summaryID = int(summary_id)
    task.title = title 
    task.gold = gold 
    task.article = summary
    task.save()

def make_bulk_entry(file_name):
    data = pd.read_csv(file_name)
    for idx, row in tqdm(data.iterrows()):
        if idx > 1000:
            break
        idx, title, gold, bart_summaries = row['idx'], row['title'], row['gold'], row['bart_summaries']
        make_annotation_sample(idx, title, gold, bart_summaries)

def allocate_smmaries(user, n):
    pks = SummaryTask.objects.filter(annotator = None).values_list('pk', flat=True)
    if len(pks) > n: 
        pks = pks[:n]
    print(f'[log] {len(pks)} unallocated samples found.')

    SummaryTask.objects.select_for_update().filter(pk__in = pks).update(
        annotator = user
    )
    print('[log] summaries allocated. ')


def create_user_and_allocate_summaries(username, email, password, n):
    user = make_user(username, email, password)
    print('[log] user created.')
    allocate_smmaries(user, n)

def bulk_allocate_existing_user(username, n):
    user = User.objects.filter(username = username).first()
    print('[log] user found.')
    allocate_smmaries(user, n)

def generate_csv(filename): 
    done_articles = SummaryTask.objects.exclude(annotator = None).filter(done=True)
    summaryID, article, gold, title, grammatical_correctness, arrangement, quality, singlePoint, enoughDetails, subjectiveScore, done, annotator = [], [], [], [], [], [], [], [], [], [], [], []
    for item in done_articles: 
        summaryID.append(item.summaryID)
        article.append(item.article)
        gold.append(item.gold)
        title.append(item.title)
        grammatical_correctness.append(item.grammatical_correctness)
        arrangement.append(item.arrangement)
        quality.append(item.quality)
        singlePoint.append(item.singlePoint)
        enoughDetails.append(item.enoughDetails)
        subjectiveScore.append(item.subjectiveScore)
        done.append(item.done)
        annotator.append(item.annotator.username)

    df = pd.DataFrame({
        'summaryID': summaryID,
        'candidate': article, 
        'gold' : gold, 
        'title': title, 
        'grammatical_correctness': grammatical_correctness, 
        'arrangement': arrangement, 
        'quality': quality, 
        'conciseness': singlePoint, 
        'exhaustiveness': enoughDetails, 
        'subjectiveScore': subjectiveScore, 
        'done': done,
        'annotator':annotator
    })

    df.to_csv(filename)
    
if __name__ == '__main__':
    tasks = ["bulk_entry", "bulk_allocate", "bulk_allocate_to_existing", "export", "help"]
    task = None
    
    # bulk_entry 
    file_name = None

    # bulk allocate 
    username = None 
    email = None 
    password = None 
    n = None 

    # export 
    filename = None
    try: 
        task = str(sys.argv[1])
        if task == tasks[0]: 
            file_name = str(sys.argv[2])
            make_bulk_entry(file_name)

        elif task == tasks[1]:
            username = str(sys.argv[2])
            email = str(sys.argv[3])
            password = str(sys.argv[4])
            n = int(str(sys.argv[5]))
            create_user_and_allocate_summaries(username, email, password, n)
        
        elif task == tasks[2]:
            username = str(sys.argv[2])
            n = int(str(sys.argv[3]))
            bulk_allocate_existing_user(username, n)

        elif task == tasks[3]: 
            filename = str(sys.argv[2])
            generate_csv(filename)

        elif task == tasks[4]:
            print("supported functions: ")
            print(f"\t1. {tasks[0]} [csv_file_name]")
            print(f"\t2. {tasks[1]} [username] [email] [password] [n]")
            print(f"\t3. {tasks[2]} [username] [n]")
            print(f"\t4. {tasks[3]} [filename]")
            print(f"\t5. {tasks[4]}")
        else: 
            raise Exception('Not supported operation')
    except Exception as e: 
        if task == None: 
            print(f'Task {tasks} not specified.')
        
        elif task == tasks[0]:
            if file_name == None:
                print(f'{tasks[0]}: filename not provided.')
        
        elif task == task[1]:
            if username == None:
                print(f'{tasks[1]}: username not provided.')
            elif email == None:
                print(f'{tasks[1]}: email not provided.')
            elif password == None: 
                print(f'{tasks[1]}: password not provided.')
            elif n == None:
                print(f'{tasks[1]}: n not provided.')
        elif task == task[2]:
            if username == None: 
                print(f'{tasks[2]}: username not provided.')
            elif n == None: 
                print(f'{tasks[2]}: n not provided.')

        elif task == task[3]: 
            if filename == None: 
                print(f'{tasks[3]}: filename not provided.')
        else:
            print(f'Exception: {e}')
