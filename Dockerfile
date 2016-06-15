FROM pcic/geospatial-python

MAINTAINER Basil Veerman <bveerman@uvic.ca>

ADD . /app
WORKDIR /app

RUN pip install -U pip && \
	pip install -i http://tools.pacificclimate.org/pypiserver/ -r requirements.txt
	
EXPOSE 8001

CMD python /usr/local/lib/python2.7/dist-packages/pydap/wsgi/app.py --ip 0.0.0.0 ./pydap_config.yaml
