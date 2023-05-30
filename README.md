# elastic_search_dj_example

Examples on Django + haystack + elastic search

Requirements:

Django
Elastic Search (required version 7.x.x)
Drf Haystack

```
Project Setup
$ mkdir dj_elastic && cd dj_elastic
$ python3 -m venv env
$ source env/bin/activate
$ poetry install
```
project directory should look like:

```
── dj_elastic
├── main
│ ├── **init**.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── manage.py
└── commons
└── templates
├── search
├── indexes
├── searches
├── hotel_text.txt
├── hoteladdress_text.txt
├── hotelimage_text.txt
├── hotelspecificationvalue_text.txt
├── **init**.py
```

```
python manage.py rebuild_index
```
