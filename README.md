# SEEDbox

![GitHub Created At](https://img.shields.io/github/created-at/Pro-Tweaker/SEEDbox)
![GitHub last commit](https://img.shields.io/github/last-commit/Pro-Tweaker/SEEDbox)
![GitHub contributors](https://img.shields.io/github/contributors/Pro-Tweaker/SEEDbox)
![GitHub License](https://img.shields.io/github/license/Pro-Tweaker/SEEDbox)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Ansible-based Docker containerized cloud media server

A modern stack built with Ansible around Docker, Traefik, and Homer. It is secured by Cloudflare and CrowdSec for enhanced protection and minimal exposure to the internet. Easily deployable and built using leading open-source projects.

![dashboard](https://user-images.githubusercontent.com/89345101/134022283-160d5070-68c2-4cdc-afed-482a92fcf339.png)

> [!WARNING]
> Please be aware that this is a work in progress (WIP) and will continue to evolve in the coming weeks/months (as of Feb. 2026).

## Table of Contents

- [Background](#background)
- [Install](#install)
    - [Prerequisites](#prerequisites)
    - [Getting started](#getting-started)
- [Usage](#usage)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Background

We wanted a better, more modern solution than swizzin. Simpler and easier to maintain than Cloudbox & Saltbox. Made with the best open-source projects and the best ideas. That's how SEEDbox was born.

## Install

### Prerequisites

> [!IMPORTANT]
> Supported operating systems and software versions:
> - Debian 13 (Trixie) - 64-bit (amd64)
> - Ansible 12 / ansible-core 2.19 and newer
> - Python 3.13 and newer
> - Docker 29.x / Docker Compose 5.x and newer

> [!IMPORTANT]
> Requirements:
> - Custom domain name
> - Cloudflare account
>
> Optional:
> - CrowdSec account

> [!NOTE]
> Check the documentation in the [Wiki](https://github.com/Pro-Tweaker/SEEDbox/wiki) for more details!

### Getting started

> [!TIP]
> You might need to run some of these commands as `sudo`, depending on your environment.

Install the minimal required packages to use the SEEDbox playbook:
```sh
apt update && apt install -y git python3 python3-pip python3-lxml ansible
```

Install the Docker collection from Ansible Galaxy:
```sh
ansible-galaxy collection install community.docker
```

Optional: Check Ansible version:
```sh
ansible --version
```

Prepare a folder, clone this repo, and copy the default settings file:
```sh
cd /home/username
git clone https://github.com/Pro-Tweaker/SEEDbox.git
cp SEEDbox/defaults/settings.yml.default SEEDbox/settings.yml
```

Customize `settings.yml` with your information:
```sh
nano settings.yml
```

## Usage

> [!TIP]
> You might need to run some of these commands as `sudo`, depending on your environment and the roles used.

> [!IMPORTANT]
> Minimal stack (mandatory `core` roles):
> - [Docker](https://www.docker.com/)
> - [Cloudflare](https://www.cloudflare.com/)
> - [CrowdSec](https://www.crowdsec.net/)
> - [Traefik](https://traefik.io/)
> - [Portainer](https://www.portainer.io/)
> - [Authelia](https://www.authelia.com/)
> - [filetree](https://github.com/Pro-Tweaker/SEEDbox/blob/main/roles/filetree/tasks/main.yml)
> - [Homer](https://github.com/bastienwirtz/homer)
> - [Homer Service Discovery](https://github.com/Pro-Tweaker/homer-service-discovery)
> - [Dashboard Icons](https://github.com/homarr-labs/dashboard-icons)
> - [Watchtower](https://github.com/nicholas-fedor/watchtower)

Run the Docker role or all mandatory core roles using the `core` tag:
```sh
ansible-playbook seedbox.yml --tags=docker
ansible-playbook seedbox.yml --tags=core
```

Optional: Check Docker version and status:
```sh
docker --version
docker-compose --version
docker info
```

Run the desired optional tags:
```sh
ansible-playbook seedbox.yml --tags=download,pvr,media,tools,monitoring
```

Or run single roles:
```sh
ansible-playbook seedbox.yml --tags=qbittorrent,jellyfin
```
### Applications (roles) and tags available:

#### Tag: "Download"
- [qBittorrent](https://www.qbittorrent.org/)
- [ruTorrent](https://github.com/Novik/ruTorrent) ([rTorrent](https://rakshasa.github.io/rtorrent/))
- [NZBGet](https://nzbget.com/)
- [SABnzbd](https://sabnzbd.org/)
- [Flood](https://flood.js.org/)
- [qui](https://getqui.com/)

#### Tag: "PVR"
- [Prowlarr](https://prowlarr.com/)
- [Sonarr](https://sonarr.tv/)
- [Radarr](https://radarr.video/)
- [Lidarr](https://lidarr.audio/)
- [Readarr](https://readarr.com/)
- [Bazarr](https://www.bazarr.media/)

#### Tag: "Media"
- [Seerr](https://seerr.dev/)
- [Jellyfin](https://jellyfin.org/)
- [Navidrome](https://www.navidrome.org/)
- [Kavita](https://www.kavitareader.com/)
- [Yamtrack](https://github.com/FuzzyGrim/Yamtrack)

#### Tag: "Tools"
- [File Browser](https://filebrowser.org/)
- [Syncthing](https://syncthing.net/)
- [ArchiveBox](https://archivebox.io/)
- [whoami](https://github.com/traefik/whoami/)

#### Tag: "Monitoring"
- [Netdata](https://www.netdata.cloud/)
- [Speedtest Tracker](https://github.com/henrywhitaker3/Speedtest-Tracker)
- [LibreSpeed](https://librespeed.org/)
- [Scrutiny](https://github.com/AnalogJ/scrutiny)

#### Tag: "Extras"
- [Tinymotd](https://github.com/bderenzo/tinymotd)
- [Utils](https://github.com/Pro-Tweaker/SEEDbox/wiki/Utils)

> [!TIP]
> You can check all the roles and tags available in the playbook file: [seedbox.yml](https://github.com/Pro-Tweaker/SEEDbox/blob/main/seedbox.yml)

## Maintainers

[@Pro-Tweaker](https://github.com/Pro-Tweaker)

[@zotabee](https://github.com/zotabee)

## Contributing

PRs to update, fix, or enhance the stack accepted. We will likely not add roles for projects that are not already part of the selected stack.

## License

MIT © 2026 Pro-Tweaker & zotabee
