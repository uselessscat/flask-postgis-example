# Adapted from 
# https://github.com/appropriate/docker-postgis/tree/master/11-2.5
FROM postgres:12

ENV POSTGIS_MAJOR 3
ENV POSTGIS_VERSION 3.0.0+dfsg-2~exp1.pgdg100+1

RUN apt update \
    && apt-cache showpkg postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR \
    && apt-get install -y --no-install-recommends \
        postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR=$POSTGIS_VERSION \
        postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR-scripts=$POSTGIS_VERSION \
        postgis=$POSTGIS_VERSION \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /docker-entrypoint-initdb.d

COPY ./configs/initdb-postgis.sh /docker-entrypoint-initdb.d/postgis.sh
COPY ./configs/update-postgis.sh /usr/local/bin