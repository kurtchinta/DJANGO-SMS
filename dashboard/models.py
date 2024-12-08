from django.db import models
from twilio.rest import Client

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Correct Twilio credentials without trailing commas
        account_sid = 'ACcf46515f1e8daf2dbf0db735f32c1b57'
        auth_token = 'bbec661c728a300a0a663e3b965238d0'
        client = Client(account_sid, auth_token)

        if self.score >= 70:
            message_body = (
                f"Hey! {self.name}, I just want you to know that you are worthy since your score is {self.score}."
            )
        else:
            message_body = (
                f"Hey! {self.name}, I just want you to know that you are not worthy since your score is {self.score}."
            )

        try:
            # Send the SMS
            message = client.messages.create(
                body=message_body,
                from_='+16814122387',  # Replace with your Twilio number
                to='+639073042157'    # Replace with the recipient's number
            )
            print(f"Message sent successfully: {message.sid}")
        except Exception as e:
            print(f"Failed to send message: {e}")

        # Call the parent class's save method
        return super().save(*args, **kwargs)
