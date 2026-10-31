![Banner](banner.png)

# configdrift-ScheduledConfigCheck
A simple scheduler that periodically runs a user-defined command (e.g., a configuration extraction script) and compares the output to a baseline. Alerts if differences are found. Uses `schedule` and `subprocess`. - Focused on Detects and reports deviations from baseline configurations across systems or applications. Compares current configurations to a known-good state, highlighting changes that could introduce security vulnerabilities or compliance issues. Supports multiple configuration formats (e.g., YAML, JSON) and remote configuration retrieval.

## Install
`git clone https://github.com/ShadowStrikeHQ/configdrift-scheduledconfigcheck`

## Usage
`./configdrift-scheduledconfigcheck [params]`

## Parameters
- `-h`: Show help message and exit
- `--interval`: No description provided
- `--output`: Path to output differences to file.
- `--format`: No description provided
- `--remote`: Treat the baseline as a URL to fetch the baseline configuration from.
- `--allow-http`: Allow fetching a remote baseline over plain http. Without this flag a remote baseline URL must use https.

A remote baseline is fetched with a 10 second timeout and is trusted as the known good baseline: whatever the URL returns is treated as the correct configuration to compare against, so use a source you trust. Remote baselines must use https unless `--allow-http` is passed for a plain http URL.

## License
Copyright (c) ShadowStrikeHQ
