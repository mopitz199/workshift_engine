FROM python:3
COPY . /src
RUN pip install -U sphinx
RUN pip install -U pytest
RUN pip install -U sphinx_rtd_theme
RUN pip install mypy