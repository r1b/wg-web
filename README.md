# wg-web

Developer tools for interacting with the Wireguard kernel module. @zx2c4
provides a [general spec](https://docs.google.com/document/d/1_3Id-0vVXlXHFB7eT6fnfXoe9ppJoS8pY7R_uCtEZG4/edit).

## wg-api

A REST API for managing Wireguard interfaces & peers. Maintains the
configuration in a local database.

## wg-cli

A utility for interacting with `wg-api`.

## wg-daemon

Synchronizes an interface's state to the kernel by:

1. Generating a temporary configuration file
2. Calling `wg syncconf <interface> <config_file>`

Using `syncconf` is less efficient than computing a diff over the configuration
but easier to implement. The API *must* send the entire configuration for an
inteface when it is modified.

Exposes a simple RESTful API.

Sample interaction:

POST /api/v1/sync/

```
{"interface": {"name": "wg0", "addresses": ["10.10.10.1/24"], "private_key": "yAnz5TF+lXXJte14tji3zlMNq+hd2rYUIgJBgB3fBmk=", "listen_port": 6666, "peers": [{"public_key": "xTIBA5rboUvnH4htodjb6e697QjLERt1NAB4mZqp8Dg=", "addresses": ["10.10.10.2/32"]}]}}
```

## ~~wg-ui~~

I am a poor UI engineer - someone else should do this.
