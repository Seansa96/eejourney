2025-02-17 21:00

Status: #baby 

Tags: [[guide]]



rvc ai voice clone setup

Download from the releases [here](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/releases)

Pick the package that is pertinent to your GPU (mine is NVIDIA, for example)

Extract it wherever you want.


Click go-web.bat

Done. Enjoy


# Advanced user


You'll need a Python version between 3.7 and 3.11, non inclusive.

This should come with pip. If it doesn't allow you to use it, you can add it to the system variables.



Now, you'll want to create a venv within the RVC directory. Just do:

```
//replace the python number with your version
python3.10 -m venv myenv
```
Then run myenv\Scripts\activate

to start the virtual environment

then just do `pip install -r requirements.txt`

for it to download all necessary dependencies.






## References:
