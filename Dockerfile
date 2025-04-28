FROM openanolis/anolisos:23

MAINTAINER Jun He<jun.he@arm.com>

RUN \
    # Install packages
    dnf updateinfo && dnf update -y && \
    dnf install -y --setopt=install_weak_deps=False \
        git unzip python3-pip \
        glibc-langpack-en glibc-langpack-zh && \
    dnf clean all && \
    # add default user
    groupadd -g 1000 builder && \
    useradd -m -s /bin/bash -u 1000 -g 1000 builder

COPY . /opt/migrate-ease
RUN chown -R builder:builder /opt/migrate-ease && \
    su - builder -c 'pip3 install -r /opt/migrate-ease/requirements.txt'

WORKDIR /opt/migrate-ease
USER builder
ENV TERM=xterm
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV PYTHONPATH /opt/migrate-ease

# Start web server by default
CMD ["python3", "web/server.py"]
