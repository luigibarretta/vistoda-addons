# Vistoda Apps for Home Assistant

This repository installs the provider runtimes used by Vistoda on Home
Assistant OS and Home Assistant Supervised. Install only the providers you use:

- **Vistoda Blink** for Blink cameras, clips, snapshots and bounded live media;
- **Vistoda EZVIZ** for EZVIZ VTM/VTDU snapshots and live media;
- **Vistoda Ring** for Ring Intercom controls, full-duplex audio and local
  recordings.

Each app keeps its provider credentials and rotating sessions inside its own
persistent `/data` volume. It publishes a private Supervisor discovery message
to the Vistoda integrations. Users never need to enter a bridge URL, port or API
token in the normal Home Assistant setup flow.

## Install

[![Install Vistoda through HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=luigibarretta&repository=vistoda-home-assistant&category=integration)
[![Install Vistoda Blink through HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=luigibarretta&repository=vistoda-blink&category=integration)
[![Add the Vistoda app repository to Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fluigibarretta%2Fvistoda-addons)

1. Install **Vistoda** through HACS. Install **Vistoda Blink** too only when
   using Blink cameras.
2. Use the button above, or add this repository to Settings → Apps → App
   store → Repositories.
3. Install and start the Vistoda provider apps you need.
4. Open Settings → Devices & services and complete the discovered Vistoda flow.

Repository URL:

`https://github.com/luigibarretta/vistoda-addons`

Home Assistant Container/Core users can run the same Rust provider images as
external services. Manual URL and API-token configuration remains available as
an advanced fallback; it is not the default installation path.

## Release contract

App versions match the immutable provider image tags. Every image must provide
both `amd64` and `aarch64` manifests before its metadata version is published.
The app network ports are private by default and no provider listener is
published to the host.

Release workflows build on native GitHub `amd64` and `aarch64` runners,
apply Home Assistant architecture labels and sign both images and the generic
manifest with keyless Cosign.

Licensed under the Apache License 2.0.
