# SEEDbox

[![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Ansible-based Docker containerized cloud media server

A modern stack built with Ansible around Docker, Traefik and Homer. Secured by Cloudflare and CrowdSec for maximum security and with the least exposure on internet. Easily deployable and using the best open-source projects.

> [!WARNING]
> Please be aware that this is a work in progress (WIP) project and it is going to evolve in the coming week/months (as of Feb. 2026).

## Screenshot
![dashboard](https://user-images.githubusercontent.com/89345101/134022283-160d5070-68c2-4cdc-afed-482a92fcf339.png)

## Table of Contents

- [Background](#background)
- [Important Notices](#important-notices)
- [Install](#install)
- [Usage](#usage)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Background

We wanted a better, more modern solution that swizzin. Simpler and easier to maintain than Cloudbox & Saltbox. And made with the best open-source projects and the best ideas. That's how SEEDbox was born.

## Important Notices

> [!IMPORTANT]
> Operating systems supported and software required: 
> - Debian 13 (Trixie) - 64-bit (amd64)
> - Ansible 12 / ansible-core 2.19 and up
> - Python 3.13 and up
> - Docker 29.x / Docker Compose 5.x and up

> [!IMPORTANT]
> Requirements:
> - Custom domain name
> - Cloudflare account
>
> Optional:
> - CrowdSec account

> [!NOTE]
> Check the documentation in the Wiki for more details

> [!IMPORTANT]
> Minimal Stack (mandatory "core" role):
> - [Docker](https://www.docker.com/)
> - [Cloudflare](https://www.cloudflare.com/)
> - [Traefik](https://traefik.io/)
> - [Portainer](https://www.portainer.io/)
> - [Authelia](https://www.authelia.com/)
> - [filetree](https://github.com/Pro-Tweaker/SEEDbox/blob/main/roles/filetree/tasks/main.yml)
> - [Homer](https://github.com/bastienwirtz/homer)
> - [Homer Service Discovery](https://github.com/Pro-Tweaker/homer-service-discovery)
> - [Dashboard Icons](https://github.com/homarr-labs/dashboard-icons)
> - [Watchtower](https://github.com/containrrr/watchtower)
> - [postfix](https://github.com/bokysan/docker-postfix)

## Install

Install the minimal required packages to use the SEEDbox playbook:
```sh
apt update && apt upgrade
apt install git python3 pip ansible
```

Install the Docker collection from Ansible Galaxy:
```sh
ansible-galaxy collection install community.docker
```

Optional : Check Ansible version:
```sh
ansible --version
ansible --version | grep "python version"
ansible-community --version
```

Prepare a folder, clone this repo, prepare the default file:
```sh
cd /home/username
git clone https://github.com/Pro-Tweaker/SEEDbox.git
cp SEEDbox\defaults\settings.yml.default SEEDbox\settings.yml
```

Customize the seetings.yml with your custom informations:
```sh
nano settings.yml
```

## Usage

Run the docker role or directly all core role(s):
```sh
sudo ansible-playbook seedbox.yml --tags=docker
sudo ansible-playbook seedbox.yml --tags=core
```

Optional : Check Docker version:
```sh
docker --version
docker-compose --version
docker info
```

Run the desired optionnal roles:
```sh
sudo ansible-playbook seedbox.yml --tags=download,pvr,media,tools,monitoring
```

Or the single roles:
```sh
sudo ansible-playbook seedbox.yml --tags=qbittorrent,jellyfin
```
### Applications and roles available:

#### Role : "Download"
- [Flood](https://flood.js.org/)
- [qBittorrent](https://www.qbittorrent.org/)
- [rTorrent](https://rakshasa.github.io/rtorrent/)
- [ruTorrent](https://github.com/Novik/ruTorrent)
- [NZBGet](https://nzbget.net/)
- [SABnzbd](https://sabnzbd.org/)

#### Role : "Media"
- [Jellyfin](https://jellyfin.org/)
- [Navidrome](https://www.navidrome.org/)
- [Kavita](https://www.kavitareader.com/)

#### Role : "PVR" aka *arr apps
- [Prowlarr](https://prowlarr.com/)
- [Sonarr](https://sonarr.tv/)
- [Radarr](https://radarr.video/)
- [Lidarr](https://lidarr.audio/)
- [Readarr](https://readarr.com/)
- [Bazarr](https://www.bazarr.media/)

#### Role : "Tools"
- [File Browser](https://filebrowser.org/)
- [Syncthing](https://syncthing.net/)
- [ArchiveBox](https://archivebox.io/)
- [whoami](https://github.com/traefik/whoami/)

#### Role : "Monitoring"
- [Netdata](https://www.netdata.cloud/)
- [Speedtest Tracker](https://github.com/henrywhitaker3/Speedtest-Tracker)
- [LibreSpeed](https://librespeed.org/)
- [Scrutiny](https://github.com/AnalogJ/scrutiny)

> [!NOTE]
> A list of all the roles is available in the Wiki

## Maintainers

[@Pro-Tweaker](https://github.com/Pro-Tweaker)

[@zotabee](https://github.com/zotabee)

## Contributing

PRs to update/fix/enhance the stack accepted. We probably won't add roles for projects we don't already have selected.

## License

MIT © 2026 Pro-Tweaker & zotabee
