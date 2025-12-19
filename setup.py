from setuptools import find_packages, setup

setup(
    name="QAsystem",
    version="0.0.0",
    author="Divyanshu Chauhan",
    author_email="divyanshuchauhan471@gmail.com",
    packages=find_packages(),
    install_requires=["pinecone-haystack","haystack-ai","fastapi","uvicorn","python-dotenv","pathlib"]
)