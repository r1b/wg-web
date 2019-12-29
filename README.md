# wg-web

Developer tools for interacting with the Wireguard kernel module. @zx2c4
provides a [general spec](https://docs.google.com/document/d/1_3Id-0vVXlXHFB7eT6fnfXoe9ppJoS8pY7R_uCtEZG4/edit).

## wg-api

A RESTful API for managing Wireguard interfaces & peers. Maintains the
configuration in a local database.

## wg-cli

A utility for interacting with `wg-api`.

## wg-nl

Synchronizes the database state to the kernel with `netlink` messages.

## ~~wg-ui~~

I am a poor UI engineer - someone else should do this.
