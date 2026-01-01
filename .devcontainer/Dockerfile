FROM ubuntu:24.04

ARG GIT_USER
ARG GIT_MAIL

COPY <<EOF /etc/sudoers.d/ubuntu
ubuntu ALL=(ALL) NOPASSWD:ALL

EOF

RUN <<EOF
apt-get update
apt-get install -y tzdata
ln -fs /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
EOF

RUN <<EOF
apt-get update
apt-get install -y sudo curl git
apt-get install -y systemd systemd-sysv
EOF

USER ubuntu
RUN <<EOF
curl -LsSf https://astral.sh/uv/install.sh | sh
git config --global init.defaultBranch main
git config --global user.name "${GIT_USER}"
git config --global user.email "${GIT_MAIL}"
EOF

USER root
ENTRYPOINT ["/sbin/init"]
