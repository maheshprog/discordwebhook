from discord_webhook import DiscordWebhook
webhook_url = input("Webhook URL: ")
while True:
    message_content = input(">> ")
    if message_content.lower() == 'exit':
        break
    webhook = DiscordWebhook(url=webhook_url, content=message_content)
    response = webhook.execute()
    if response.ok:
        print('Message sent successfully!')
    else:
        print('Error code:', response.status_code)
print('Shutting Down...')
