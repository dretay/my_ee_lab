.PHONY: jupyter
.PHONY: pythondeps

Pipfile.lock: Pipfile
	( \
		pipenv install \
		pipenv run jupyter lab build \
		#pipenv run "jupyter labextension install @jupyter-widgets/jupyterlab-manager" \
		pipenv run jupyter labextension install jupyter-matplotlib \
	)
jupyter: Pipfile.lock
	( \
		pipenv run jupyter-lab notebooks/ --allow-root --no-mathjax --ip=0.0.0.0 --port=8888 --no-browser --NotebookApp.token='' \
	)
