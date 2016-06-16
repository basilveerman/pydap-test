# pydap-test

## Install

Aquire or build the container:

```bash
git clone https://github.com/pacificclimate/pydap-test
cd pydap-test
sudo docker build -t pcic/pydap-test
```

Or

```bash
docker pull pcic/pydap-test # Not an automated build, may not be most recent build
```

## Deploy

```bash
sudo docker run --name pydap-test -p 8001:8001 -v <data_location>:/data pcic/pydap-test
```

## Use

Go to `http://localhost:8001/catalog.json`. From the list of presented URLs, you can load the results of various handlers by going to <catalog_url>.<handler_key>. For example, the DDS response response would be <catalog_url>.dds, the DAS response <catalog_url>.das, and the html reponse at <catalog_url>.html.

With multidimensional NetCDF data, you can request specific variables and hyperslabs using OpenDAP syntax, eg <catalog_url>.nc?<variable_name>[0:10][0:10][0:10]
