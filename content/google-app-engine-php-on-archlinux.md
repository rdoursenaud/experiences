Title: Google App Engine PHP Development with PhpStorm on Arch Linux
Date: 2017-07-26 17:30
Category: Blog
Tags: GNU/Linux, Arch Linux, Google, Google Cloud, Google Cloud Platform, Google App Engine, PHP, JetBrains, PhpStorm
Slug:  gae-dev-phpstorm-archlinux
Status: published


[//]: # (TODO: package php55-memcache and php55-memcached? NO!!!! It should NOT be loaded for the appserver to work. It's checked in `devappserver2/php/check_environment.php`)

# Introduction
The Google App Engine is a very good PaaS solution. Setting up a development environment is not trivial task. Make sure to read the official documentation for proper understanding.

Today we'll deal with the PHP Standard environment.

# Installation
Read the [Official instructions](https://cloud.google.com/appengine/docs/standard/php/tools/using-local-server) first.

1. Install the Google Cloud SDK from the AUR
2. Install php55 from the AUR
3. Install php55-appengine from the AUR (https://github.com/GoogleCloudPlatform/appengine-php-extension)
4. (Optional) Install php55-xdebug from the AUR

## Setup

### PHP

[//]: # (TODO: Enable all extensions provided by the Standard Runtime Environment. See: https://cloud.google.com/appengine/docs/standard/php/runtime)

Enable the `bcmath` extension that is required.  
Edit `/etc/php55/php.ini` and add to the extensions list:
```ini
extension=bcmath.so
```

To allow php tooling from the Google Cloud SDK to run, append its paths to the `open_basedir` directive in `/etc/php55/php.ini`:
```ini
:/opt/google-cloud-sdk/platform/google_appengine/google/appengine/tools/devappserver2/php:/opt/google-cloud-sdk/platform/google_appengine/google/appengine/sdk/php
```

To disable `html_errors` for better CLI debugging, create `/etc/php55/conf.d/disable_html_errors.ini`:
```ini
html_errors = Off
```

## Run

# From the CLI
Run `dev_appserver.py` with the following options:
```shell
/opt/google-cloud-sdk/platform/google_appengine/dev_appserver.py --php_executable_path /usr/bin/php55-cgi --php_gae_extension_path /usr/lib/php55/modules/gae_runtime_module.so --php_xdebug_extension_path=/usr/lib/php55/modules/xdebug.so --log_level debug .
```

[//]: # (TODO: Breakdown the option flags)

I like to run my development server in debug mode all the time but you can remove `--log_level debug` if you don't need it.

If you have any error, you can append the `--dev_appserver_log_level debug` for a more verbose output.

# In PhpStorm
Start a new Google App Engine project.  
In the `Settings`, set the PHP level to "PHP 5.5".  
Add a `PHP 5.5` interpreter to `/usr/bin/php55` and add the xdebug path.  
Edit the run "Run/Debug Configuration" and add the following to the `Interpreter options`:
```shell
--php_executable_path /usr/bin/php55-cgi --php_gae_extension_path /usr/lib/php55/modules/gae_runtime_module.so --php_xdebug_extension_path /usr/lib/php55/modules/xdebug.so --log_level debug
```
