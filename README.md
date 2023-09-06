# AWS-EC2-Nginx-Monitoring-and-Gmail-Notification-with-Python
# Application Monitoring Script

This is a Python script for monitoring the status of an application and restarting it if it's down. The script uses the following tools/libraries:

*   `requests` for sending HTTP requests to the monitored application
*   `smtplib` for sending email notifications to the script owner
*   `paramiko` for SSH connection to the server running the application
*   `schedule` for scheduling the script to run in intervals

## Prerequisites

*   Python 3.x
*   `requests` library (`pip install requests`)
*   `paramiko` library (`pip install paramiko`)
*   Access to the email account used for sending notifications
*   Access to the server running the monitored application

## Configuration

Before running the script, make sure to update the following variables in the code:

*   `EMAIL_ADDRESS`: The email address used for sending notifications
*   `EMAIL_PASSWORD`: The password for the email account
*   `hostname`: The hostname or IP address of the server running the monitored application
*   `username`: The SSH username for the server
*   `key_filename`: The path to the SSH private key file for the server
*   `docker_container`: The name or ID of the Docker container running the application

## Usage

To run the script, simply execute the following command in the terminal:

    python monitor_app.py

The script will start monitoring the application and send email notifications if it's down. If the application is down, the script will attempt to restart it by running the `docker start` command on the server.

By default, the script runs every 5 seconds. You can adjust this interval by modifying the `schedule.every(5).seconds` line in the code.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

*   This project was inspired by similar application monitoring scripts available in GitHub and other sources.
