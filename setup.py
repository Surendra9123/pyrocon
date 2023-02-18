import os
from setuptools import setup
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

pkg2 = os.getcwd()
print(read('README.md'))
setup(
    name = "",
    version = "1.0.6",
    author = "SPiDER",
    author_email = "mindajitendra63@gmail.com",
    description = ("Easy conversation handler for pyrogram mtproto library {for bots only}"),
    license = "BSD",
    keywords = "example documentation tutorial",
    long_description = read('README.md'),
    long_description_content_type='text/markdown',
    url = "https://github.com/Surendra9123/Pyrogram-Conversation",
    packages=["pyrocon"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ])