FROM postgres:13


RUN apt-get update && \
    apt-get install -y locales && \
    echo "tr_TR.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen tr_TR.UTF-8 && \
    update-locale LANG=tr_TR.UTF-8 LC_ALL=tr_TR.UTF-8 && \
    apt-get install -y postgis postgresql-13-postgis-3 && \
    rm -rf /var/lib/apt/lists/*

ENV LANG tr_TR.UTF-8
ENV LANGUAGE tr_TR:tr
ENV LC_ALL tr_TR.UTF-8

COPY init.sql /docker-entrypoint-initdb.d/init.sql
COPY postgresql.conf /etc/postgresql/postgresql.conf
COPY pg_hba.conf /etc/postgresql/pg_hba.conf

CMD ["postgres", "-c", "config_file=/etc/postgresql/postgresql.conf"]