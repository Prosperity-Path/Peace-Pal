# Peace-Pal
A Python use-case of the [Prosperity Development Kit](https://github.com/Prosperity-Path/PDK) to help users find more inner peace.
Peace Pal serves up exercises that include content to nudge users towards more peace, as well as using an emotion labeling model to serve relevant content snippets designed to assuage uneasiness.

Running the PDK is a prerequisite.

Then, to get started, install the required packages in `requirements.txt`. Feel free to use a virtual environment.
```
pip install -r requirements.txt
```
The core requirement to make an app that uses the PDK is to have a REST API with 4 post end points. This app's API uses [Fast API](https://github.com/tiangolo/fastapi).
In order to run the app in development, we'll need to install [uvicorn](https://www.uvicorn.org/) with `pip install uvicorn`.
```
uvicorn main:app --reload
```
Note that the app will install TensorFlow and some models that are fairly bulky. So if you're setting this repo up, you should be prepared to allocate a bit more than 1GB of disk space.
