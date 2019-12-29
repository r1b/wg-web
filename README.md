# wg-web

Developer tools for interacting with the Wireguard kernel module.

## wg-api

A RESTful API for managing Wireguard interfaces & peers. Manages the kernel
state with `netlink` messages. Synchronizes the kernel state to a local database.

## wg-cli

A utility for interacting with `wg-api`.
