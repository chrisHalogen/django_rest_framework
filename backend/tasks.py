from celery import task
import time
import requests

@task()
def first_async_task():
    time.sleep(5)
    print("Hello Async")

@task()
def populate_dog():
	url = "https://dog.ceo/api/breeds/image/random"
	try:
		res = requests.get(url)
	except requests.ConnectionError as e:
		raise Exception("Failed Operation", e)

	if res.status_code in [200,201]:
		data = res.json()
		image_url = data.get("message","")
		from api.models import Dog
		Dog.objects.create(url=image_url)