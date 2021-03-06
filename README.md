# LslProcessor

## Setup

This section explains how to install and uninstall the project.

Install pip package from GitHub.

```sh
pip3 install git+https://git@github.com/FunTimeCoding/lsl-processor.git#egg=lsl-processor
```

Install pip package from DevPi.

```sh
pip3 install -i https://testpypi.python.org/pypi lsl-processor
```

Uninstall package.

```sh
pip3 uninstall lsl-processor
```


## Usage

This section explains how to use the project.

Run program.

```sh
lp
```


## Development

This section explains how to improve the project.

Configure Git on Windows before cloning. This avoids problems with Vagrant and VirtualBox.

```sh
git config --global core.autocrlf input
```

Build project. This installs dependencies.

```sh
script/build.sh
```

Run tests, check style and measure metrics.

```sh
script/test.sh
script/check.sh
script/measure.sh
```

Build package.

```sh
script/package.sh
```

Install Debian package.

```sh
sudo dpkg --install build/python3-lsl-processor_0.1.0-1_all.deb
```

Show files the package installed.

```sh
dpkg-query --listfiles python3-lsl-processor
```
