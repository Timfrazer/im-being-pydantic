# FastAPI & Pydantic
FastAPI is a microframework similar to Flask, which utilizes pydantic models heavily. It also leans heavily on Starlette, a lightweight ASGI framework/toolkit, which is ideal for building high-performance asyncio services in python.

By using Pydantic It can also generate OpenAPI-specifications from your application based on your Pydantic models.

This gives you  framework-agnostic models while still being able to leverage tight integration with a modern and easy to use framework. If you're going to start a new API-project, I highly recommend trying FastAPI; yes I am biased...

## Slides
To view the notebook as slides just run the following.
` jupyter nbconvert pydantic.ipynb --to slides --post serve`
~~~~