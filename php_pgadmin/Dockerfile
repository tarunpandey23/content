RUN apk --no-cache --update add php5-pgsql postgresql && ${DOCKAGE_ETC_DIR}/buildtime/install && cp -ar ${DOCKAGE_ETC_DIR}/etc/* /etc     && rm -rf /var/cache/apk/* ${DOCKAGE_ETC_DIR}/etc ${DOCKAGE_ETC_DIR}/buildtime
ADD dir:f411d38c7169c9f10935c9a97b4a4498a148a701d087845ccd0bd885adb59c5e in /etc/dockage
LABEL maintainer=Mohammad Abdolirad <m.abdolirad@gmail.com> org.label-schema.name=phppgadmin org.label-schema.vendor=Dockage org.label-schema.description=phpPgAdmin Docker image, phpPgAdmin is a web-based administration tool for PostgreSQL. org.label-schema.vcs-url=https://github.com/dockage/phppgadmin org.label-schema.license=MIT
CMD ["app:start"]
ENTRYPOINT ["/sbin/entrypoint"]
WORKDIR /var/www
VOLUME [/data /var/log]
EXPOSE 443/tcp 80/tcp
RUN apk update     && apk --no-cache add nginx php5-fpm     && runit-enable-service nginx     && runit-enable-service php-fpm     && chown nginx:nginx ${DOCKAGE_WEBROOT_DIR}     && mv ${DOCKAGE_ETC_DIR}/sbin/* /sbin     && rm -rf /var/cache/apk/* ${DOCKAGE_ETC_DIR}/sbin ${DOCKAGE_WEBROOT_DIR}/*     && ln -s /usr/bin/php-fpm5 /usr/bin/php-fpm
ADD dir:1131dc0e6ee923a4d0508ffd9735f95ed27dc76610642fc87e3868a468208513 in /etc/dockage
ENV DOCKAGE_WEBROOT_DIR=/var/www DOCKAGE_DATA_DIR=/data DOCKAGE_ETC_DIR=/etc/dockage DOCKAGE_LOG_DIR=/var/log
LABEL org.label-schema.name=alpine-nginx-php-fpm org.label-schema.vendor=Dockage org.label-schema.description=Docker Nginx & PHP-FPM image built on Alpine Linux org.label-schema.vcs-url=https://github.com/dockage/alpine-nginx-php-fpm org.label-schema.license=MIT
MAINTAINER Mohammad Abdoli Rad <m.abdolirad@gmail.com>
CMD ["/sbin/runit-init"]
RUN apk update     && apk --no-cache add runit     && mkdir -p ${SERVICE_AVAILABLE_DIR} ${SERVICE_ENABLED_DIR}     && chmod +x /opt/installer     && sync     && /opt/installer     && rm -rf /var/cache/apk/* /opt/installer
ADD 8e8de944436a7d7eb6f19b5a19b5fe395975dadd3cac15baa41c111d0ca6e82f in /opt/
ENV SVDIR=/service SVWAIT=7
ENV SERVICE_AVAILABLE_DIR=/etc/sv SERVICE_ENABLED_DIR=/service
STOPSIGNAL [SIGCONT]
LABEL org.label-schema.name=alpine-runit org.label-schema.vendor=Dockage org.label-schema.description=Docker image uses runit as a process supervision on Alpine Linux org.label-schema.vcs-url=https://github.com/dockage/alpine-runit org.label-schema.version=3.6 org.label-schema.license=MIT
MAINTAINER Mohammad Abdoli Rad <m.abdolirad@gmail.com>
RUN apk add --no-cache su-exec net-tools ca-certificates nano tar curl findutils
LABEL org.label-schema.name=alpine org.label-schema.vendor=Dockage org.label-schema.description=Alpine image that forms the base for Dockage's docker images. org.label-schema.vcs-url=https://github.com/dockage/alpine org.label-schema.version=3.6 org.label-schema.license=MIT
MAINTAINER Mohammad Abdoli Rad <m.abdolirad@gmail.com>
CMD ["/bin/sh"]
ADD file:cb381165dec3689cf77e902c07ea78ca4da6bce4f5ac1909eebd40dba3273bfe in /