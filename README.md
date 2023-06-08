# Peace Pal
This is the companion app to the PDK [Getting Started Guide](https://github.com/Prosperity-Path/PDK/wiki/Getting-Started-Guide).
__________________
Peace Pal is a Python use-case of the [Prosperity Development Kit](https://github.com/Prosperity-Path/PDK) to help users find more inner peace.
Peace Pal serves up exercises that include content to nudge users towards more peace, as well as using an emotion labeling model to serve relevant content snippets designed to assuage uneasiness.

Running the PDK is a prerequisite.

Then, to get started, install the required packages in `requirements.txt`. Feel free to use a virtual environment.
```
pip install -r requirements.txt
```
The core requirement to make an app that uses the PDK is to have a REST API with 4 POST endpoints and 1 GET endpoint. This app's API uses [Fast API](https://github.com/tiangolo/fastapi).
In order to run the app in development, we'll need to install [uvicorn](https://www.uvicorn.org/) with `pip install uvicorn`.
```
uvicorn main:app --reload --port 8080
```
Note that the app will install TensorFlow and some models that are fairly bulky. So if you're setting this repo up, you should be prepared to allocate a bit more than 1GB of disk space.

_______________
### Responses to the [Value-add Driven Test and Dev Framework](https://github.com/Prosperity-Path/Wealth-Building-Content/blob/eed9e6213a13b649f8594636dc6be73aa53f3afa/Value-add-Driven-Testing-and-Dev.md)

**What’s the practical objective that you’re going to reduce friction against?**
* Someone having anxiety that pulls them away from living the stress-free life they want to live.
If there was a digital genie lamp that granted wishes through email, conceiveably a piece of content could help them work through the friction causing the stress.

**What competitive advantage do you have that will reduce friction for a user?**
* Substantial self development than the average person that has results in volume of original writing that has helped bring me a lot more peace. Also a solid understanding of sentiment analysis.

**What triggers the action that reduces friction?**
* An email at the start of the user’s day that uses previously collected information to suggest a new question or content snippet designed to help them. OR the user sending an email update with an explicit request for help. 

**What’s the action [or set of actions] that reduces the friction?**
* An email response that includes an analysis and targeted recommendation to reduce the barriers preventing peace.

**What’s the compounding effect of reducing friction? How is that shown to the user?**
* The recommendations get better and there’s also a roll-up of the accumulated sentiment. 
