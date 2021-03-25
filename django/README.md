##########  README.md  ###########
How to add static files to django?

1) Start with settings.py:

import os

```
INSTALLED_APPS = [
  ...
  'new_app.apps.New_appConfig'
  ...
  ]
  ```
``` 
STATIC_URL = '/static/'                                  ## this is by default
STATICFILES_DIRS = [ os.path.join(BASE_DIR, "static"), ]  ## this is new
```

2) Create /static/<app_name>/ folder same way /templates/<app_name> is made.
   Add css, jpg and other folders and files there.

3) In html template add:
```
{% load static %}
<link rel="stylesheet" href="{% static '/css/style.css' %}">
<img src="{% static '/img/cat.jpg' %}">
```
