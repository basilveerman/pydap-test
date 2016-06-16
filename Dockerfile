FROM pcic/geospatial-python

MAINTAINER Basil Veerman <bveerman@uvic.ca>

ADD . /app
WORKDIR /app

RUN pip install -U pip && \
	pip install -i http://tools.pacificclimate.org/pypiserver/ -r requirements.txt
	
EXPOSE 8001

CMD python wsgi.py -p 8001 -i 0.0.0.0 -c pydap_config.yaml