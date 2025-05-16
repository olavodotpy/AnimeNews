## Documentation
### For information, read the [```docs```](https://github.com/olavodotpy/AnimeNews/tree/Master/docs) folder in the correct order

## Clone, deploy on localhost

Do ```git clone``` the application in HTTPS, SSH or CLI:

Example in SSH

```git clone git@github.com:olavodotpy/AnimeNews.git```

Create a develop branch that tracks the origin/develop of the repository:

```git checkout -b develop origin/develop```

Create a virtual environment:

```python -m venv venv```

Enter/activate your environment with:

```source venv/bin/activate```

To exit/deactivate, run:

```deactivate```

Do an install of the manifest file:

```pip install -r requirements.txt```

run ```main.py``` using fastapi:

```fastapi dev src/animenews/main.py```

Make a good implementation and send a PR to the develop branch 😊