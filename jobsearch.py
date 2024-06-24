import requests
from twilio.rest import Client



URL = 'https://remoteok.com/api'
keys = ['date', 'company', 'position', 'tags', 'location', 'url']

wanted_tags =['python']

def get_jobs():
    response = requests.get(URL)
    job_results = response.json()
    #print(job_results)
    jobs = []
    for job_result in job_results:
        #print(job_result)
        job ={k:v for k, v in job_result.items() if k in keys}
        if job:
            #print(job)
            tags = job.get('tags')
            tags= {tag.lower() for tag in tags}
            if "react" in tags:
                jobs.append(job)
                print(jobs)
                
    return jobs


def send_whatsapp_text(jobs):
    from_whatsapp_number='whatsapp:<send_number>', 
    account_sid = '<account_sid>' 
    auth_token = '<auth_token>' 
    to_whatsapp_number = 'whatsapp:<reciever_number>'
    client = Client(account_sid, auth_token) 
    for job in jobs:
        message = f"""
                Hi Mark, We got new jobs for you.
                date = {job.get('date')}
                company ={job.get('company')}
                url = {job.get('url')}
                position = {job.get('position')}
                location ={job.get('location')}
        """
        msg = client.messages.create(
            body = message, from_ = from_whatsapp_number, to= to_whatsapp_number
        )
        #print(message.sid)
      
 
 


 

 
send_whatsapp_text(get_jobs())
    
