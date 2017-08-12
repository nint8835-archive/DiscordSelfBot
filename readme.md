# DiscordSelfBot

## Docker Installation

1. Clone repository
    ```shell
    git clone https://github.com/nint8835/DiscordSelfBot.git
    ```
2. Copy the existing config file
    ```shell
    cd DiscordSelfBot
    cp template_config.json config.json
    ```
3. Edit the config file
    * Replace `YOUR EMAIL HERE` with the email address used to register your Discord account
    * Replace `YOUR TOKEN HERE` with your Discord token. You can retrieve this using part one of [this guide](https://github.com/TheRacingLion/Discord-SelfBot/wiki/Discord-Token-Tutorial).
4. Build the Docker image
    ```shell
    docker build --tag discordselfbot .
    ```
5. Start the Docker container
    ```shell
    docker run -d --rm --name discordselfbot discordselfbot
    ```
6. Stop the bot when you are done
    ```shell
    docker container stop discordselfbot
    ```
