dumpdata:
	python manage.py dumpdata app_gerenciador.projeto --indent 4 > fixtures/projeto.json
	python manage.py dumpdata app_gerenciador.material --indent 4 > fixtures/material.json

dumpdata-windows:
	python -Xutf8 manage.py dumpdata app_gerenciador.projeto --indent 4 > fixtures/projeto.json
	python -Xutf8 manage.py dumpdata app_gerenciador.material --indent 4 > fixtures/material.json

loaddata:
	python manage.py loaddata fixtures/material.json --app app_gerenciador.material
	python manage.py loaddata fixtures/projeto.json --app app_gerenciador.projeto