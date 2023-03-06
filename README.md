# SlackMate (with Python & Slack-Bolt)

This is a SlackBot built with Python and the Slack Bolt library. The SlackBot can respond to messages in specific channels, create new channels and respond to different commands.


# Getting Started

1. Create a new Slack App and Bot User: Follow the instructions [here](https://medium.com/@arthur1cp/maximizing-productivity-the-power-of-slackbots-ce82a91c6de0) to create a new Slack App and Bot User.
2. Install the Slack App: Install the Slack App in your workspace by clicking the "Install App" button on the "Basic Information" page of your Slack App.
3. Set up your environment: Clone this repository and install the required Python packages using pip.

```
git clone https://github.com/yourusername/slackbot.git`
pip install slack-bolt
pip install slack-cdk
```

4. Set your environment variables: Set your Slack Bot token Slack App token as environment variables.
```
export SLACK_APP_TOKEN='your-slack-app-token'
export SLACK_BOT_TOKEN='your-slack-bot-token'
```
5. Run the SlackBot: Start the SlackBot by running the following command.
```
python slackmate.py
```


# Contributing
If you'd like to contribute to this SlackBot, feel free to fork this repository and submit a pull request.

# License
This SlackBot is licensed under the MIT License. See the LICENSE file for details.

# Acknowledgments
This SlackBot was built using the Slack Bolt library. Special thanks to the developers of these tools for making this project possible.

